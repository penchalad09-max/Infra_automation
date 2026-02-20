# python/validate_webserver.py
import requests

def validate_webserver(url="http://localhost:8080"):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Web server is running and serving content.")
        else:
            print(f"⚠️ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Validation failed: {e}")

if __name__ == "__main__":
    validate_webserver()
