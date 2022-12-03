import requests
import os

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
URL = "https://api.spotify.com/v1/me/tracks"


def main():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    resp = requests.get(url=URL, headers=headers)
    print(requests.post(endpoint, data=data, headers=headers).json())


if __name__ == "__main__":
    main()