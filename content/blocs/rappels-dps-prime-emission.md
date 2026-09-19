# RAPPELS DCG — DPS, PRIME D'ÉMISSION ET DROIT D'ATTRIBUTION

*Mécanismes et calculs des augmentations de capital*
*Référentiel DSCG UE1 — droit positif vérifié au 3 septembre 2026*

---

> **Rattachement** — fiche transversale destinée au chapitre « Rappels DCG ». Elle complète, sur le plan calculatoire, le livret 3.1 « Le financement par fonds propres », qui en traite le régime juridique.

---

## A. FONDEMENTS JURIDIQUES DU BLOC

| Objet | Texte |
|---|---|
| Droit préférentiel de souscription | Art. **L. 225-132** C. com. |
| Suppression du DPS | Art. **L. 225-135** C. com. |
| Émission réservée à des personnes désignées | Art. **L. 225-138** C. com. |
| **Libération des actions et de la prime** | Art. **L. 225-144** C. com. |
| Actions d'apport | Art. **L. 225-147** C. com. |
| Souscriptions insuffisantes | Art. **L. 225-134** C. com. |
| Capital préalablement libéré | Art. **L. 225-131** C. com. |
| Délai d'exercice du DPS | Art. **R. 225-131** C. com. |

---

## B. LE PROBLÈME À RÉSOUDRE

Une augmentation de capital fait entrer de nouveaux actionnaires — ou modifie la répartition entre anciens. Elle produit deux effets défavorables aux actionnaires en place :

| Effet | Contenu |
|---|---|
| **Dilution politique** | Leur pourcentage de droits de vote diminue |
| **Dilution financière** | Les nouveaux accèdent aux **réserves accumulées** avant leur entrée, sans y avoir contribué |

**Deux instruments y répondent, et il faut bien voir qu'ils ne protègent pas les mêmes personnes :**

| Instrument | Qui protège-t-il ? | Contre quoi ? |
|---|---|---|
| **Prime d'émission** | La **société** et, indirectement, les anciens actionnaires | L'accès gratuit des nouveaux aux réserves |
| **DPS** | L'**actionnaire ancien**, individuellement | La dilution de sa participation |

---

## C. LES TROIS VALEURS DE L'ACTION

Tout calcul commence par identifier la valeur utilisée. Les confondre est la première cause d'erreur.

| Valeur | Définition | Usage |
|---|---|---|
| **Valeur nominale** (VN) | Capital social ÷ nombre d'actions | Plancher du prix d'émission ; base du capital |
| **Valeur mathématique** (ou intrinsèque) | Actif net comptable ÷ nombre d'actions | Sociétés non cotées |
| **Valeur boursière** (cours) | Prix constaté sur le marché | Sociétés cotées |

**Dans les calculs de DPS, la valeur de référence est la valeur de l'action *avant* l'augmentation** — cours de bourse pour une société cotée, valeur mathématique sinon.

---

## D. LA PRIME D'ÉMISSION

### D.1 — Définition et calcul

**La prime d'émission est la différence entre le prix d'émission et la valeur nominale de l'action.**

```
Prime d'émission unitaire = Prix d'émission − Valeur nominale
Prime d'émission totale   = Nombre d'actions nouvelles × (Prix d'émission − Valeur nominale)
```

### D.2 — L'encadrement du prix d'émission

```
Valeur nominale  ≤  Prix d'émission  ≤  Valeur de l'action avant augmentation
```

| Borne | Justification |
|---|---|
| **Plancher : la valeur nominale** | Interdiction d'émettre **au-dessous du pair** : le capital doit être intégralement couvert |
| **Plafond pratique : la valeur de l'action** | Au-delà, l'opération serait sans intérêt pour les souscripteurs |

**La prime n'est jamais obligatoire.** Mais son absence dilue financièrement les anciens actionnaires, qui voient les nouveaux accéder aux réserves sans contrepartie. Plus la prime est élevée, plus la protection des anciens est forte — et plus le DPS a une valeur faible.

### D.3 — Le traitement de la prime

| Point | Régime |
|---|---|
| **Nature** | La prime **n'entre pas dans le capital social** : elle figure en capitaux propres, au poste « primes d'émission » |
| **Conséquence** | Elle n'est pas soumise au régime du capital : sa distribution ou son incorporation obéit à des règles propres |
| **Libération** | **La totalité de la prime doit être libérée dès la souscription** (art. L. 225-144) |

