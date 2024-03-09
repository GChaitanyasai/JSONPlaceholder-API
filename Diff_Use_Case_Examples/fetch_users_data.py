import requests
import json

def fetch_user_data(user_ids):
    if isinstance(user_ids, int):
        user_ids = [user_ids]  # Converting single ID to a list

    user_data_list = []

    for user_id in user_ids:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            user_data = response.json()
            user_data_list.append(user_data)
        else:
            print(f"Failed to fetch user data for ID {user_id}. Status code: {response.status_code}")

    save_to_file(user_data_list, "users_data.json")  # Saving data to a file
    return user_data_list

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2) 

# Example Usage
user_ids = [1, 2, 3]  # or user_ids = 1 for a single ID
users_data = fetch_user_data(user_ids)
print(f"Users Information: {users_data}")
