#!/usr/bin/python3

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        results = response.json().get("data")
        if results is None:
            print("None")
            return

        posts = results.get("children", [])
        if not posts:
            print("None")
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
            else:
                print("None")
    except requests.RequestException as e:
        print("None")
