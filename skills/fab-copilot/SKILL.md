---
name: fab-copilot
description: "Utiliser pendant le développement, le packaging ou les transferts de projets de Fabrice pour garder une autonomie légère, anticiper les risques, appliquer APK/AAB/icône/nommage et passer la main avant les transferts d'assets réellement fragiles."
---

# FAB Copilot — skill légère v0.3

## Intention

Collaborer avec Fabrice, développeur qui apprécie l'autonomie de l'agent **et** les petits débogages partagés. Ne ni lui retirer le contrôle, ni l'interrompre inutilement. Inspiré du principe des skills composables (comme Superpowers), sans rendre obligatoires brainstorming, TDD, sous-agents ou longues checklists à chaque action.

## Boucle de décision (appliquer sans réciter)

1. **Comprendre le résultat souhaité et la cause de chaque règle.** Distinguer objectif stable, préférence actuelle, contournement d'un incident et hypothèse technique.
2. **Observer les capacités du moment** : type d'API (binaire, multipart, JSON Base64), volumes, fiabilité constatée, environnement, branche Git, droits et outillage. Ne pas présumer que Base64, le réseau ou l'API sont la cause démontrée d'un échec.
3. **Choisir la solution proportionnée** : petite action fiable → agir ; grosse opération → chercher voie directe, chunking, compression appropriée ou intervention humaine si elle apporte réellement un gain.
4. **Avant une opération risquée**, proposer un relais **court et actionnable** : ce qui est prêt, ce qui reste local, pourquoi cette voie est risquée, où se trouvent les fichiers, commande ou trois clics pour l'humain, comment reprendre ensuite. Ne pas attendre un échec ou une boucle de reconnexion.
5. **Exécuter, vérifier, laisser une trace** : commit SHA, build, release, lien ou chemin effectivement vérifié ; synchroniser les quatre mémoires et le registre des ordres de mission du projet **pendant** les modifications, jamais seulement à la fin. Ne jamais attribuer un résultat à un outil qui ne l'a pas confirmé.

## FAB-DEBUG-001 — Petits pas, reporting et isolation quand le diagnostic patine

**Déclencheur conditionnel :** lorsque plusieurs tentatives ne produisent presque aucun progrès vérifiable, qu'une cause reste indéterminée, ou que des correctifs successifs déplacent le symptôme. Ne pas imposer ce protocole à un bug trivial déjà expliqué. Ne pas confondre fréquence des essais et compréhension accrue.

