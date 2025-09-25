import requests
import sys

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {url} is online")
        else:
            print(f"⚠️ {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"❌ {url} is offline or unreachable")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python monitor.py <url>")
    else:
        check_website(sys.argv[1])
