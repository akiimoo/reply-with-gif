import praw
import requests
import time

bot = praw.Reddit(
    client_id = "",
    client_secret = "",
    refresh_token = "",
    user_agent = "Reply with gif bot 1.0",
    redirect_uri = "http://localhost",
)

def searchGif(comment): #look for gif with the comment content
    url = "http://api.giphy.com/v1/gifs/search"
    params = {"q": comment, "api_key": "", "limit": "1"}
    data = requests.request(url=url, params=params, method="GET")
    response = data.json()
    return response["data"][0]["images"]["original"]["url"] #returns exact path to gif

for subreddit in bot.subreddits.default(limit=None):
    for submission in subreddit.hot(limit=30):
        print("Looking in " + submission.title)
        for comment in submission.comments:
            try:
                print(comment.body)
                commentLen = comment.body.split(" ")
                if len(commentLen) < 10:
                    comment.reply(searchGif(comment.body))
                    print(f"Replied to {comment.body}")
                    time.sleep(8 * 60)
                time.sleep(20)
            except Exception:
                pass