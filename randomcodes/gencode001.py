import facebook

# Create a Facebook Graph API client
graph = facebook.GraphAPI(access_token="<access_token>", version="3.1")

# Get the list of friends
friends = graph.get_object(id="me", fields="friends")
friend_ids = [friend["id"] for friend in friends["friends"]["data"]]

# Get the interests of each friend
interests = {}
for friend_id in friend_ids:
    profile = graph.get_object(id=friend_id, fields="interests")
    if "interests" in profile:
        for interest in profile["interests"]["data"]:
            if interest["name"] in interests:
                interests[interest["name"]] += 1
            else:
                interests[interest["name"]] = 1

# Print the interests and their frequency
for interest, count in interests.items():
    print(f"{interest}: {count}")

#This script uses the Facebook Graph API to access the data of your Facebook friends. You will need to obtain an access token, which is a unique string that authenticates you with the API. You can get an access token by following the instructions in the Facebook Graph API documentation.

#To use this script, you will need to replace <access_token> with your own access token. The script will then get the list of your friends, get the interests of each friend, and count the frequency of each interest. Finally, it will print the interests and their frequency.

#Keep in mind that you will need to have the facebook module installed in order to use this script. You can install it using pip: pip install facebook-sdk. You will also need to have a Facebook account and be friends with the people whose interests you want to analyze.
