# TODO — FAB Copilot

## V0.1 — implémenté
- [x] Dépôt indépendant ; pas de fork ni import de Superpowers.
- [x] Skill au format `SKILL.md` avec frontmatter et déclencheurs.
- [x] Manifeste portable `plugin.json` pour empaqueter la skill en plugin installable.
- [x] Motivation et arbitrage contextuel : autonomie, relais humain **avant** les transferts risqués, exceptions légères.
- [x] Conventions : APK + AAB si pertinent, nom du projet/version, icône, architecture PWA/native selon contexte.
- [x] Continuité : préserver stable, `TODO.md` dans chaque dépôt travaillé, vérifier commits et builds.
- [x] Diagnostic local des assets (métadonnées uniquement) et tests unitaires.

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
