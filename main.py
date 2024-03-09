import json
from api_interaction import fetch_data
from data_storage import save_to_file, append_to_file, load_from_file
from data_manipulation import transform_data, transform_post, filter_posts_by_user, search_posts_by_keyword

def fetch_and_store(endpoint):
    data = fetch_data(endpoint)
    print(f"{endpoint.capitalize()} Data:")
    print(json.dumps(data, indent=2))  # Formating using JSON.dumps

    # Save data to a separate file with human-readable formatting
    save_to_file(data, f"{endpoint}_data.json")

    return data

def main():
    # Fetch and store users data
    users_data = fetch_and_store("users")

    # Fetch and store posts data
    posts_data = fetch_and_store("posts")

    # Fetch and store photos data
    photos_data = fetch_and_store("photos")

    # Fetch and store comments data
    comments_data = fetch_and_store("comments")

    # Combine data from different endpoints
    combined_data = {
        "users": users_data,
        "posts": posts_data,
        "photos": photos_data,
        "comments": comments_data,
    }

    # Transform and display combined data
    transformed_data = transform_data(combined_data)
    print("Transformed Data:")
    print(json.dumps(transformed_data, indent=2))  

    # Save transformed data to a separate file with human-readable formatting
    save_to_file(transformed_data, "transformed_data.json")

    # Append transformed data to the original data file with indentation
    append_to_file(transformed_data, "all_data.json")

    # Display the original and transformed data from the combined file
    loaded_data = load_from_file("all_data.json")
    print("Loaded Data:")
    print(json.dumps(loaded_data, indent=2)) 

    # Filter posts and display
    filtered_posts = filter_posts_by_user(transformed_data["posts"], 1)
    print("Filtered Posts:")
    print(json.dumps(filtered_posts, indent=2)) 

    # Search posts by keyword and display
    keyword_search_result = search_posts_by_keyword(transformed_data["posts"], "sunt")
    print("Keyword Search Result:")
    print(json.dumps(keyword_search_result, indent=2))  

if __name__ == "__main__":
    main()
