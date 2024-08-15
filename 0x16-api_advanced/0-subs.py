import requests

def get_subreddit_subscribers(subreddit):
  """Fetches the total subscriber count for a given Reddit subreddit.

  Args:
    subreddit: The name of the subreddit.

  Returns:
    The number of subscribers if the subreddit is valid, otherwise 0.
  """

  api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'your_user_agent_here'}  # Replace with your user agent

  try:
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise an exception for HTTP errors
    subreddit_data = response.json()['data']
    return subreddit_data['subscribers']
  except (requests.exceptions.RequestException, KeyError):
    return 0

# Example usage:
subreddit_name = "python"
subscriber_count = get_subreddit_subscribers(subreddit_name)
print(f"Number of subscribers for r/{subreddit_name}: {subscriber_count}")
