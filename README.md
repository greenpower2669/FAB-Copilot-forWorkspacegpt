# FAB Copilot — collaboration légère (v0.3)

Un **profil de développement pour agents** inspiré du format de skills utilisé notamment par [Superpowers](https://github.com/obra/superpowers), mais **sans sa chaîne de procédures obligatoire**.

## Pourquoi

Fabrice aime déléguer le codage et partager le débogage. L'agent doit conserver son initiative, sans fabriquer des étapes inutiles, tout en sachant **passer la main avant** une opération manifestement plus facile ou fiable à faire par l'humain. Exemple historique : envoyer beaucoup de PNG via une API JSON qui impose le Base64 peut gonfler les transferts et compliquer une reprise. **Ce n'est pas une interdiction du Base64** : si le transfert est petit, ou si une autre API transporte le binaire, la décision change.

> Règle fondamentale : comprendre *pourquoi* une règle existe, vérifier si elle s'applique au contexte réel, puis choisir la stratégie la plus simple et vérifiable.

## 📜 Les ordres de Fab ne se perdent pas

[**ordres-de-mission.md**](ordres-de-mission.md) est le registre canonique des commandes explicites de Fab dans ce dépôt et, par la skill, dans tout projet consommateur. Une demande de fonctionnalité (« pour plus tard », « en todo », « code pas » compris) y reste intacte jusqu'à production, avec statut et preuve. `todo.md` contient le plan technique de l'agent, `debughistorical.md` les bugs ; `topo.md` est facultatif et peut rester à l'agent. Voir FAB-MISSION-001 dans la skill.

## 🧠 Une mémoire réellement vivante

> **Pas de code sans mise à jour des mémoires pendant le même travail et dans le même commit.**

| Fichier vivant | Rôle |
| --- | --- |
| [brain.md](brain.md) | Fonctionnement voulu, précis et vérifiable |
| [brainmap.md](brainmap.md) | Architecture **complète**, exhaustive et hiérarchisée |
| [debughistorical.md](debughistorical.md) | Bugs, régressions et incompréhensions, avec preuves |
| [todo.md](todo.md) | Plan technique de l'agent, blocages et tests ; distinct des ordres de Fab |

📘 [Lire la présentation et le protocole illustré](docs/MEMOIRE-VIVANTE.md).

## Fichiers

- [Skill](skills/fab-copilot/SKILL.md) : activation et boucle décisionnelle.
- [Conventions](skills/fab-copilot/references/conventions.md) : nommage, APK/AAB, icônes, architecture, stabilité, accessibilité.
- [Transferts](skills/fab-copilot/references/transferts.md) : choix de transport et relais humain **avant** upload risqué.
- [AGENTS.md](AGENTS.md) : point d'entrée pour assistants lisant les consignes du dépôt.
- [Configuration exemple](fab-copilot.example.json) : préférences et seuils ajustables, jamais une vérité absolue.
- [Asset Gate](scripts/asset_gate.py) : diagnostic local facultatif, sans charger les octets des fichiers.
- [Tests](tests/test_asset_gate.py) et [todo](todo.md).

## Utilisation

**Le dépôt est désormais empaqueté en plugin de skills via [plugin.json](plugin.json), mais GitHub ne l'installe pas à lui seul dans ChatGPT Work.** Il faut l'importer ou le référencer via le flux de création/installation de plugin de l'environnement. Dans un agent compatible avec les dossiers de skills, référencer ou installer `skills/fab-copilot/` selon sa documentation. Sinon, faire lire `skills/fab-copilot/SKILL.md` à l'agent au début du travail. Si l'agent lit `AGENTS.md`, ce fichier lui sert de porte d'entrée.

Diagnostic facultatif, local et sans upload :

```bash
python scripts/asset_gate.py ./assets --transport json-base64
python -m unittest discover -s tests -v
```

Le diagnostic émet seulement chemins, nombres et tailles : ni image, ni contenu, ni chaîne Base64.

## 📦 Livraisons

Chaque version prête à distribuer passe par une GitHub Release vérifiée, avec lien de release et liens directs des assets utiles ; Android : APK/AAB distincts si adaptés, nom du projet, version et icône. Ne pas promettre une release quand les droits ou les binaires manquent.

## Évolution

Motivations stables ; règles conditionnelles et seuils contextuels. Les mesures temporaires se retirent dès que leur cause ne s'applique plus. Aucune annonce de livraison sans preuve de commit/release et de builds réellement disponibles.

Licence MIT pour le code original ici. Superpowers est distinct, cité comme inspiration, pas embarqué.

## ZIP de réinstallation — 0.3.0

[**Télécharger la skill prête à importer**](https://github.com/greenpower2669/FAB-Copilot-forWorkspacegpt/raw/refs/heads/main/dist/fab-copilot-v0.3.0-skill.zip) : `SKILL.md` à la racine du ZIP, avec `references/`. Dans ChatGPT, réimporter la skill depuis le ZIP pour remplacer l'ancienne copie ; une mise à jour du dépôt Git seule ne met pas nécessairement à jour une skill déjà installée.
