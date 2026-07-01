#!/usr/bin/python3
"""
Recursively counts occurrences of keywords in all hot posts of a subreddit.
"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Parses titles recursively and tallies case-insensitive word matches.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api.advanced.script:v1.0.0 (by /u/pazubuike-dot)"
    }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            words_in_title = title.split()
            for word in words_in_title:
                clean_word = word.strip('.,!_*-=+/&^%$#@~`()[]{}|\\:;"\'<>?')
                if clean_word in counts:
                    counts[clean_word] += 1

        next_page = data.get("after")
        if next_page is not None:
            return count_words(subreddit, word_list, counts, next_page)

        # Sort values descending by count, then alphabetically ascending
        sorted_counts = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))

    except Exception:
        return
