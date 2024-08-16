import requests

def number_of_subscribers(subreddit):
    
    # Set up the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define custom headers with User-Agent
    headers = {'User-Agent': 'custom_user_agent/0.0.1'}
    
    try:
        # Making the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
