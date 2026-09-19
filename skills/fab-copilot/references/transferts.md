# Transferts et relais humain — avant la zone fragile

## Objectif, pas interdiction

Un transfert d'assets via **API JSON/Base64** peut augmenter les données transportées d'environ 33 % avant l'overhead JSON ; une réponse d'outil très volumineuse ou des retries peuvent aussi peser sur la session. Cela **ne démontre pas** qu'un plantage précis vient du Base64 et ne justifie pas de l'interdire. L'outil GitHub Contents peut lui-même exiger Base64 ; une petite icône est généralement raisonnable.

## Avant d'envoyer

1. Faire un inventaire **métadonnées seulement** : nombre, tailles, formats, emplacement, fichiers déjà présents sur Git, commit/release déjà réalisé.
2. Vérifier **la capacité réelle** du canal (Git push binaire depuis workspace ? multipart ? API JSON Base64 obligatoire ? taille max ? permissions ?). Ne pas imaginer un accès terminal ou une API qui n'existe pas.
3. Décider :
   - petit PNG/quelques fichiers légers et canal fonctionnel → transférer normalement, même en Base64 imposé ;
   - lot volumineux + API binaire directe disponible → utiliser le binaire (ou Git natif), sans relais par principe ;
   - lot volumineux + seul canal JSON/Base64 + interruption/risque/coût avéré → **ne pas démarrer cet upload**, sauvegarder l'état, donner un relais humain concret ;
   - canal inconnu → vérifier avant de décider, ne pas affirmer qu'une autre voie existe.
4. Si relais : fournir chemins et manifeste de **métadonnées**, action à effectuer, critère de reprise et état exact des commits. Aucune chaîne Base64 ni contenu binaire dans les messages de l'agent, sauf nécessité démontrée.

## Heuristiques ajustables, pas limites de plateforme

L'outil facultatif `scripts/asset_gate.py` considère par défaut le transport JSON/Base64 comme « important » au-delà de **256 Kio pour un fichier**, **2 Mio au total**, ou **12 fichiers**. Valeurs **indicatives**, ajustables selon API et incidents ; elles ne sont ni des limites GitHub ni des quotas ChatGPT. Si les capacités réelles ou le coût sont favorables, l'agent peut poursuivre avec justification.

## Après interruption

Ne pas répéter en boucle le transfert. Contrôler HEAD/commit SHA, arbres, fichiers distants, et artefacts présents ; reprendre uniquement les éléments manquants. Si aucune preuve, dire « non vérifié ». Ne jamais présenter un export JSON ou une image encodée comme un **push Git confirmé**.

## Exemple de commande de relais (uniquement si terminal Git disponible)

```bash
git status --short
git add assets/
git commit -m "assets: add generated images"
git push origin <branche-verifiee>
```

Adapter à la branche **effectivement vérifiée** et aux fichiers présents ; la commande n'est pas supposée exécutable depuis un simple téléphone ou depuis une session sans accès à la VM. Ne pas demander de transférer des clés ou tokens dans le chat.