1. **Figer la référence et reproduire :** relever version/commit, scénario, entrée et résultat attendu/observé ; préserver les acquis et pouvoir revenir au dernier état stable. Une tentative = une question précise, avec critère qui pourrait infirmer l'hypothèse.
2. **Augmenter le reporting utile avant de réécrire :** instrumenter les frontières des blocs (entrée → sortie, décisions, temps, dimensions/format/horodatage selon le projet, code d'erreur, étape exacte et identifiant de tentative). Collecter seulement les données nécessaires, borner volume/coût, éviter secrets, chemins privés et médias bruts ; ne pas masquer une erreur dans un « OK » trompeur.
3. **Isoler un bloc à la fois :** désactivation temporaire, bypass, mock, drapeau de diagnostic ou comparaison ancien/nouveau parcours ; changer **une seule variable** par essai et garder le même fichier/scénario. Conserver une voie témoin qui fonctionne, si elle existe. Protéger données, sécurité, sauvegardes et intégrité : ne jamais désactiver silencieusement un garde-fou critique ni supprimer la seule copie d'un média.
4. **Comparer et réduire :** si le symptôme disparaît, le bloc est **suspect, pas prouvé coupable** (ses entrées, sorties, timing et interactions peuvent être la vraie cause). Réactiver puis tester l'hypothèse isolée, ou subdiviser le bloc et répéter ; utiliser une recherche dichotomique si plusieurs blocs indépendants le permettent. Ne pas multiplier les modifications « au cas où ».
5. **Consigner la preuve et rétablir :** pour chaque essai, noter état du bloc, paramètres, résultat, interprétation et niveau de certitude ; mettre la cause confirmée ou encore inconnue dans `debughistorical.md`, les chemins/dépendances dans `brainmap.md`, le contrat dans `brain.md` s'il change, et le prochain pas dans `todo.md`. Réactiver les blocs écartés, retirer les traces de diagnostic inutiles et vérifier les non-régressions avant livraison. Si aucun essai ne discrimine les hypothèses, arrêter la boucle et demander l'observation ou le test humain précis qui manque.

**Règle de Fab :** « Si tes connaissances ou tes progrès sont limités ou presque nuls devant un bug, avance par petits pas ; augmente le reporting et n'hésite pas à désactiver les blocs un à un pour découvrir d'où vient le problème. » L'isolation est un diagnostic **réversible**, jamais une suppression définitive de fonctionnalités sans demande de Fab.

**Principes d'arbitrage :** autonomie par défaut ; relais humain contextuel ; aucune règle temporaire éternelle ; aucun arrêt pour un seul petit PNG sans raison concrète ; aucun mensonge de livraison ; pas de promesse de travail en arrière-plan.

## Règle absolue — FAB-MISSION-001 : missions de Fab dans un fichier distinct

**Lire `ordres-de-mission.md` AVANT `todo.md` et préserver chaque commande explicite de Fab, même « pour plus tard » ou « code pas ».** Si ce fichier manque, le créer à la racine du projet et reconstruire les demandes attestées depuis `brain.md` et les anciennes notes, sans inventer une commande.

- `ordres-de-mission.md` = **ce que Fab a demandé**, détail exact, ID stable, ordre/priorité fixé par Fab, état et preuve de résultat. Tant que non produit, ne jamais supprimer, fusionner, réinterpréter, réordonner, déprioriser ou déclarer obsolète sans accord explicite de Fab. Une mission produite est archivée de manière visible avec sa preuve, et un test humain attendu laisse le statut « Livré, à valider ».
- `todo.md` = **ton exécution** : prochaines étapes techniques, sous-tâches, tests, blocages, propositions `[AGENT]` et courtes actions `[BUG]`. Ce fichier peut évoluer avec les investigations **sans effacer une mission utilisateur**.
- `debughistorical.md` = récit de bugs, témoignages, hypothèses, causes vérifiées et régressions. Un bug signalé ne devient pas automatiquement une nouvelle mission de fonctionnalité ; si Fab ordonne sa correction, relier alors son ordre dans `ordres-de-mission.md` à l'ID du bug.
- `brain.md` garde le contrat complet. `brainmap.md` garde l'architecture. `topo.md`, s'il existe, est un aide-mémoire **facultatif de l'agent**, jamais un substitut au carnet de Fab.

« Code pas » interdit l'exécution de code dans ce tour mais **ne retire pas la mission**. Quand Fab demande « que reste-t-il ? », commencer par `ordres-de-mission.md` (missions non produites), puis distinguer le plan technique et les bugs. Ne jamais lui donner le total de vieilles cases `todo.md` comme un total de ses projets.

## Règle absolue — FAB-MEM-001 : quatre mémoires vivantes

Avant **toute** modification de code, skill, configuration ou architecture, lire d'abord `ordres-de-mission.md`, puis `brain.md`, `brainmap.md`, `debughistorical.md` et `todo.md` du dépôt travaillé (les créer/migrer s'ils manquent). Les garder synchronisés en temps réel avec le code, tout au long de l'intervention, **dans le même commit**. Examiner les quatre ; n'éditer que les parties concernées, sans inventer une entrée inutile. En cas d'interruption, laisser immédiatement l'état vrai et le prochain geste dans `todo.md`.

- `brain.md` : contrat fonctionnel détaillé, vérité actuelle et décisions de Fab.
- `brainmap.md` : **cartographie technique complète**, non raccourcie artificiellement : toutes les parties connues, fonctions, dépendances et causes/conséquences, hiérarchisées et navigables.
- `debughistorical.md` : incompréhensions, bugs, régressions, hypothèses vs causes prouvées, correctifs et vérifications.
- `todo.md` : plan de réalisation technique, fait, reste, blocages, tests humains/non faits et preuves, sans confusion avec les commandes de Fab.

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
