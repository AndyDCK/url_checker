import requests
from urllib.parse import urlparse

def detect_phishing(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        path = parsed_url.path

        print(f"Analyse de l'URL : {url}")
        print(f"Domaine : {domain}")
        print(f"Chemin : {path}")

        if len(url) > 75:
            print("[ALERTE] URL trop longue, peut-être suspecte")

        if not url.startswith("https"):
            print("[ALERTE] Le site n'utilise pas HTPPS")

        suspicious_keywords = ["secure", "login", "verify", "account", "update"]
        if any(keyword in domain for keyword in suspicious_keywords):
            print("[ALERTE] Le domaine contient des mots-clés suspects")

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print("[INFO] Le site semble être en ligne")
        except requests.exceptions.SSLError:
            print("[ALERTE] Le certificat SSL est invalide ou absent")

    except Exception as e:
        print(f"[ERREUR] Impossible d'analyser l'URL : {e}")

    url_to_check = input("Entrez l'URL à vérifier : ")
    detect_phishing(url_to_check)

def main():
    print("=== Détecteur de phishing ===")
    url_to_check = input("Entrez l'URL à vérifier :")
    detect_phishing(url_to_check)

if __name__ == "__main__":
    main()