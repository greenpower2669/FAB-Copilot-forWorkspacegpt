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
- [ ] Créer une GitHub Release de la nouvelle version via un canal qui dispose de l'écriture Releases, puis vérifier le lien. **Un commit seul n'est pas une release.**
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

