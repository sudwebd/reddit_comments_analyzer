import praw
import logging
from keys import *

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_reddit_comments(keyword, limit=1000):
    logging.info("Initializing Reddit instance with credentials")
    # Initialize the Reddit instance with credentials
    reddit = praw.Reddit(
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

    logging.info(f"Getting subreddit instance for {SUBREDDIT}")
    # Get the subreddit instance
    subreddit = reddit.subreddit(SUBREDDIT)
    
    logging.info(f"Searching for posts with keyword '{keyword}' and limit {limit}")
    # Search for posts in the subreddit using the provided keywords
    posts = subreddit.search(keyword, limit=limit)

    posts_comments = []
    # Iterate through the posts and collect comments
    for post in posts:
        # Replace 'more' comments to get the full list of comments
        post.comments.replace_more(limit=5)
        for comment in post.comments.list():
            # Append the comment body to the list
            posts_comments.append(comment.body)

    logging.info(f"Total comments collected: {len(posts_comments)}")
    # Return the list of comments
    return posts_comments