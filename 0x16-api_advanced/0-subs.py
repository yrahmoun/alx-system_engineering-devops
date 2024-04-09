#!/usr/bin/python3
"""module for number_of_subscribers"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json()
    subs = results.get("data").get("subscribers")
    return subs
