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
