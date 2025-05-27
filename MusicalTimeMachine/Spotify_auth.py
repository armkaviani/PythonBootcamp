import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify_auth:
    def __init__(self, client_id, client_secret, traveldate):
        self.client_id = client_id
        self.client_secret = client_secret
        self.spotify = self.authenticate()
        self.redirect_uri = "http://example.com"
        self.scope = "playlist-modify-private"
        self.cache_path = "token.txt"
        self.username = "Armaghan"
        self.show_dialog=True
        self.travel_date = traveldate
        

    def authenticate(self):
        spotify = spotipy.Spotify(auth_manager = SpotifyOAuth(
            client_id=self.client_id, 
            client_secret=self.client_secret, 
            redirect_uri=self.redirect_uri, 
            scope=self.scope, 
            cache_path=self.cache_path, 
            username=self.username, 
            show_dialog=self.show_dialog
        )) 

        return spotify

   
