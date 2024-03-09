def transform_data(data):
    transformed_data = {}

    for key, value in data.items():
        if isinstance(value, list):
            transformed_data[key] = [transform_post(post) for post in value]
        elif isinstance(value, dict):
            transformed_data[key] = transform_post(value)
        else:
            transformed_data[key] = value

    return transformed_data

def transform_post(post):
    if 'body' in post:
        word_count = len(post['body'].split())
        post['word_count'] = word_count

        if 'userId' in post:
            user_id = post['userId']
            post['user_type'] = "Admin" if user_id == 1 else "Regular User"

    return post

def filter_posts_by_user(posts, user_id):
    return [post for post in posts if post['userId'] == user_id]

def search_posts_by_keyword(posts, keyword):
    return [post for post in posts if keyword.lower() in post.get('body', '').lower()]
