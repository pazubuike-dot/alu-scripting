#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api.advanced.script:v1.0.0 (by /u/pazubuike-dot)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get("data", {}).get("children", [])
            if not children:
                print(None)
                return
            for post in children:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
