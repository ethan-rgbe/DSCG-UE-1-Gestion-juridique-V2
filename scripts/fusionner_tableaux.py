#!/usr/bin/env python3
"""
fusionner_tableaux.py — Intègre data/tableaux_blocs.json dans
data/tableaux_comparatifs.json, puis supprime le premier fichier.

    python3 scripts/fusionner_tableaux.py

À lancer UNE SEULE FOIS. L'opération est prudente :
  - une sauvegarde horodatée du fichier principal est créée avant écriture ;
  - aucun tableau existant n'est modifié ni supprimé ;
  - les identifiants déjà présents sont ignorés, jamais écrasés ;
  - un titre en double interrompt l'opération sans rien écrire, car deux
    tableaux homonymes rendent ambigus les renvois « (voir tableau lié) ».

Après fusion, build.py n'a plus rien à fusionner au chargement : les nouveaux
tableaux sont des tableaux comme les autres, révisables en mode Reconstituer.
"""

import json
import os
import shutil
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
PRINCIPAL = os.path.join(DATA, "tableaux_comparatifs.json")
BLOCS = os.path.join(DATA, "tableaux_blocs.json")


def main():
    if not os.path.exists(BLOCS):
        print("data/tableaux_blocs.json est absent : rien à fusionner.")
        print("Si la fusion a déjà eu lieu, il n'y a rien à faire.")
        return 0
    if not os.path.exists(PRINCIPAL):
        print("ERREUR : data/tableaux_comparatifs.json est introuvable.")
        return 1

    with open(PRINCIPAL, encoding="utf-8") as f:
        principal = json.load(f)
    with open(BLOCS, encoding="utf-8") as f:
        nouveaux = json.load(f)

    ids = {t.get("id") for t in principal}
    titres = {(t.get("titre") or "").strip().lower(): t.get("id") for t in principal}

    a_ajouter, deja, conflits = [], [], []
    for t in nouveaux:
        tid = t.get("id")
        if tid in ids:
            deja.append(tid)
            continue
        cle = (t.get("titre") or "").strip().lower()
        if cle in titres:
            conflits.append((tid, titres[cle], t.get("titre")))
            continue
        a_ajouter.append(t)
        ids.add(tid)
        titres[cle] = tid

    print(f"Tableaux existants ........ {len(principal)}")
    print(f"Tableaux à intégrer ....... {len(nouveaux)}")
    print(f"  déjà présents ........... {len(deja)}")
    print(f"  titres en conflit ....... {len(conflits)}")
    print(f"  à ajouter ............... {len(a_ajouter)}")

    if conflits:
        print("\nOpération interrompue : les titres suivants existent déjà.")
        for tid, autre, titre in conflits:
            print(f"  · {tid} porte le même titre que {autre} : « {titre} »")
        print("\nRenommez l'un des deux, puis relancez. Aucun fichier n'a été modifié.")
        return 1

    if not a_ajouter:
        print("\nRien à ajouter. Le fichier data/tableaux_blocs.json peut être supprimé.")
        return 0

    horodatage = datetime.now().strftime("%Y%m%d-%H%M%S")
    sauvegarde = PRINCIPAL.replace(".json", f".sauvegarde-{horodatage}.json")
    shutil.copy(PRINCIPAL, sauvegarde)

    principal.extend(a_ajouter)
    with open(PRINCIPAL, "w", encoding="utf-8") as f:
        json.dump(principal, f, ensure_ascii=False, indent=2)

    os.remove(BLOCS)

    print(f"\n✓ {len(a_ajouter)} tableaux intégrés — total : {len(principal)}")
    print(f"✓ sauvegarde : {os.path.basename(sauvegarde)}")
    print("✓ data/tableaux_blocs.json supprimé")
    print("\nLancez maintenant : python3 scripts/build.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
