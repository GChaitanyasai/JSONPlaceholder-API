import requests

def fetch_data(endpoint):
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None
