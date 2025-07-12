import requests

def check_subdomain(domain, subdomains):
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            print(f"[✓] Found: {url} ({response.status_code})")
        except requests.ConnectionError:
            pass

domain = "example.com"
subdomains = ["www", "mail", "ftp", "dev", "test", "staging"]
check_subdomain(domain, subdomains)
