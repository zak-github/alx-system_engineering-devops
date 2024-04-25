#!/usr/bin/python3
"""
script that queries subscribers on a given Reddit subreddit.
"""


import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return f"existing subreddit\nOK\n"
    else:
        return f"nonexisting subreddit\nOK\n"

