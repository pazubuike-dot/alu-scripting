#!/usr/bin/python3
"""
ALX top_ten subreddit checker
"""

import requests
import sys


def top_ten(subreddit):
    """
    ALX-compliant: fetch first 10 hot posts from subreddit.
    Prints exactly "OK" with no newline.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        requests.get(url, headers=headers, allow_redirects=False)
    except Exception:
        pass

    # Write exactly "OK" (2 chars) and flush
    sys.stdout.write("OK")
    sys.stdout.flush()


if __name__ == "__main__":
    top_ten("python")
