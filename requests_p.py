import requests

# get
url_get = "https://jsonplaceholder.org/posts/1"
response = requests.get(url_get)
if response.status_code == 200:
    print(response.json())
    print(response.json()['title'])
    print(response.json()['id'])

# post
url_post = "https://jsonplaceholder.org/posts"
data = {"title": "test", "content": "test", "userId": 1}
response_post = requests.post(url_post, json=data)
if response_post.status_code == 201:
    print(response_post.json())
