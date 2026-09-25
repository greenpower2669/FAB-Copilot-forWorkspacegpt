# 🧠 FAB Copilot — brain.md
> Contrat fonctionnel vivant · Référence de l'intention, pas inventaire du code.
> Dernière synchronisation : 2026-09-21 · Première adoption du protocole FAB-MEM-001.

## Mission
FAB Copilot aide Fabrice à développer, déboguer, conditionner et livrer ses projets tout en conservant son initiative. La méthode est légère et fondée sur le *pourquoi* des règles. Elle n'ajoute ni serveur MCP obligatoire, ni sous-agents, ni TDD, ni interruption sans motif concret. L'humain conserve les décisions et les validations sur appareil.

## Exigences non négociables

### FAB-MEM-001 — Mémoire vivante sans différé
Tout projet adopté contient `brain.md`, `brainmap.md`, `debughistorical.md`, `todo.md` à sa racine, créés au démarrage ou migrés depuis l'existant sans perte. Tout changement de code, skill, configuration, architecture, comportement, correction ou packaging est accompagné **dans le même cycle de travail et le même commit** des actualisations pertinentes. Examiner les quatre fichiers à chaque intervention ; un fichier non affecté reste inchangé après vérification. Ne jamais prétendre avoir synchronisé sans vérifier la version sur Git. Ne pas programmer une « documentation en fin de projet ». En cas d'interruption, enregistrer immédiatement l'état effectivement atteint, et ne pas annoncer de commit si ce n'est pas confirmé.

### FAB-MEM-002 — Rôle des quatre fichiers
- `brain.md` : vérité fonctionnelle courante, comportements attendus dans les moindres détails, contraintes, critères d'acceptation, décisions de Fab, inconnues explicites ; ne jamais lui attribuer une supposition.
- `brainmap.md` : **cartographie technique complète**, sans plafond de taille : tous les modules et sous-modules, fichiers, classes, fonctions, entrées/sorties, flux, invariants, dépendances, effets de bord et propagations de causes connues. Organisation hiérarchique, sommaire, diagrammes et références croisées ; ne jamais tronquer pour faire « court ». Signaler ce qui reste non vérifié.
- `debughistorical.md` : symptômes, malentendus, bugs, régressions, hypothèses distinctes des causes démontrées, preuves, correctifs, vérification, prévention.
- `todo.md` : état réel fait/en cours/bloqué/à tester, preuves, prochain geste, livraison ; conserver les tâches historiques non terminées lors de la migration.
Toutes les entrées liées utilisent un identifiant stable (`FAB-MEM-001`, etc.) pour naviguer entre les fichiers.

### FAB-MEM-003 — Réparer la compréhension
Devant un écart : comparer observation au contrat ; déterminer si exigence absente/ambiguë, carte incomplète, mauvaise hypothèse, défaut d'implémentation ou régression. Confronter à l'historique. Expliciter et corriger la compréhension avant le code, sans transformer une inférence de l'agent en décision de Fab. Ne pas inventer de cause confirmée. Une régression doit conduire à se demander si la cartographie aurait permis de l'anticiper et à l'enrichir.

### FAB-DEL-001 — Livrer par release vérifiée
Toute version effectivement prête à distribuer est publiée par GitHub Release, avec lien vers la page de release **et liens directs vers les binaires**, pas seulement des archives ZIP ou des artefacts Actions temporaires. Android : APK et AAB distincts quand adaptés au périmètre, nom projet/version, version interne cohérente, icône identifiable. Un build sans test sur téléphone n'est pas « validé sur téléphone ». Si un accès manque, consigner le blocage et ne pas inventer de liens.

### FAB-COL-001 — Autonomie contextualisée
L'agent travaille seul sur les tâches fiables et réversibles, partage le débogage utile, anticipe et passe la main **avant** un transfert volumineux à risque lorsque le canal disponible l'impose. Un petit Base64 n'est pas interdit ; mesurer le cas réel. Pas de déploiement/test prétendu s'il a été confié à l'humain.

## Contrat de modification
Lire les quatre fichiers et les instructions du dépôt ; identifier les exigences et composants touchés ; mettre à jour les mémoires pertinentes en accompagnement de chaque modification ; vérifier les liens, le code, les tests possibles et les états non vérifiés ; livrer code et mémoires dans un commit cohérent ; publier une release si une version livrable est réellement disponible. Voir [protocole détaillé](docs/MEMOIRE-VIVANTE.md).

## Limites honnêtes
La présence des fichiers ne prouve pas qu'une analyse est juste ; preuves et incertitudes doivent être tracées. L'outil facultatif `asset_gate.py` est un conseil local, non un orchestrateur de releases ni un garde-fou de commits.


### FAB-MISSION-001 — Les commandes de Fab sont un registre autonome
Chaque projet utilisant la skill possède à sa racine `ordres-de-mission.md`, **séparé de `todo.md`**. Ce registre conserve les demandes explicites de Fab, tous leurs détails, ID, priorité fixée par Fab, état et preuve jusqu'à livraison. Seul Fab peut annuler, fusionner, remplacer, modifier le périmètre ou reprioriser sa mission. « Code pas » ou « pour plus tard » interdit de démarrer le code, mais n'efface pas la demande. Une demande produite passe en archivage visible après preuve et validation humaine si nécessaire. Le `todo.md` contient uniquement l'exécution/les propositions de l'agent et les actions correctives courtes ; les bugs et hypothèses détaillés restent dans `debughistorical.md`. `topo.md`, facultatif, peut rester une note de navigation de l'agent. À la question « que reste-t-il ? », lire d'abord le registre des missions Fab, pas les anciennes cases historiques.

### FAB-DEBUG-001 — Progression empirique quand un débogage stagne (demande de Fab, 25/09/2026)
Déclencheur : manque de connaissance ou progrès nul/très faible après plusieurs essais, hypothèses indiscernables ou corrections qui déplacent le bug. L'agent revient à une version stable et à un scénario reproductible, augmente les journaux aux limites utiles de chaque bloc, puis neutralise **un seul bloc à la fois**, réversiblement, en comparant à témoin et entrée identiques. L'absence de bug après désactivation désigne un suspect et non une cause démontrée. Réactiver et réduire jusqu'à une relation causale vérifiable ; préserver sécurité, intégrité, originaux et sauvegardes. Aucune suppression définitive d'une fonctionnalité pour masquer l'incident. Éviter les logs volumineux, les secrets et données personnelles. Si les essais n'apportent aucune preuve discriminante, demander l'observation humaine ciblée plutôt que boucler. Archiver les résultats et la certitude dans debughistorical ; dépendances et blocs dans brainmap ; prochain pas dans todo ; contrat dans brain seulement si pertinent. Ce mode est contextuel et ne s'impose pas aux bugs évidents.
**Limite de diffusion :** source Git modifiée ≠ skill déjà installée mise à jour ; l'ancien ZIP v0.3.0 doit être remplacé pour contenir FAB-DEBUG-001.
