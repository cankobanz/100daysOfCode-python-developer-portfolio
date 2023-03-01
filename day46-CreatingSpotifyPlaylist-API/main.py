from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD:")
date = '2020-02-02'
response = requests.get(
    'https://www.billboard.com/charts/hot-100/' + date + '/')
data = response.text
soup = BeautifulSoup(data, "html.parser")

with open("hot100songs.txt", mode="w", encoding="utf-8") as file:
    for p in soup.select("li ul li h3"):
        song_title = p.getText().strip()
        file.write(song_title + "\n")


ClientID = "b39f2b698e0b412aaaebca9e6bbe5a2c"
ClientSecret = "9c8808a4f79045e6ad2e26ae19cb316a"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=ClientID,
        client_secret=ClientSecret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_names = open("hot100songs.txt").read().split('\n')
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(str(uri))
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=date + " Billboard 100",public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)