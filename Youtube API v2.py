# %% 🧠 Imports
import requests
import pandas as pd
from tqdm import tqdm
from datetime import datetime
import isodate

# Your YouTube Data API key
API_KEY = ' Add you API KEY '

# Define brands and their YouTube channel IDs
channels = {
    "Real Madrid": "UCWV3obpZVGgJ3j9FVhEjF2Q",
    "FC Barcelona": "UC14UlmYlSNiQCBe9Eookf_A"
}

# ------------------------
# Function: Get Channel Stats
# ------------------------
def get_channel_stats(channel_id, brand):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        'part': 'snippet,statistics',
        'id': channel_id,
        'key': API_KEY
    }
    response = requests.get(url, params=params).json()

    if 'items' not in response or len(response['items']) == 0:
        print(f"❌ Error fetching channel stats for {brand}")
        return {}

    item = response['items'][0]
    stats = item['statistics']
    snippet = item['snippet']

    return {
        'brand': brand,
        'channel_id': channel_id,
        'channel_title': snippet['title'],
        'published_at': snippet['publishedAt'],
        'subscribers': int(stats.get('subscriberCount', 0)),
        'total_views': int(stats.get('viewCount', 0)),
        'total_videos': int(stats.get('videoCount', 0)),
        'country': snippet.get('country', '')
    }

# ------------------------
# Function: Get Uploads Playlist ID
# ------------------------
def get_uploads_playlist_id(channel_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        'part': 'contentDetails',
        'id': channel_id,
        'key': API_KEY
    }
    response = requests.get(url, params=params).json()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# ------------------------
# Function: Get All Videos from Upload Playlist (no date filter)
# ------------------------
def get_all_videos_from_playlist(playlist_id, brand):
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    video_ids = []
    next_page_token = None

    while True:
        params = {
            'part': 'snippet',
            'playlistId': playlist_id,
            'maxResults': 50,
            'key': API_KEY,
            'pageToken': next_page_token
        }

        response = requests.get(url, params=params).json()
        items = response.get('items', [])

        for item in items:
            video_ids.append(item['snippet']['resourceId']['videoId'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    print(f"✅ Total videos retrieved for {brand}: {len(video_ids)}")
    return video_ids

# ------------------------
# Function: Get Video Stats
# ------------------------
def get_video_stats(video_ids, brand):
    url = "https://www.googleapis.com/youtube/v3/videos"
    all_stats = []

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        params = {
            'part': 'snippet,statistics,contentDetails',
            'id': ",".join(batch),
            'key': API_KEY
        }
        response = requests.get(url, params=params).json()

        for item in response.get('items', []):
            snippet = item['snippet']
            statistics = item.get('statistics', {})
            content_details = item.get('contentDetails', {})

            all_stats.append({
                'brand': brand,
                'video_id': item['id'],
                'title': snippet.get('title', ''),
                'published_at': snippet.get('publishedAt', ''),
                'views': int(statistics.get('viewCount', 0)),
                'likes': int(statistics.get('likeCount', 0)),
                'comments': int(statistics.get('commentCount', 0)),
                'duration': content_details.get('duration', '')
            })

    return all_stats

# ------------------------
# Main Execution
# ------------------------

channel_stats_list = []
video_stats_list = []

for brand, channel_id in tqdm(channels.items(), desc="Processing Channels"):
    print(f"\n🔍 Fetching channel stats for {brand}")
    channel_stats = get_channel_stats(channel_id, brand)
    if channel_stats:
        channel_stats_list.append(channel_stats)

        print(f"📼 Fetching all videos for {brand}")
        playlist_id = get_uploads_playlist_id(channel_id)
        video_ids = get_all_videos_from_playlist(playlist_id, brand)
        videos = get_video_stats(video_ids, brand)
        video_stats_list.extend(videos)

# Save to CSV
channel_df = pd.DataFrame(channel_stats_list)
video_df = pd.DataFrame(video_stats_list)

channel_df.to_csv("youtube_channel_metrics.csv", index=False, encoding='utf-8-sig')
video_df.to_csv("youtube_video_metrics.csv", index=False, encoding='utf-8-sig')

print("\n✅ All channel and video data saved successfully.")

# %%
