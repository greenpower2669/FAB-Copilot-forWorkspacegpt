# Ordres de mission — FAB Copilot

> **Registre canonique des demandes explicites de Fab.** Ces missions ne sont ni un journal de bugs, ni une liste d'idées de l'agent, ni les détails du plan technique. La skill et la procédure imposent ce registre aux projets qui adoptent FAB Copilot.

## Règles de conservation et de décision — FAB-MISSION-001
- Une demande explicite de Fab, y compris « pour plus tard », « en todo » et « code pas », devient une **mission stable**, à identifier avec ID, formulation fidèle, critères de résultat et statut. « Code pas » suspend l'exécution immédiate, **pas** l'inscription ni la persistance.
- Seul Fab peut annuler, remplacer, fusionner, modifier le périmètre, réordonner ou déprioriser ses missions. Aucune nouvelle panne, urgence technique, proposition de l'agent ou version de code ne modifie silencieusement l'ordre ou le contenu des missions utilisateur.
- La mission reste ouverte tant que son produit demandé n'est pas réellement livré ; si le comportement exige une validation humaine, rester **Livré, à valider** jusqu'au retour de Fab. Un simple commit ou une CI réussie ne vaut pas validation Android.
- Une mission produite reste dans la section **Missions livrées**, datée et reliée à la preuve, et n'est jamais effacée sans consigne explicite de Fab. Révisions ultérieures : ajouter une trace, ne pas réécrire l'histoire.

## Mission ouverte

### FAB-MISSION-001 — Protéger les ordres de mission dans chaque projet
- **Demandeur :** Fab, 23/09/2026.
- **Mission :** mettre à jour le Git FAB Copilot et ses projets consommateurs pour que les commandes de Fab soient consignées dans un **fichier séparé `ordres-de-mission.md`**, distinct du `todo.md` technique. Garder `topo.md` libre comme aide-mémoire de l'agent. Préserver tous les détails demandés, y compris cadence, résolutions, options d'export, journal GET ERR, sans les diluer parmi les bugs.
- **Résultat attendu :** règle intégrée à la skill, protocole et documents du dépôt ; fichier créé et rempli dans EASYCUT à partir des demandes attestées ; aucune modification du code Android.
- **Statut :** **Livré dans Git, activation de la skill dans les clients encore à valider par Fab**. La présence sur `main` ne prouve pas qu'une copie déjà installée s'est rechargée.

## Modèle à copier dans tout nouveau projet

### MISSION-XXX — Titre donné par Fab
- **Demandeur / date / source :** Fab, ...
- **Formulation et détails demandés :** ...
- **Critère « produit » :** ...
- **Statut :** À faire / En cours / Livré, à valider / Validé, produit.
- **Preuve de livraison et décision éventuelle de Fab :** ...
- **Liens :** `brain.md` pour contrat exact ; `todo.md` pour l'exécution technique ; `debughistorical.md` seulement s'il y a un bug.

### FAB-ZIP-001 — ZIP de la skill à réinstaller
- **Demandeur :** Fab, 23/09/2026 : donner le ZIP de la nouvelle skill pour la réinstaller dans ChatGPT.
- **Livraison :** `dist/fab-copilot-v0.3.0-skill.zip` extrait des sources du commit `c97e85221cf2388f44783f41e1830122dd23d222` ; téléchargement : https://github.com/greenpower2669/FAB-Copilot-forWorkspacegpt/raw/refs/heads/main/dist/fab-copilot-v0.3.0-skill.zip.
- **Statut : Livré, à valider dans ChatGPT.** Publication Git ne prouve ni le téléchargement ni l'import de la skill par Fab.

## Mission méthodologique FAB-DEBUG-001 — Petits pas et isolation des bugs
- **Demandeur / date :** Fab, 25/09/2026.
- **Commande :** quand connaissances ou progrès devant un bug sont limités ou presque nuls, avancer par petits pas, augmenter le reporting, désactiver temporairement des blocs un par un afin de localiser le problème. Conserver les acquis et apprendre de chaque essai.
- **Produit demandé :** règle conditionnelle explicite dans la skill FAB Copilot, liée aux quatre mémoires et au diagnostic réversible ; pas un changement du code EasyCut ni une désactivation permanente.
- **Statut :** intégré aux sources Git de FAB Copilot ; activation dans une skill déjà installée et reconditionnement du ZIP à vérifier. La présence dans Git seule ne recharge pas la copie importée.
- **Liens :** `skills/fab-copilot/SKILL.md` ; `brain.md` ; `brainmap.md` ; `todo.md`.
