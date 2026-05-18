import random
import requests

def fetch_random_dog():
    print("📡 Sending request to the Dog API...")
    
    url = "https://dog.ceo/api/breeds/image/random"
    
    try:
        # Fire off the GET request
        response = requests.get(url, timeout=5)
        
        # Check if the HTTP status code is 200 (OK)
        response.raise_for_status()
        
        # Parse the JSON response body
        data = response.json()
        
        print("\n✅ Success! Response Received:")
        print(f"Status Code: {response.status_code}")
        print(f"Random Dog Image URL: {data['message']}")
        print(f"API Status: {data['status']}")
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request failed! Error: {e}")

if __name__ == "__main__":
    fetch_random_dog()