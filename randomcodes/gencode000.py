import requests
import json

# Get the user's Instagram ID
username = "<username>"
url = f"https://www.instagram.com/{username}/?__a=1"
response = requests.get(url)
data = json.loads(response.text)
user_id = data["graphql"]["user"]["id"]

# Get the user's media
media_url = f"https://www.instagram.com/graphql/query/?query_id=17888483320059182&id={user_id}&first=100"
media_response = requests.get(media_url)
media_data = json.loads(media_response.text)

# Download the photos
for item in media_data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]:
    if item["node"]["__typename"] == "GraphImage":
        photo_url = item["node"]["display_url"]
        photo_response = requests.get(photo_url)
        with open(f"{item['node']['id']}.jpg", "wb") as f:
            f.write(photo_response.content)

print("Done!")

#This script uses the requests library to send HTTP requests to Instagram's API and the json library to parse the responses. It first gets the user's Instagram ID by sending a request to the API and parsing the response. It then gets the user's media (i.e., photos) by sending another request to the API and parsing the response. Finally, it downloads the photos by sending requests to the URLs of the photos and writing the responses to files.

#To use this script, you will need to replace <username> with the username of the Instagram account you want to download photos from. You can also adjust the first parameter in the media URL to specify the number of photos you want to download (e.g., first=50 will download the first 50 photos).

#Keep in mind that Instagram's API has rate limits, so you may need to wait if you try to download too many photos at once. Additionally, you should respect the terms of use and copyright of Instagram's content.