> **⚠️ C'est la règle de libération la plus souvent manquée.** Les actions souscrites en numéraire sont libérées, lors de la souscription, **d'un quart au moins de leur valeur nominale** mais **de la totalité de la prime d'émission**. Le fractionnement ne concerne donc que le nominal.

---

## E. LE DROIT PRÉFÉRENTIEL DE SOUSCRIPTION

### E.1 — Mécanisme

Chaque action ancienne porte **un DPS**. Le rapport de souscription indique combien de DPS sont nécessaires pour souscrire une action nouvelle.

```
Rapport de souscription = N actions anciennes pour n actions nouvelles
```

**Exemple de lecture** : « 5 actions anciennes pour 2 nouvelles » signifie qu'il faut détenir 5 DPS pour souscrire 2 actions nouvelles.

### E.2 — Les deux issues pour l'actionnaire ancien

| Choix | Conséquence |
|---|---|
| **Il souscrit** | Il maintient sa participation ; son patrimoine est inchangé |
| **Il vend ses DPS** | Sa participation diminue, mais le prix de vente compense exactement sa perte de valeur |

**C'est toute la logique du DPS : il rend l'opération neutre pour l'actionnaire ancien, quel que soit son choix.**

---

## F. LES FORMULES

### F.1 — Valeur théorique de l'action après augmentation

C'est une **moyenne pondérée** entre les actions anciennes, valorisées à leur valeur avant opération, et les actions nouvelles, valorisées au prix d'émission.

```
                 (N × VA) + (n × PE)
        VAD  =  ─────────────────────
                       N + n
```

| Symbole | Signification |
|---|---|
| **N** | Nombre d'actions **anciennes** |
| **n** | Nombre d'actions **nouvelles** |
| **VA** | Valeur de l'action **avant** l'augmentation |
| **PE** | **Prix d'émission** de l'action nouvelle |
| **VAD** | Valeur théorique de l'action **après**, dite « ex-droit » |

### F.2 — Valeur théorique du DPS

Le DPS vaut exactement ce que l'action perd en valeur du fait de l'opération.

```
        DPS = VA − VAD
```

Ce qui, en développant, donne la formule directe :

```
                n × (VA − PE)
        DPS = ─────────────────
                    N + n
```

**Trois lectures utiles de cette formule :**

1. si **PE = VA**, le DPS vaut **zéro** : l'émission au prix du marché ne dilue personne ;
2. plus le **prix d'émission est bas**, plus le DPS est **élevé** — la décote est compensée par le droit ;
3. plus l'augmentation est **importante** relativement au capital existant, plus le DPS est élevé.

---

## G. EXEMPLE CHIFFRÉ COMPLET

**Données** — une société a un capital de 1 000 000 € divisé en **10 000 actions** de **100 € de valeur nominale**. L'action vaut **250 €**. Elle émet **2 000 actions nouvelles** au prix de **190 €**, à raison de **5 anciennes pour 1 nouvelle**.

### G.1 — La prime d'émission

```
Prime unitaire = 190 − 100 = 90 €
Prime totale   = 2 000 × 90 = 180 000 €
Augmentation de capital (nominal) = 2 000 × 100 = 200 000 €
Fonds levés = 2 000 × 190 = 380 000 €
```

### G.2 — La valeur ex-droit

```
        (10 000 × 250) + (2 000 × 190)     2 500 000 + 380 000
VAD =  ───────────────────────────────  =  ───────────────────  = 240 €
                 10 000 + 2 000                   12 000
```

### G.3 — La valeur du DPS

```
DPS = 250 − 240 = 10 €
```

Vérification par la formule directe :

```
        2 000 × (250 − 190)     120 000
DPS =  ────────────────────  =  ───────  = 10 €
              12 000             12 000
```

### G.4 — La vérification de la neutralité

| Situation | Calcul | Résultat |
|---|---|---|
| **Actionnaire qui souscrit** — il détient 5 actions et souscrit 1 nouvelle | Avant : 5 × 250 = 1 250 € ; il décaisse 190 €. Après : 6 × 240 = 1 440 € | 1 440 − 190 = **1 250 €** : patrimoine inchangé |
| **Actionnaire qui vend ses droits** — il détient 5 actions | Avant : 1 250 €. Après : 5 × 240 = 1 200 €, plus 5 DPS vendus 10 € = 50 € | 1 200 + 50 = **1 250 €** : patrimoine inchangé |
| **Souscripteur nouveau** — il achète 5 DPS et souscrit 1 action | Il décaisse 5 × 10 + 190 = 240 € et reçoit une action valant 240 € | Opération **équilibrée** |

