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

## Mission méthodologique FAB-MEM-004 — Délestage contextuel des mémoires
- **Demandeur / date :** Fab, 28/09/2026.
- **Commande :** préserver les mémoires essentielles tout en évitant qu'elles remplissent inutilement le contexte de travail. Dans le quartet actif, utiliser toujours l'ordre `todo.md` → `brain.md` → `brainmap.md` → `debughistorical.md`. `ordres-de-mission.md` reste séparé.
- **Règle de conservation :** rien n'est détruit pour gagner de la place. Les blocs anciens/expirés peuvent être transférés dans `sauvegarde.md`, archive froide marquée « EXPIRÉ — NE PAS LIRE PAR DÉFAUT », avec provenance et identifiants.
- **Règle de lecture :** lire l'état/index des mémoires puis seulement les sections pertinentes ; lecture exhaustive pour audit global, refonte transversale ou dépendance incertaine.
- **Critère produit :** méthode inscrite dans la source FAB Copilot et dans ses quatre mémoires ; application concrète à un projet consommateur seulement lorsque Fab choisit de la lancer.
- **Statut :** **intégré dans les sources Git par cette intervention ; reconditionnement/rechargement de la skill encore à faire si l'on veut l'utiliser depuis une copie déjà installée.**


## Mission méthodologique FAB-IMMUTABLE-001 / FAB-ANDROID-SIGN-001 / FAB-CLOSE-001 — invariants, signature et clôture propre
- **Demandeur / date :** Fab, 12/10/2026.
- **Commande :** généraliser dans FAB Copilot le protocole validé sur GeckoDoku : section IMMUTABLE dans `ordres-de-mission.md`, package/application ID et noms contractuels protégés, procédure de signature Android/Google Play reproductible sans exposer les secrets, et nettoyage/archivage des mémoires lors d'un merge `main` + Release.
- **Secrets :** ne mémoriser que les noms/rôles canoniques ; jamais les valeurs. `ANDROID_UPLOAD_KEYSTORE_BASE64` représente la sauvegarde chiffrée du keystore selon la procédure du projet ; le `.pem` reste un certificat public.
- **Clôture :** les cinq fichiers actifs doivent refléter la version réellement livrée ; le vieux détail utile est déplacé vers `sauvegarde.md`, avec pointeurs courts depuis l'actif lorsque nécessaire.
- **Statut :** intégré sur branche dédiée FAB Copilot ; merge `main` et reconditionnement de la skill non effectués sans ordre explicite de Fab.