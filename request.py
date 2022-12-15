from os import getenv
from re import compile
from dotenv import load_dotenv
from datetime import timedelta
from googleapiclient.discovery import build

load_dotenv()

def get_playlist_time(fv, playlist_id):
    """
    Writes all time values for videos from a youtube playlist
    and returns the total time for the playlist
    """
    fv.write(f"Playlist_id: {playlist_id}\n")

    youtube = build('youtube', 'v3', developerKey= getenv('API_KEY'))

    hours_pattern = compile(r'(\d+)H')
    minutes_pattern = compile(r'(\d+)M')
    seconds_pattern = compile(r'(\d+)S')

    total_seconds = 0

    nextPageToken = None
    nextPage = True
    while nextPage:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken
        )

        pl_response = pl_request.execute()

        vid_ids = []
        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])

        vid_request = youtube.videos().list(
            part="contentDetails",
            id=','.join(vid_ids)
        )

        vid_response = vid_request.execute()

        for item in vid_response['items']:
            duration = item['contentDetails']['duration']

            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            video_seconds = timedelta(
                hours=hours,
                minutes=minutes,
                seconds=seconds
            ).total_seconds()

            fv.write(f"{hours}:{minutes}:{seconds}, {video_seconds}\n")

            total_seconds += video_seconds

        nextPageToken = pl_response.get('nextPageToken')

        if not nextPageToken:
            nextPage = False

    total_seconds = int(total_seconds)

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours}:{minutes}:{seconds}'
