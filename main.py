from googleapiclient.discovery import build

# Replace with your API key
API_KEY = "YOUR_YOUTUBE_API_KEY"

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_playlist_videos(playlist_id):
    """Fetch all video IDs from a given playlist."""
    videos = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]
            videos.append(video_id)

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return videos

def add_videos_to_playlist(video_ids, new_playlist_id):
    """Add videos to a specified playlist, avoiding duplicates."""
    existing_videos = get_playlist_videos(new_playlist_id)  # Get current playlist videos

    for video_id in video_ids:
        if video_id not in existing_videos:  # Add only if not already in playlist
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": new_playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id
                        }
                    }
                }
            ).execute()

# Replace with your playlist IDs
source_playlists = ["SOURCE_PLAYLIST_ID_1", "SOURCE_PLAYLIST_ID_2"]
new_playlist_id = "YOUR_NEW_PLAYLIST_ID"

# Fetch videos from source playlists
all_videos = []
for playlist in source_playlists:
    all_videos.extend(get_playlist_videos(playlist))

# Add videos to the new playlist
add_videos_to_playlist(all_videos, new_playlist_id)

print("Videos have been successfully merged!")