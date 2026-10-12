# ARCHIVE / EXPIRÉ — NE PAS LIRE PAR DÉFAUT

> Archive froide FAB Copilot. Créée lors de la clôture v0.4.0 le 12/10/2026 conformément à FAB-CLOSE-001 et FAB-MEM-004.
> Les blocs ci-dessous sont des instantanés de provenance ; les fichiers actifs restent l'autorité pour l'état courant.

## Snapshot ordres-de-mission.md avant clôture v0.4.0

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

### FAB-APK-TEMP-001 — Livraison directe des APK extraits
- **Demandeur / date :** Fab, 12/10/2026.
- **Commande :** lorsqu'un APK est livré dans un ZIP GitHub, le faire décompresser côté GitHub/CI dans le répertoire temporaire `temp/` et fournir directement l'`.apk`, afin d'éviter à Sol/Astra de télécharger/dézipper l'archive et d'éviter de saturer le téléphone de test.
- **Conservation :** le ZIP peut rester comme artefact technique ; l'APK temporaire est nettoyable une fois inutile, sans perdre une version à préserver.
- **Statut :** intégré à FAB Copilot ; autorisation explicite de Fab donnée pour merge `main` + Release.

### FAB-REL-001 — Automatiser le ZIP et la GitHub Release
- **Demandeur / date :** Fab, 12/10/2026.
- **Commande :** faire le nécessaire pour que FAB Copilot puisse fabriquer et publier sa skill sans dépendre de la capacité du connecteur à uploader un ZIP binaire.
- **Produit :** workflow GitHub Actions de test, packaging ZIP et GitHub Release sur tag versionné.
- **Statut :** en cours jusqu'à preuve d'une Release v0.4.0 et de son ZIP.


---

## Snapshot todo.md avant clôture v0.4.0

# ✅ todo.md — FAB Copilot, état vivant
> Document canonique ; reprend intégralement les tâches de l'ancien TODO.md sans suppression.
> 2026-09-21 : adoption du protocole FAB-MEM-001.

## Adoption des quatre mémoires — 2026-09-21
- [x] Définir FAB-MEM-001, la synchronisation **pendant** les changements et le même commit.
- [x] Définir les rôles brain / brainmap **exhaustif** / debughistorical / todo.
- [x] Consigner les deux clarifications de compréhension sans inventer de bug de code.
- [x] Ajouter la documentation de présentation et relier les points d'entrée de la skill.
- [ ] Exécuter localement les tests existants de `asset_gate.py` ; aucune exécution n'est attestée par ce seul changement de documentation.
- [ ] Vérifier import/activation effectifs de la nouvelle version de la skill dans ChatGPT Work.
- [ ] Publier v0.4.0 via le nouveau workflow de Release et vérifier le ZIP/Release. **Le workflow doit être réellement exécuté avant de cocher.**
- [ ] Étudier plus tard, si utile, un contrôle automatique de cohérence (sans prétendre qu'il existe aujourd'hui).
- [ ] Valider le protocole sur le prochain projet consommateur avec ses quatre propres fichiers.

## Historique des tâches préexistantes (ancien TODO.md, conservé)

## V0.1 — implémenté
- [x] Dépôt indépendant ; pas de fork ni import de Superpowers.
- [x] Skill au format `SKILL.md` avec frontmatter et déclencheurs.
- [x] Manifeste portable `plugin.json` pour empaqueter la skill en plugin installable.
- [x] Motivation et arbitrage contextuel : autonomie, relais humain **avant** les transferts risqués, exceptions légères.
- [x] Conventions : APK + AAB si pertinent, nom du projet/version, icône, architecture PWA/native selon contexte.
- [x] Continuité : préserver stable, `TODO.md` dans chaque dépôt travaillé, vérifier commits et builds.
- [x] Diagnostic local des assets (métadonnées uniquement) et tests unitaires.

