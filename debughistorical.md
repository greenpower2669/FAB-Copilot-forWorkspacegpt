# 🐞 FAB Copilot — debughistorical.md
> Mémoire active des incidents encore utiles. Historique complet antérieur à la clôture v0.4.0 : `sauvegarde.md`.

## FAB-HIST-006 — Création directe de Release indisponible via le connecteur
- **Date :** 12/10/2026.
- **Observation :** le connecteur GitHub utilisé dans la conversation permet commits/PR/merge mais n'expose ni création de tag ni création de Release avec asset binaire.
- **Cause de blocage :** capacité absente du connecteur, pas défaut de la skill.
- **Correction :** FAB-REL-001 utilise désormais un fichier Git `release-version.txt` comme déclencheur. Sur `main`, GitHub Actions teste, package, crée le tag via `gh release create` et publie le ZIP.
- **Anti-régression :** ne pas revenir à un workflow qui exige que l'agent crée lui-même un tag avant que GitHub Actions puisse démarrer.
- **État :** correction codée ; validation finale = workflow vert + Release v0.4.0 + ZIP vérifié.
