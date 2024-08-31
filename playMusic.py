import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import json
import os

from dotenv import load_dotenv
load_dotenv()

# Your Spotify Developer credentials
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET =os.environ["CLIENT_SECRET"]
REDIRECT_URI =os.environ["REDIRECT_URI"]
SCOPE = os.environ["SCOPE"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

#play the song 
def play_track(track_id):
    devices = sp.devices()
    if devices['devices']:
        for i, device in enumerate(devices['devices']):
            print(f"{i}: {device['name']} ({device['type']})")
        device_id = devices['devices'][0]['id']  # Use the first available device
        track_uri = f'spotify:track:{track_id}'
        sp.start_playback(device_id=device_id, uris=[track_uri])
        print(f"Playing track: {track_uri}")
    else:
        print("No active device found. Please open Spotify on a device.")

# Search for the track
def search_track(track_name, artist_name=None):
    query = f'track:{track_name}'
    if artist_name:
        query += f' artist:{artist_name}'
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['id'], track['name'], track['artists'][0]['name']
    else:
        return None


# Receiving the data:

dict_str = sys.argv[1]
data=json.loads(dict_str)
track_name=data['track_name']
artist_name=data['artist_name']




track_info = search_track(track_name, artist_name)
if track_info:
    track_id, track_name, artist_name = track_info
    print(f"Track ID: {track_id}")
    print(f"Track Name: {track_name}")
    print(f"Artist: {artist_name}")
    play_track(track_id)
else:
    print("Track not found.")