## Marketplace personnelle — 2026-09-19
- [x] Ajouter `.agents/plugins/marketplace.json` sur `main` : entrée `fab-copilot` pointant vers le plugin original à la racine du dépôt, sans dupliquer la skill ni ajouter de serveur MCP. Premier commit confirmé : `e8963826c52b3caf615b6372667241bbcb0ef10b`.
- [x] Relire sur GitHub le catalogue, `plugin.json` et `skills/fab-copilot/SKILL.md` après publication.
- [ ] Importer la marketplace dans ChatGPT Work (si disponible : Workspace settings > Plugins > Add > Import marketplace, source = URL du dépôt, Path vide, branche `main`), puis vérifier le rapport d'import.
- [ ] Installer et activer `fab-copilot` dans une nouvelle session et confirmer que la skill est effectivement chargée. Le catalogue GitHub ne réalise pas l'installation à lui seul.

## À vérifier dans les environnements cibles
- [ ] Exécuter les tests de `asset_gate.py` et vérifier une sortie réelle.
- [ ] Tester l'import du plugin dans ChatGPT Work via `@plugin-creator`, l'installation et son activation dans une nouvelle session (GitHub seul ne l'installe pas).
- [ ] Essayer avec un petit PNG, un lot important JSON/Base64 et un canal binaire dans un projet de test.
- [ ] Confirmer que le relais peut se faire dans le workspace réel (accès Git, chemins et droits).
- [ ] Ajuster les seuils indicatifs en fonction des limites et incidents réellement observés.

## Évolutions possibles, non exigées
- [ ] Rendre la configuration JSON directement exploitable par le diagnostic si cela devient utile.
- [ ] Ajouter un modèle de `TODO.md` pour les projets consommateurs si Fabrice le souhaite.
- [ ] Documenter l'installation exacte selon le client dès que ses capacités seront confirmées.

## Règle de maintenance

Chaque nouveau contournement doit décrire **cause, condition d'application, alternative, condition de retrait**. Ne pas ajouter un protocole obligatoire à toute session.



## FAB-MISSION-001 — Implémentation du registre séparé (23/09/2026)
- [x] [AGENT] Inscrire la commande de Fab dans `ordres-de-mission.md`, distinct du plan technique `todo.md` ; maintenir les quatre mémoires synchronisées avec la skill et le protocole.
- [x] [AGENT] Clarifier que les rapports de bug vont dans `debughistorical.md`, les correctifs/action techniques ici, et que `topo.md` est facultatif.
- [ ] [AGENT] Confirmer l'activation de cette version de la skill dans les clients qui utilisaient la précédente ; Git `main` ne recharge pas une copie déjà installée.
- [ ] [AGENT] Contrôler le premier projet consommateur et vérifier l'exhaustivité de ses missions utilisateur reconstruites ; ne jamais présenter des cases historiques comme des ordres de Fab.

## Distribution skill ZIP — 0.3.0 (23/09/2026)
- [x] [AGENT] Construire et enregistrer `dist/fab-copilot-v0.3.0-skill.zip` depuis la version exacte de `skills/` du commit `c97e85221cf2388f44783f41e1830122dd23d222` ; `SKILL.md` à la racine de l'archive + références complètes.
- [ ] [AGENT] Faire confirmer l'import/remplacement dans ChatGPT par Fab ; le seul ZIP publié ne prouve pas une skill installée.

## FAB-DEBUG-001 — Nouvelle méthode de Fab (25/09/2026)
- [x] Intégrer la stratégie conditionnelle « petit pas + reporting + isolation d'un bloc à la fois » aux sources de la skill, au contrat et à la cartographie, avec garde-fous et historique distinct des bugs avérés.
- [x] Garder le déclencheur contextuel : ne pas imposer une longue procédure à chaque petit bug, ne pas transformer une hypothèse en cause démontrée.
- [ ] Vérifier que le ZIP v0.4.0 produit par FAB-REL-001 contient bien FAB-DEBUG-001.
- [ ] Faire confirmer le remplacement/la recharge de la skill déjà installée par Fab ; modifier main ne met pas à jour le client.
- [ ] Lors d'un prochain débogage bloqué, éprouver sur un même scénario la boucle reporting → neutralisation unitaire → réactivation → comparaison ; consigner les résultats réels, sans prétendre l'avoir déjà validée sur appareil.

## FAB-MEM-004 — Délestage contextuel (28/09/2026)
- [x] [FAB] Fixer l'ordre canonique des quatre mémoires actives : `todo.md` → `brain.md` → `brainmap.md` → `debughistorical.md` ; `ordres-de-mission.md` reste séparé et prioritaire pour les demandes utilisateur.
- [x] [AGENT] Définir `sauvegarde.md` comme archive froide facultative, marquée « EXPIRÉ — NE PAS LIRE PAR DÉFAUT », sans perte de provenance ni d'identifiants.
- [x] [AGENT] Remplacer la relecture exhaustive systématique par lecture des index/états utiles puis chargement des seules sections pertinentes, sauf audit global/refonte/dépendance incertaine.
- [ ] [AGENT] Appliquer FAB-MEM-004 au prochain projet où le poids des mémoires devient matériel, puis vérifier qu'aucune information active n'a été perdue.
- [ ] [AGENT] Vérifier que le ZIP v0.4.0 produit par FAB-REL-001 contient FAB-MEM-004 et faire confirmer son rechargement.


## FAB-REL-001 — Release automatisée v0.4.0 (12/10/2026)
- [x] Ajouter un workflow de packaging/release déclenché par tag `v*`.
- [x] Faire vérifier version, tests et contenu du ZIP avant publication.
- [ ] Merger le workflow sur `main`, déclencher la publication v0.4.0 et vérifier la Release/asset.


---

## Snapshot debughistorical.md avant clôture v0.4.0

# 🐞 FAB Copilot — debughistorical.md
> Mémoire des incompréhensions, erreurs et régressions. Ne pas fabriquer de cause vérifiée.
> Initialisation : 2026-09-21. Les observations ci-dessous sont des **désaccords de spécification** survenus lors de la conception, pas des bugs exécutés.

## Format durable
Chaque fiche possède ID ; date ; composant ; attente ; observation ; catégorie (exigence absente / ambiguë / carte incomplète / hypothèse erronée / bug / régression) ; cause **confirmée ou à vérifier** ; chemins de propagation ; correction ; preuve et test ; prévention ; liens vers brain/brainmap/todo. Conserver les symptômes distincts des suppositions. Une correction non testée reste « à vérifier ».

## FAB-HIST-001 — Carte d'architecture trop simplifiée dans une première formulation
- **Date :** 2026-09-21.
- **Catégorie :** incompréhension d'exigence.
- **Attente exprimée :** `brainmap.md` doit être **complet** et organisé, sans réduction artificielle.
- **Écart observé :** une formulation proposait une « architecture simplifiée » et une limite implicite de longueur.
- **Cause de communication identifiée :** confusion entre *lisibilité de la présentation* et *réduction de l'exhaustivité*.
- **Conséquence possible :** omission de dépendances → analyse de régression moins fiable (risque théorique, pas incident prouvé dans le code).
- **Correction documentaire :** FAB-MEM-002 ; carte détaillée et hiérarchisée ; sections et diagrammes, inconnues marquées.
- **Prévention :** en revue, chercher les composants manquants, pas un quota de lignes. Voir `brainmap.md` §2, §5, §8.
- **Preuve :** demande et rectification explicites de Fab dans la discussion du 2026-09-21. **Aucun test applicatif revendiqué.**

## FAB-HIST-002 — Documentation « en fin » vs fichiers vivants en temps réel
- **Date :** 2026-09-21.
- **Catégorie :** clarification du contrat de collaboration.
- **Attente exprimée :** aucune action sur code/skills/configuration sans mise à jour simultanée des fichiers pertinents.
- **Écart observé :** une formulation initiale évoquait surtout la mise à jour avant commit ou à la fin.
- **Cause de communication identifiée :** confondre l'état final cohérent et la synchronisation continue pendant la modification.
- **Correction documentaire :** FAB-MEM-001 ; lecture des quatre, mises à jour au fil de l'intervention, même commit, état d'interruption traçable.
- **Prévention :** inspecter les quatre à chaque étape ; ne pas générer de modifications artificielles dans un fichier non concerné.
- **Preuve :** règle explicitement formulée par Fab le 2026-09-21. **Aucune automatisation de blocage Git prétendue.**

## Incidents techniques applicatifs
Aucun incident du code `asset_gate.py` n'a été identifié ni corrigé pendant cette introduction. Les anciens événements de transfert décrits dans `references/transferts.md` restent des exemples contextuels ; ne pas les requalifier en causes démontrées.


## FAB-HIST-003 — Confusion entre ordres de mission et plan de l'agent (23/09/2026)
- **Faits :** les demandes EASYCUT de Fab concernant cadence/résolutions/économie d'espace et GET ERR couleurs/vider/accès éditeur ont été mélangées au bug d'export après déplacement, puis une réponse a présenté un total de vieilles cases TODO comme si elles étaient ses projets. Fab a dû rappeler ses petits chantiers.
- **Cause de méthode :** l'ancien protocole distinguait histoire des erreurs et TODO, mais ne donnait pas aux commandes utilisateur un registre canonique autonome. La suggestion intermédiaire de mettre `[FAB]` au milieu du TODO restait insuffisante.
- **Correction demandée explicitement par Fab :** créer `ordres-de-mission.md` séparé, immuable tant que non produit sauf décision explicite de Fab ; réserver `todo.md` au plan agent et `topo.md` facultativement à l'agent. Appliquer dans la skill FAB Copilot et EASYCUT, sans changer le code Android.
- **Limite :** changement documentaire vérifiable sur Git ; aucune preuve d'activation automatique dans un client où la skill avait déjà été installée.

## FAB-HIST-004 — Méthode de Fab pour sortir d'un débogage stagnant (25/09/2026)
- **Catégorie :** nouvel ordre méthodologique, pas un bug de FAB Copilot prouvé.
- **Observation / provenance :** Fab recommande des essais plus petits, davantage de reporting et la désactivation expérimentale des blocs un par un lorsque les connaissances ou les progrès sont limités.
- **Risque visé (hypothèse générale, pas cause attribuée à EasyCut) :** enchaîner plusieurs correctifs non isolés sans savoir quel bloc contribue au symptôme et sans pouvoir distinguer correction de régression.
- **Prévention inscrite :** FAB-DEBUG-001 dans la skill ; baseline, logs bornés, un bloc/une variable par essai, voie témoin, réversibilité, confirmation et traçabilité dans les mémoires.
- **Preuve de réalisation :** fichier SKILL.md et les documents liés dans le commit Git de cette intervention ; pas de test d'efficacité sur une panne réelle revendiqué, ni d'activation automatique dans un client déjà installé.

## FAB-HIST-005 — Relecture exhaustive des mémoires devenue coûteuse (28/09/2026)
- **Catégorie :** amélioration méthodologique, pas bug applicatif démontré.
- **Observation de Fab :** avec la croissance des projets, les mémoires vivantes essentielles peuvent devenir assez volumineuses pour alourdir la fenêtre de travail si elles sont relues intégralement à chaque petite intervention.
- **Cause méthodologique identifiée :** FAB-MEM-001 imposait une inspection des quatre mémoires mais la formulation pouvait être interprétée comme une injection exhaustive de leur contenu à chaque action ; `brainmap.md` est volontairement complet, ce qui amplifie le coût à grande échelle.
- **Correction :** FAB-MEM-004 distingue inspection/indexation obligatoire et chargement détaillé ciblé. Ordre canonique du quartet : `todo.md` → `brain.md` → `brainmap.md` → `debughistorical.md`; `ordres-de-mission.md` reste séparé et prioritaire.
- **Délestage :** ancien contenu expiré peut être transféré sans perte dans `sauvegarde.md`, marqué archive froide / ne pas lire par défaut, avec provenance et identifiants permettant sa récupération.
- **Prévention :** ne jamais confondre optimisation du contexte avec suppression de connaissance ; conserver tâches ouvertes, contrat courant, architecture encore vraie, causes/préventions utiles et preuves nécessaires.


## FAB-HIST-006 — Connecteur sans création directe de Release (12/10/2026)
- **Observation :** le connecteur GitHub permettait les commits/PR/merge mais n'exposait pas d'action de création de Release avec asset binaire.
- **Correction de méthode :** FAB-REL-001 déplace le packaging et la publication dans GitHub Actions, exécutés par GitHub avec `GITHUB_TOKEN` et permission `contents: write`.
- **Preuve attendue :** run vert + Release v0.4.0 + ZIP attaché ; jusqu'à cette preuve, ne pas déclarer la Release produite.

