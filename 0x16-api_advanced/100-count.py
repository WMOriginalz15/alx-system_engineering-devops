#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    if not word_list or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    children = data.get("data", {}).get("children", [])

    for post in children:
        title = post["data"]["title"].lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title:
                counts[word] = counts.get(word, 0) + title.count(word_lower)

    after = data["data"].get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")


if __name__ == "__main__":
    # Example usage
    subreddit_name = "python"  # Replace with the subreddit you want to query
    words_to_count = ["python", "tutorial", "guide"]  # Replace with words you're interested in
    count_words(subreddit_name, words_to_count)
