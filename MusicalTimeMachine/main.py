from billboard import Billboard
import os
from Spotify_auth import Spotify_auth



def main():
    travel_date = input("Which year do you want to travelto? Type the date in this format YYYY-MM-DD: ")
    billboard = Billboard(travel_date)
    song_names = billboard.get_html()

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    spotify_auth = Spotify_auth(client_id, client_secret, travel_date)
    spotify_auth.create_playlist(song_names)
    

if __name__ == "__main__":
    main()