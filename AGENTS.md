# FAB Copilot — consignes aux agents

Avant un travail sur ce dépôt ou un projet qui adopte FAB Copilot, lire [la skill](skills/fab-copilot/SKILL.md). Charger uniquement les références pertinentes ; ne pas imposer un protocole lourd à chaque demande.

Raison d'être : autonomie de développement + intervention humaine ciblée, **avant** un transfert coûteux/fragile ; plaisir du débogage partagé sans créer artificiellement des bogues ou des interruptions.

- Le **pourquoi** prime sur les règles littérales ; vérifier les capacités réelles de l'environnement.
- Continuer seul pour les opérations petites, sûres et réversibles ; conserver les versions stables.
- Réserver le relais humain aux cas où il évite un risque réel ou économise substantiellement temps/ressources.
- Si une opération échoue, ne pas boucler aveuglément : inspecter les artefacts/commits déjà réalisés, puis choisir une reprise limitée.
- Ne jamais déclarer un upload, un commit, une APK ou un AAB terminé sans preuve contrôlée.
- **FAB-MEM-001, obligation permanente :** lire et tenir à jour en temps réel les quatre fichiers du dépôt travaillé : `brain.md`, `brainmap.md` (architecture complète, sans réduction artificielle), `debughistorical.md`, `todo.md`. Aucun changement de code, skill ou configuration sans modification documentaire pertinente dans le même cycle et commit. Examiner les quatre ; ne pas écrire dans un fichier non affecté pour la forme. Lors d'une interruption, consigner l'état vrai immédiatement dans `todo.md`.
- Pour les applications : suivre [conventions](skills/fab-copilot/references/conventions.md) ; pour les assets : [transferts](skills/fab-copilot/references/transferts.md).

Pour les détails, lire [le protocole](docs/MEMOIRE-VIVANTE.md) et les quatre fichiers vivants de ce dépôt. Toute version distribuable doit être publiée comme GitHub Release avec liens vérifiés vers les assets directs ; ne jamais remplacer un APK par un ZIP.

Ce document exprime des **préférences de collaboration**, pas une capacité technique d'interrompre les outils ou d'installer automatiquement la skill.
