# JSONPlaceholder API Project

This project is designed to interact with the JSONPlaceholder API, retrieving data from various endpoints and showcasing capabilities in data manipulation, storage, and advanced retrieval. The primary objectives include creating a user-friendly console display of the retrieved data and implementing basic data storage functionality without the need for a full-fledged database. Additionally, the project focuses on enhanced data manipulation, introducing innovative transformations and implementing functions for complex data queries.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation and Execution](#installation-and-execution)
- [Usage](#usage)
  - [Data Transformations](#data-transformations)
  - [Advanced Data Queries](#advanced-data-queries)
- [License](#license)

# Introduction

This project is a demonstration of interacting with the JSONPlaceholder API, a mock API providing various endpoints simulating blog-related data. The main focus is on creating a user-friendly console display, storing retrieved data locally, and implementing advanced data manipulation and querying functionalities.

# Features

- Interact with the JSONPlaceholder API.
- Display retrieved data in a user-friendly format in the console.
- Simulate basic data storage locally without a full-fledged database.
- Implement advanced data transformations.
- Perform complex data queries such as filtering, searching, and identification of top engaging posts.

# Project Structure

JSONPlaceholder-API-Project/
│

├── api_interaction.py

├── data_manipulation.py

├── data_storage.py

├── main.py

├── README.md

├── Diff_Use_Case_Examples/

├── fetch_users_data

├── fetch_user_todos

├── fetch_posts_comments

└── ...

# Introduction
This project is a demonstration of interacting with the JSONPlaceholder API, a mock API providing various endpoints simulating blog-related data. The main focus is on creating a user-friendly console display, storing retrieved data locally, and implementing advanced data manipulation and querying functionalities.

# Features
Interact with the JSONPlaceholder API.
Display retrieved data in a user-friendly format in the console.
Simulate basic data storage locally without a full-fledged database.
Implement advanced data transformations.
Perform complex data queries such as filtering, searching, and identification of top engaging posts.
# Getting Started
# Prerequisites
- IDE - VisualStudio Code(we can use any IDE of your choice).

- Python 3.x.

- PIP

- Git Bash or Powershell

# Installation and Execution

```bash
# Installing Requests library using pip
pip install requests
```

```bash
# Clone the repository
git clone https://github.com/GChaitanyasai/JSONPlaceholder-API.git
```

```bash
# Move into the project directory
cd JSONPlaceholder-API
```

```bash
# Executing the Project
python main.py
```

For executing different use case examples:
```bash
# Move into the project directory
cd Diff_Use_Case_Examples

# Executing the Scripts
# To fetch information about a specific user(s) and their associated posts
python fetch_users_data.py

# To retrieve comments associated with a specific post
python fetch_user_todos.py

# To retrieve a list of incomplete tasks (todos) for a specific user(s)
python fetch_posts_comments.py
```

# Usage
## Data Transformations
The project includes functions for meaningful data transformations, categorizing posts, calculating average engagement metrics, and other innovative transformations. Transformed data is stored in a manner that distinguishes it from the original data.

## Advanced Data Queries
Functions for complex data queries are implemented, including filtering for specific user characteristics, searching for keywords within posts, and identifying the top engaging posts.

## License
This project is licensed under the MIT License.
