from reddit_scraper import get_reddit_comments
from llm_text_analysis import get_formatted_response
# Include all keys in keys.py file
from keys import *

def main():
    try:
        # Fetch comments from Reddit based on specified keywords
        comments = get_reddit_comments(KEYWORDS)
        
        # Analyze comments with LLM and get formatted responses
        responses = get_formatted_response(comments)
        
        # Print the top 10 formatted responses
        print(f"Top 10 responses for \"{KEYWORDS}\" in Subreddit \"{SUBREDDIT}\"")
        print(responses)
    except Exception as e:
        print(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()