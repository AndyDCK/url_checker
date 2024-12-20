# URL Checker

URL Checker est un outil simple en Python pour détecter des liens potentiellement suspects ou de phishing. Il analyse une URL et identifie des caractéristiques qui pourraient indiquer un danger pour l'utilisateur.

## Fonctionnalités

- Analyse de la longueur de l'URL.
- Vérification de l'utilisation d'HTTPS.
- Détection de mots-clés suspects dans le domaine.
- Vérification du certificat SSL.

## Installation

### Prérequis

- Python 3.10 ou plus récent.
- Le module `requests`. Installe-le via pip si nécessaire :
  ```bash
  pip install requests
  ```

### Cloner le dépôt

```bash
git clone git@github.com:AndyDCK/url_checker.git
cd url_checker
```

## Utilisation

1. Lancez le script :

   ```bash
   python3 main.py
   ```

2. Entrez l'URL à analyser lorsqu'elle est demandée.

   Exemple d'entrée :
   ```
   Entrez l'URL à vérifier : http://paypal-secure-login.com
   ```

   Exemple de sortie :
   ```
   Analyse de l'URL : http://paypal-secure-login.com
   Domaine : paypal-secure-login.com
   Chemin :
   [ALERTE] Le site n'utilise pas HTTPS.
   [ALERTE] Le domaine contient des mots-clés suspects.
   [INFO] Le site semble être en ligne.
   ```

---

### Auteur

- **AndyDCK**