**La triple vérification est le meilleur contrôle d'un calcul en épreuve** : si les trois situations ne donnent pas un résultat neutre, il y a une erreur.

---

## H. LE DROIT D'ATTRIBUTION

### H.1 — Objet

Il joue dans les **augmentations de capital par incorporation de réserves**, qui donnent lieu à l'attribution d'**actions gratuites** aux actionnaires existants.

**C'est le cas particulier où le prix d'émission est nul.** Aucune ressource nouvelle n'entre dans la société : les réserves sont simplement virées au capital.

### H.2 — Les formules

```
                 N × VA
        VAD =  ──────────
                 N + n

                          n × VA
        DA = VA − VAD =  ─────────
                          N + n
```

### H.3 — Exemple

Reprenons la même société : 10 000 actions valant 250 €, avec attribution de **2 000 actions gratuites** à raison de 5 anciennes pour 1 nouvelle.

```
        10 000 × 250     2 500 000
VAD =  ─────────────  =  ─────────  = 208,33 €
           12 000          12 000

DA = 250 − 208,33 = 41,67 €
```

**Vérification** : l'actionnaire détenant 5 actions possédait 1 250 € ; il détient désormais 6 actions valant 208,33 €, soit **1 250 €**. La richesse est inchangée — l'attribution gratuite ne crée aucune valeur, elle la répartit sur davantage de titres.

---

## I. L'AUGMENTATION MIXTE

Lorsque deux augmentations sont décidées **simultanément** — l'une en numéraire, l'autre par incorporation de réserves —, la valeur ex-droit se calcule **en une seule fois**, en intégrant les deux émissions.

```
                 (N × VA) + (n₁ × PE)
        VAD =  ────────────────────────
                    N + n₁ + n₂
```

où **n₁** est le nombre d'actions de numéraire et **n₂** le nombre d'actions gratuites.

**Les deux droits se calculent ensuite séparément, à partir de cette même valeur ex-droit** : chaque action ancienne porte à la fois un DPS et un droit d'attribution.

> **⚠️ L'erreur classique consiste à calculer les deux opérations l'une après l'autre**, en appliquant la seconde à la valeur issue de la première. Décidées simultanément, elles se calculent ensemble.

---

## J. SOUSCRIPTION IRRÉDUCTIBLE ET RÉDUCTIBLE

| | **À titre irréductible** | **À titre réductible** |
|---|---|---|
| Nature | **Droit garanti**, proportionnel aux titres détenus | **Faculté**, si elle est prévue |
| Étendue | Le nombre d'actions correspondant aux DPS détenus | Au-delà, sur les actions non souscrites à titre irréductible |
| Service des demandes | Intégral | **Réduit proportionnellement** si les demandes excèdent les titres disponibles |

**Si les souscriptions n'absorbent pas la totalité de l'émission** (art. L. 225-134), le conseil peut, dans l'ordre qu'il détermine :

1. **limiter l'émission** au montant des souscriptions reçues, à condition qu'il atteigne au moins les **trois quarts** de l'augmentation décidée ;
2. **répartir librement** tout ou partie des actions non souscrites ;
3. les **offrir au public**, totalement ou partiellement.

---

## K. LES RÈGLES DE LIBÉRATION

| Type d'apport | Libération à la souscription | Solde |
|---|---|---|
| **Numéraire** | **Un quart au moins** de la valeur nominale **et la totalité de la prime d'émission** | Dans les **cinq ans** à compter du jour où l'augmentation est devenue définitive |
| **Nature** | **Intégralement libérés dès l'émission** | — |
| **Mixte** — nominal résultant pour partie d'une incorporation de réserves et pour partie d'espèces | **Intégralement libérées** à la souscription | — |

**Deux délais complémentaires :**

| Délai | Objet |
|---|---|
| **Cinq jours de bourse au minimum** | Durée d'exercice du DPS, à compter de l'ouverture de la souscription |
| **Six mois** | Si l'augmentation n'est pas réalisée dans ce délai à compter de l'ouverture de la souscription, les souscripteurs peuvent obtenir la restitution des fonds |

---

## L. À NE PAS CONFONDRE

**Valeur nominale ≠ prix d'émission ≠ valeur de l'action.** Trois grandeurs distinctes : la première fonde le capital, la deuxième est le prix payé, la troisième la valeur réelle.

