# Ordres de mission — FAB Copilot

## IMMUTABLE / À PRÉSERVER — FAB-IMMUTABLE-001
- **Identité de la skill/plugin :** `fab-copilot`.
- **Source canonique de version :** `plugin.json`.
- **Source canonique de la skill :** `skills/fab-copilot/SKILL.md` avec `skills/fab-copilot/references/`.
- **Nom de l'archive distribuée :** `fab-copilot-vX.Y.Z-skill.zip`.
- **Workflow de publication :** `.github/workflows/release-skill.yml`.
- **Déclencheur de publication :** `release-version.txt`, qui doit correspondre à `plugin.json`.
- **Secrets :** aucun secret applicatif dans le dépôt ou les mémoires ; la Release utilise uniquement le `GITHUB_TOKEN` éphémère du workflow.
- Toute modification de ces invariants exige l'accord explicite de Fab et un avenant daté.

> Registre canonique des demandes explicites de Fab. Les détails historiques clos avant v0.4.0 sont conservés dans `sauvegarde.md`.

## Règles de conservation et de décision — FAB-MISSION-001
- Une demande explicite de Fab, y compris « pour plus tard », « en todo » et « code pas », devient une mission stable.
- Seul Fab peut annuler, remplacer, fusionner, modifier le périmètre, réordonner ou déprioriser ses missions.
- Une mission nécessitant un essai humain reste **Livré, à valider** jusqu'au retour de Fab.
- Les missions closes quittent la vue active lors d'une clôture propre mais restent dans `sauvegarde.md`.

## Mission active

### FAB-ZIP-002 — FAB Copilot v0.4.0 installable
- **Demandeur / date :** Fab, 12/10/2026.
- **Commande :** intégrer les nouvelles règles, relire l'ensemble, merger et produire une vraie Release avec ZIP installable sans dépendre d'une création manuelle de tag.
- **Produit attendu :** Release GitHub `v0.4.0` ; ZIP `fab-copilot-v0.4.0-skill.zip` vérifié, contenant notamment FAB-DEBUG-001, FAB-MEM-004, FAB-IMMUTABLE-001, FAB-CLOSE-001, FAB-APK-TEMP-001 et FAB-REL-001.
- **Statut :** **Livré, à valider**. Les refs `v0.4.0` et `verified-v0.4.0` sont résolues ; le tag de preuve n'est créé qu'après re-téléchargement du ZIP publié, validation du SHA-256 et contrôle des règles attendues. Reste uniquement la réimportation/validation de la skill par Fab.
