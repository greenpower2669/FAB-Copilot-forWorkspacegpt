# Conventions de développement — motivations et adaptations

## Collaboration

- **Pourquoi** : Fabrice reste un programmeur actif, aime inspecter et déboguer avec l'agent. L'agent code de façon autonome lorsqu'il y est invité ; il partage des éléments reproductibles quand l'analyse humaine a de la valeur. Ne pas ajouter des validations inutiles, des sous-agents forcés ni des bogues artificiels.
- Anticiper les problèmes plausibles (API, poids d'assets, limite de session, dépendances, sauvegarde, sécurité, autonomie du téléphone) sans transformer chaque intuition en certitude.
- Garder lisibles les retours, privilégier les indications textuelles et vocales lorsque cela sert l'accessibilité ; éviter les interfaces qui reposent uniquement sur la couleur.

## Application Web / Android

- **Pourquoi** : faciliter test, diffusion et mise à jour. Pour un projet Android qui s'y prête, produire **APK + AAB** ; ce sont deux artefacts distincts, jamais « une APK AAB ».
- Nommer les fichiers avec **nom réel du projet + version** (p. ex. `SpaceFortress-v1.3.apk` et `SpaceFortress-v1.3.aab`), plutôt qu'un nom générique. Maintenir une version cohérente dans l'app et les artefacts.
- Prévoir une **icône cohérente, sympathique et identifiable** ; une petite icône peut passer par Base64 si l'API le demande, sans déclencher un relais inutile. Ne pas présenter une icône temporaire comme définitive.
- Si faisable, préférer **noyau commun Web/PWA + Android** pour réduire la duplication. Vérifier les contraintes concrètes de performance, accès natif, C++/JNI/NDK, confidentialité, vidéo/caméra et expérience utilisateur. Ne pas imposer un noyau commun si l'architecture native est plus pertinente.
- Si la demande porte sur un prototype ou un APK uniquement, suivre le périmètre demandé ; ne pas fabriquer un AAB ou une Web App non souhaités juste pour cocher une case.
- Ne pas annoncer APK, AAB, icône, GitHub release ou tests comme prêts avant validation des fichiers, de leurs chemins et des résultats des builds. Une erreur de build doit être rapportée.

## Synchronisation continue — FAB-MEM-001

Les quatre fichiers `brain.md`, `brainmap.md` (**complète, hiérarchisée, sans limite de taille arbitraire**), `debughistorical.md` et `todo.md` vivent pendant **chaque** action sur code, skill ou configuration ; un même commit doit contenir l'implémentation et ses mises à jour documentaires pertinentes. Lire tous les quatre ; ne modifier que ceux réellement touchés. Une interruption se consigne immédiatement, sans remettre les mémoires à plus tard. Voir `../../../docs/MEMOIRE-VIVANTE.md`.

## Git et continuité

- **Pourquoi** : les interruptions de sessions ne doivent pas effacer l'avancement. Vérifier branche, commit HEAD, fichiers modifiés et dernier état stable avant d'écrire.
- Petites étapes vérifiables ; ne pas écraser une version stable sans justification ni faire de force push par réflexe.
- Si tout n'est pas fait en une session, mettre à jour le `todo.md` **du dépôt travaillé** avec : fait / reste / blocages / dernier commit vérifié / prochain test. Le `todo.md` de FAB Copilot suit seulement l'évolution de cette skill.
- Éviter de recommencer des uploads ou builds sans avoir vérifié ce qui a réellement abouti.

## Distribution vérifiée

Une version prête à partager doit être publiée par GitHub Release et accompagnée des liens directs vers ses binaires, notamment APK et AAB adaptés au périmètre, plutôt que d'un ZIP intermédiaire ou d'artefacts Actions temporaires. Si le canal de publication manque, noter le blocage dans `todo.md` et ne pas prétendre que la release existe.

## Règles durables et mesures temporaires

Toujours conserver la raison de la règle. Par exemple « éviter les gros Base64 via JSON » n'est pertinent que si l'API **impose** ce transport et si le volume/risque le justifie. Documenter temporairement les incidents, réévaluer les seuils et retirer les contournements devenus inutiles.
