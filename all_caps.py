import requests
import os
import json

SONGS_FILE = "saved_songs.json"


def main():
    access_token = get_access_token()
    write_saved_songs(access_token)
    print_all_caps_songs()


def write_saved_songs(access_token):
    with open(SONGS_FILE, "w") as songs_file:
        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        saved_songs = {}
        url = "https://api.spotify.com/v1/me/tracks?limit=50"
        while url:
            print(f"Calling {url}")
            resp = requests.get(url=url, headers=headers).json()
            for item in resp['items']:
                saved_songs[item['track']['id']] = (item['track']['name'], item['track']['artists'][0]['name'])

            url = resp['next']

        json.dump(saved_songs, songs_file)

def print_all_caps_songs():
    print("=" * 25)
    print("\n" * 5)
    with open(SONGS_FILE, "r") as songs_file:
        songs = json.load(songs_file)
        for name, artist in songs.values():
            if name.isupper() and not any(char.isdigit() for char in name):
                print(f"{name} - {artist}")

def get_access_token():
    with open("token.json", "r") as token_file:
        return json.load(token_file)['access_token']

if __name__ == "__main__":
    main()