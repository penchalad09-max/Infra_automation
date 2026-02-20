# python/validate_webserver.py
import requests

def check_webserver():
    try:
        response = requests.get("http://localhost:8080")
        return response.status_code == 200 and "Hello from Ansible!" in response.text
    except Exception:
        return False

if __name__ == "__main__":
    if check_webserver():
        print("✅ Web server is running and serving content.")
    else:
        print("❌ Web server validation failed.")