**Prime d'émission ≠ prime de remboursement.** La première tient à un prix d'émission supérieur au nominal, la seconde à un remboursement obligataire supérieur au pair.

**Prime d'émission ≠ capital social.** La prime figure en capitaux propres sans entrer dans le capital.

**DPS ≠ droit d'attribution.** Souscription payante contre attribution gratuite ; le second est le cas particulier où le prix d'émission est nul.

**Valeur du DPS ≠ décote.** Le DPS vaut la perte de valeur de l'action, non l'écart entre valeur et prix d'émission.

**Irréductible ≠ réductible.** Droit garanti contre faculté soumise à réduction proportionnelle.

**Renonciation individuelle ≠ suppression du DPS.** La première émane de l'actionnaire, la seconde de l'assemblée générale extraordinaire.

**Un quart du nominal ≠ un quart du prix d'émission.** La fraction libérable ne porte que sur le nominal ; la prime est due intégralement.

---

## M. PIÈGES D'EXAMEN

1. **Utiliser la valeur nominale au lieu de la valeur réelle** de l'action dans le calcul de la valeur ex-droit.
2. **Oublier de pondérer** : la valeur ex-droit est une moyenne pondérée, non une moyenne simple de VA et PE.
3. **Émettre au-dessous du pair** : le prix d'émission ne peut jamais être inférieur à la valeur nominale.
4. **Fractionner la prime d'émission** : elle est due en totalité à la souscription.
5. **Appliquer le quart à la totalité du prix d'émission** au lieu du seul nominal.
6. **Calculer une augmentation mixte en deux temps** au lieu d'un calcul unique.
7. **Confondre le rapport de souscription et le nombre de DPS** : chaque action ancienne porte un DPS, et le rapport indique combien il en faut.
8. **Oublier la vérification de neutralité**, qui détecte la plupart des erreurs.
9. **Croire que l'attribution gratuite enrichit l'actionnaire** : elle répartit la même valeur sur plus de titres.
10. **Oublier le seuil des trois quarts** en cas de souscriptions insuffisantes.
11. **Confondre la suppression du DPS et l'émission réservée** : la seconde suppose la première, mais l'inverse n'est pas vrai.

---

## N. FORMULATIONS TYPES POUR LA COPIE

> « La valeur théorique de l'action après augmentation résulte de la moyenne pondérée des actions anciennes valorisées avant l'opération et des actions nouvelles valorisées au prix d'émission. Le droit préférentiel de souscription a pour valeur théorique la différence entre la valeur de l'action avant l'opération et cette valeur ex-droit. »

> « Aux termes de l'article L. 225-144 du Code de commerce, les actions souscrites en numéraire sont obligatoirement libérées, lors de la souscription, d'un quart au moins de leur valeur nominale et de la totalité de la prime d'émission, le surplus devant être libéré dans le délai de cinq ans à compter du jour où l'augmentation est devenue définitive. »

> « L'actionnaire qui ne souhaite pas souscrire cède son droit préférentiel ; le prix de cession compense exactement la dépréciation de ses titres, de sorte que l'opération demeure neutre pour son patrimoine. »

---

## O. TABLEAU DE SYNTHÈSE

| Question | Réponse |
|---|---|
| Prime d'émission | Prix d'émission − valeur nominale |
| Encadrement du prix d'émission | Entre la valeur nominale et la valeur de l'action |
| Nature de la prime | Capitaux propres, hors capital social |
| Valeur ex-droit | (N × VA + n × PE) ÷ (N + n) |
| Valeur du DPS | VA − VAD, soit n(VA − PE) ÷ (N + n) |
| DPS nul | Lorsque le prix d'émission égale la valeur de l'action |
| Droit d'attribution | n × VA ÷ (N + n) |
| Augmentation mixte | Calcul unique, avec n₁ au prix d'émission et n₂ gratuit |
| Irréductible | Droit garanti, proportionnel |
| Réductible | Faculté, réduction proportionnelle des demandes |
| Souscriptions insuffisantes | Limitation aux trois quarts, répartition libre, ou offre au public |
| Libération du numéraire | Un quart du nominal, **totalité de la prime** |
| Solde | Cinq ans à compter de la réalisation définitive |
| Apports en nature | Intégralement libérés dès l'émission |
| Durée d'exercice du DPS | Cinq jours de bourse au minimum |
| Non-réalisation | Restitution des fonds après six mois |
