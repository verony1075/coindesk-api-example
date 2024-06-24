import requests

def get_latest_story():
    
    response = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty")
    latest_story_id = response.json()[0]


    story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{latest_story_id}.json?print=pretty")
    story = story_response.json()
    if story['type'] == 'story':
        print(f"Title: {story['title']}")
        print(f"Author: {story['by']}")
        print(f"Link: {story['url']}")

get_latest_story()