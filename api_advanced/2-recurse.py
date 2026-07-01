#!/usr/bin/python3
"""
Queries the Reddit API recursively to return a list of all hot post titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively pulls all hot article titles for a subreddit.
    Returns None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api.advanced.script:v1.0.0 (by /u/pazubuike-dot)"
    }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])
        
        # Copy elements into an isolated list to avoid persistent mutable defaults issues
        if after is None:
            hot_list = []

        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        next_page = data.get("after")
        if next_page is not None:
            return recurse(subreddit, hot_list, next_page)
        
        return hot_list if len(hot_list) > 0 else None
    except Exception:
        return None
