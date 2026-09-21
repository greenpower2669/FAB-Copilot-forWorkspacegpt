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
