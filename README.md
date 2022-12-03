# all-caps

Script used to print songs that are all caps from your spotify liked songs

## How to run locally

install requirements
`pip install -r requirements.txt`

Get temporary oauth token. Spotify has a node app set up to get an oauth token for you https://github.com/spotify/web-api-auth-examples
[How to get an oauth token](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/)
export ACCESS_TOKEN="{YOUR_ACCESS_TOKEN}"

python all_caps.py

