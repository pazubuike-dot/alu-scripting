#!/usr/bin/python3
"""
Queries the Reddit API to return the total number of subscribers for a sub.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns total subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api.advanced.script:v1.0.0 (by /u/pazubuike-dot)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        return 0
    except Exception:
        return 0
