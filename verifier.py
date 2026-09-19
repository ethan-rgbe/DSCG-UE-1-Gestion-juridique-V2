#!/usr/bin/env python3
"""
verifier.py — Diagnostic du dépôt, sans rien modifier.

    python3 scripts/verifier.py

Affiche l'inventaire des fichiers, l'état de la restructuration et la liste
des anomalies, en distinguant celles qui bloquent la publication de celles
qui sont sans conséquence.

Ce script ne modifie aucun fichier et ne génère pas le site.
"""

import json
import os
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

BLOQUANT, SIGNALE = [], []


def charger(nom, requis=True):
    chemin = os.path.join(DATA, nom)
    if not os.path.exists(chemin):
        if requis:
            BLOQUANT.append(f"data/{nom} est absent du dépôt")
        return None
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        BLOQUANT.append(f"data/{nom} n'est pas un JSON valide : ligne {e.lineno}, {e.msg}")
        return None


def titre(t):
    print("\n" + t)
    print("-" * len(t))


def main():
    print("=" * 62)
    print("DIAGNOSTIC DU DÉPÔT")
    print("=" * 62)

    chapitres = charger("chapitres.json")
    notions = charger("notions.json")
    fiches = charger("fiches.json")
    cartes = charger("qr_cartes.json")
    tableaux = charger("tableaux_comparatifs.json")
    annales = charger("annales.json")
    programme = charger("programme.json")
    points = charger("points_attention.json")
    blocs = charger("blocs.json", requis=False)
    tab_blocs = charger("tableaux_blocs.json", requis=False)

    if chapitres is None or notions is None:
        print("\nFichiers essentiels manquants : diagnostic interrompu.")
        return 1

    chap_ids = {c["id"] for c in chapitres}
    notion_ids = {n["id"] for n in notions}
    tab_ids = {t["id"] for t in (tableaux or [])}
    if tab_blocs:
        tab_ids |= {t["id"] for t in tab_blocs}

    # ---------------- Inventaire ----------------
    titre("INVENTAIRE")
    md_blocs = sorted(glob.glob(os.path.join(ROOT, "content", "blocs", "*.md")))
    ids_md = {os.path.splitext(os.path.basename(p))[0] for p in md_blocs}
    print(f"  chapitres ................. {len(chapitres)}")
    print(f"  notions ................... {len(notions)}")
    print(f"  blocs ..................... {len(blocs) if blocs is not None else 'fichier absent'}")
    print(f"  fiches de blocs (.md) ..... {len(ids_md)}")
    print(f"  tableaux comparatifs ...... {len(tableaux or [])}")
    print(f"  tableaux issus des fiches . {len(tab_blocs) if tab_blocs is not None else 'fichier absent'}")
    print(f"  cartes Q/R ................ {len(cartes or [])}")
    print(f"  fiches (ancien format) .... {len(fiches or [])}")

    # ---------------- Restructuration ----------------
    titre("ÉTAT DE LA RESTRUCTURATION")
    attendus = {
        "data/blocs.json": blocs is not None,
        "data/tableaux_blocs.json": tab_blocs is not None,
        "content/blocs/": len(ids_md) > 0,
        "chapitres avec statut": any("statut" in c for c in chapitres),
    }
    for nom, present in attendus.items():
        print(f"  [{'✓' if present else '✗'}] {nom}")

    if blocs is not None:
        avec = sum(1 for b in blocs if b.get("id") in ids_md)
        print(f"\n  Blocs pourvus d'une fiche : {avec}/{len(blocs)}")
        sans_bloc = sorted(ids_md - {b.get("id") for b in blocs})
        if sans_bloc:
            SIGNALE.append(f"{len(sans_bloc)} fiche(s) sans bloc déclaré : {', '.join(sans_bloc[:4])}")

    # ---------------- Contrôles ----------------
    if blocs is not None:
        vus = set()
        for b in blocs:
            bid = b.get("id")
            if not bid:
                BLOQUANT.append("un bloc n'a pas d'identifiant")
                continue
            if bid in vus:
                BLOQUANT.append(f"bloc '{bid}' : identifiant en double")
            vus.add(bid)
            if b.get("chapitre_id") not in chap_ids:
                BLOQUANT.append(f"bloc '{bid}' : chapitre '{b.get('chapitre_id')}' inexistant")
            for nid in b.get("notions_liees") or []:
                if nid not in notion_ids:
                    SIGNALE.append(f"bloc '{bid}' renvoie à la notion absente '{nid}'")
            for tid in b.get("tableaux_lies") or []:
                if tid not in tab_ids:
                    SIGNALE.append(f"bloc '{bid}' renvoie au tableau absent '{tid}'")

    for n in notions:
        if n.get("chapitre_id") not in chap_ids:
            BLOQUANT.append(f"notion '{n['id']}' : chapitre inexistant")

    for t in (tab_blocs or []):
        cols = (t.get("contenu") or {}).get("colonnes") or []
        for i, r in enumerate((t.get("contenu") or {}).get("lignes") or []):
            if len(r) != len(cols):
                BLOQUANT.append(f"tableau '{t.get('id')}' ligne {i} : {len(r)} cellules pour {len(cols)} colonnes")
        if t.get("chapitre_id") not in chap_ids:
            BLOQUANT.append(f"tableau '{t.get('id')}' : chapitre inexistant")

    if annales:
        for a in annales:
            for d in a.get("rattachement", []):
                cid = d.get("chapitre_id")
                if cid and cid not in chap_ids:
                    BLOQUANT.append(f"annales {a.get('annee')} D{d.get('dossier')} : chapitre '{cid}' inexistant")
                for q in d.get("questions", []):
                    nid = q.get("notion_id")
                    if nid and nid not in notion_ids:
                        SIGNALE.append(f"annales {a.get('annee')} {q.get('num')} : notion absente '{nid}'")

    if programme:
        for p in programme.get("parties", []):
            for sp in p.get("sous_parties", []):
                cid = sp.get("chapitre_id")
                if cid and cid not in chap_ids:
                    BLOQUANT.append(f"programme : chapitre '{cid}' inexistant")
                if not cid:
                    SIGNALE.append(f"programme : '{sp.get('titre')}' n'est rattaché à aucun chapitre")

    if points:
        for cid in points:
            if cid not in chap_ids:
                SIGNALE.append(f"points d'attention : chapitre '{cid}' inexistant")

    # ---------------- Rapport ----------------
    titre("RÉSULTAT")
    if BLOQUANT:
        print(f"  {len(BLOQUANT)} anomalie(s) BLOQUANTE(S) — la publication sera interrompue :")
        for x in BLOQUANT[:25]:
            print("    ✗", x)
        if len(BLOQUANT) > 25:
            print(f"    … (+{len(BLOQUANT) - 25} autres)")
    else:
        print("  ✓ Aucune anomalie bloquante : la publication peut avoir lieu.")

    if SIGNALE:
        print(f"\n  {len(SIGNALE)} point(s) signalé(s) — sans effet sur la publication,")
        print("  le site ignore les renvois vers un élément absent :")
        for x in SIGNALE[:15]:
            print("    ·", x)
        if len(SIGNALE) > 15:
            print(f"    … (+{len(SIGNALE) - 15} autres)")
        if tab_blocs is None:
            print("\n  → data/tableaux_blocs.json est absent : c'est la cause la plus")
            print("    probable des renvois non résolus vers des tableaux.")

    print()
    return 1 if BLOQUANT else 0


if __name__ == "__main__":
    sys.exit(main())
