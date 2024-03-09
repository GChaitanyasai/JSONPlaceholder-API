import requests
import json

def fetch_user_todos(user_ids):
    if isinstance(user_ids, int):
        user_ids = [user_ids]

    all_todos_data = []

    for user_id in user_ids:
        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}&completed=false"
        response = requests.get(url)

        if response.status_code == 200:
            todos_data = response.json()
            all_todos_data.extend(todos_data)
            save_to_file(todos_data, f"user_{user_id}_todos.json")
        else:
            print(f"Failed to fetch todos for User ID {user_id}. Status code: {response.status_code}")

    return all_todos_data

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
# Example Usage
user_ids = [1, 2, 3] 
user_todos = fetch_user_todos(user_ids)
print(f"Incomplete Todos for User IDs {user_ids}: {user_todos}")