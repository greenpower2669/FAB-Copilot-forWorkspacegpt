---
name: fab-copilot
description: "Utiliser pendant le développement, le packaging ou les transferts de projets de Fabrice pour garder une autonomie légère, anticiper les risques, appliquer APK/AAB/icône/nommage et passer la main avant les transferts d'assets réellement fragiles."
---

# FAB Copilot — skill légère v0.2

## Intention

Collaborer avec Fabrice, développeur qui apprécie l'autonomie de l'agent **et** les petits débogages partagés. Ne ni lui retirer le contrôle, ni l'interrompre inutilement. Inspiré du principe des skills composables (comme Superpowers), sans rendre obligatoires brainstorming, TDD, sous-agents ou longues checklists à chaque action.

## Boucle de décision (appliquer sans réciter)

1. **Comprendre le résultat souhaité et la cause de chaque règle.** Distinguer objectif stable, préférence actuelle, contournement d'un incident et hypothèse technique.
2. **Observer les capacités du moment** : type d'API (binaire, multipart, JSON Base64), volumes, fiabilité constatée, environnement, branche Git, droits et outillage. Ne pas présumer que Base64, le réseau ou l'API sont la cause démontrée d'un échec.
3. **Choisir la solution proportionnée** : petite action fiable → agir ; grosse opération → chercher voie directe, chunking, compression appropriée ou intervention humaine si elle apporte réellement un gain.
4. **Avant une opération risquée**, proposer un relais **court et actionnable** : ce qui est prêt, ce qui reste local, pourquoi cette voie est risquée, où se trouvent les fichiers, commande ou trois clics pour l'humain, comment reprendre ensuite. Ne pas attendre un échec ou une boucle de reconnexion.
5. **Exécuter, vérifier, laisser une trace** : commit SHA, build, release, lien ou chemin effectivement vérifié ; synchroniser les quatre mémoires du projet **pendant** les modifications, jamais seulement à la fin. Ne jamais attribuer un résultat à un outil qui ne l'a pas confirmé.

**Principes d'arbitrage :** autonomie par défaut ; relais humain contextuel ; aucune règle temporaire éternelle ; aucun arrêt pour un seul petit PNG sans raison concrète ; aucun mensonge de livraison ; pas de promesse de travail en arrière-plan.

## Règle absolue — FAB-MEM-001 : quatre mémoires vivantes

Avant **toute** modification de code, skill, configuration ou architecture, lire `brain.md`, `brainmap.md`, `debughistorical.md` et `todo.md` du dépôt travaillé (les créer/migrer s'ils manquent). Les garder synchronisés en temps réel avec le code, tout au long de l'intervention, **dans le même commit**. Examiner les quatre ; n'éditer que les parties concernées, sans inventer une entrée inutile. En cas d'interruption, laisser immédiatement l'état vrai et le prochain geste dans `todo.md`.

- `brain.md` : contrat fonctionnel détaillé, vérité actuelle et décisions de Fab.
- `brainmap.md` : **cartographie technique complète**, non raccourcie artificiellement : toutes les parties connues, fonctions, dépendances et causes/conséquences, hiérarchisées et navigables.
- `debughistorical.md` : incompréhensions, bugs, régressions, hypothèses vs causes prouvées, correctifs et vérifications.
- `todo.md` : fait, reste, blocages, tests humains/non faits et preuves.

Si une régression survient, vérifier si la carte était incomplète et enrichir la compréhension. Ne jamais attribuer à Fab une supposition de l'agent. Cette règle s'applique **aussi à FAB Copilot**. Protocole : [MEMOIRE-VIVANTE.md](../../docs/MEMOIRE-VIVANTE.md). Contrat : [brain.md](../../brain.md) ; carte : [brainmap.md](../../brainmap.md).

**Livraison :** pour toute version prête à distribuer, publier une GitHub Release vérifiée et fournir sa page et les liens directs vers ses fichiers ; pour Android, APK/AAB distincts selon le besoin, noms projet/version, icône. Ne jamais substituer un ZIP ou un artefact Actions temporaire à un APK. Si la publication est impossible, l'indiquer dans `todo.md` sans annoncer une release inexistante.

## Quand ouvrir les références

- Packaging, PWA/Android, ergonomie, versionnement, release → [conventions.md](references/conventions.md).
- Images, binaires, JSON, Base64, GitHub, quotas, API, interruptions → [transferts.md](references/transferts.md).
- Inventaire facultatif sur machine locale : `python scripts/asset_gate.py ./assets --transport json-base64` (depuis la racine de ce dépôt ou après copie du script). Ce diagnostic ne bloque pas un agent à lui seul.

## Exemple de relais

« La version 1.3 est codée localement ; le commit GitHub n'est pas confirmé. Il reste 27 PNG pour 18 Mio dans le workspace. L'outil disponible impose un JSON/Base64 ; le transfert serait plus volumineux et notre session a eu des interruptions. Je n'ai **pas** lancé l'upload. Tu peux pousser le dossier `assets/` en binaire avec Git depuis ce workspace [commande adaptée à l'environnement], ou me confirmer une API binaire disponible. Ensuite je vérifie le commit et termine la release. »

## Réversibilité

Si l'API suivante accepte directement les PNG binaires, utiliser cette voie et **ne plus déclencher** le contournement lié à JSON/Base64. Si le volume est minuscule, poursuivre même avec Base64. Faire évoluer les seuils avec les résultats réels, sans changer la philosophie.
