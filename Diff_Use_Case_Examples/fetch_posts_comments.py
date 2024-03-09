import requests
import json

def fetch_post_comments(post_ids):
    if isinstance(post_ids, int):
        post_ids = [post_ids]

    all_comments_data = []

    for post_id in post_ids:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
        response = requests.get(url)

        if response.status_code == 200:
            comments_data = response.json()
            all_comments_data.extend(comments_data)
            save_to_file(comments_data, f"post_{post_id}_comments.json")
        else:
            print(f"Failed to fetch comments for Post ID {post_id}. Status code: {response.status_code}")

    return all_comments_data

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

# Example Usage
post_ids = [1, 2, 3] 
comments_data = fetch_post_comments(post_ids)
print(f"Comments for Post IDs {post_ids}: {comments_data}")