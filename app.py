from flask import Flask, render_template
import praw
import random
import requests
import config

app = Flask(__name__)

@app.route("/")
def index():
    # Create a Reddit instance
    reddit = praw.Reddit(client_id=config.CLIENT_ID,
                         client_secret=config.CLIENT_SECRET,
                         user_agent=config.USER_AGENT)

    # Get a random hot post from r/memes
    subreddit = reddit.subreddit('memes')
    hot_posts = subreddit.hot(limit=50)  # Adjust the limit as per your preference

    # Select a random post from the hot posts
    random_post = random.choice(list(hot_posts))

    # Extract the post title and media URL
    post_title = random_post.title
    post_url = random_post.url
    post_type = determine_post_type(post_url)  # Determine the post type (image or video)

    # Fetch a random image of mountains from the Unsplash API
    background_url = fetch_random_mountain_image()

    # Render the template with the post details and background image URL
    return render_template('index.html', title=post_title, url=post_url, post_type=post_type, background_url=background_url)

def determine_post_type(url):
    # Function to determine the post type based on the URL or other relevant information
    # You can implement your own logic here based on the structure of the URL or any other data available
    # Example: Check if the URL ends with an image extension or contains keywords indicating a video

    if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return 'image'
    elif url.endswith(('.mp4', '.avi', '.mov')):
        return 'video'
    else:
        return 'unknown'

def fetch_random_mountain_image():
    # Make an HTTP request to the Unsplash API and retrieve a random image of mountains
    access_key = config.UNSPLASH_ACCESS_KEY
    url = f"https://api.unsplash.com/photos/random?query=mountains&orientation=landscape&client_id={access_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['urls']['regular']
    else:
        # In case of an error or no image found, provide a default fallback image URL
        return "https://example.com/fallback_mountain_image.jpg"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
