# Reddit API Project

This project includes Python scripts that interact with the Reddit API to perform various tasks. Each script is designed to fulfill specific requirements related to querying information from Reddit subreddits.

## Project Structure

- **0-subs.py**: Retrieves the number of subscribers for a given subreddit.
- **1-top_ten.py**: Prints the titles of the first 10 hot posts for a given subreddit.
- **2-recurse.py**: Implements a recursive function to retrieve titles of all hot articles for a given subreddit.

## Requirements

- **Python Version**: 3.4.3
- **Libraries**: Requests module for sending HTTP requests to the Reddit API.

## How to Use

1. **Number of Subscribers (Task 0)**
   - Run `0-main.py` and pass the subreddit as a command-line argument:
     ```bash
     python3 0-main.py programming
     ```

2. **Top Ten Hot Posts (Task 1)**
   - Run `1-main.py` and pass the subreddit as a command-line argument:
     ```bash
     python3 1-main.py programming
     ```

3. **Recursive Query for Hot Articles (Task 2)**
   - Run `2-main.py` and pass the subreddit as a command-line argument:
     ```bash
     python3 2-main.py programming
     ```

## Important Notes

- Ensure you have the `requests` library installed.
- Use the provided scripts responsibly, and respect the Reddit API usage policies.

## Author

- [Your Name]

Feel free to modify this `README.md` file based on your preferences and additional information you'd like to provide about the project.
