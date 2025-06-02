import requests
from bs4 import BeautifulSoup

class Billboard:
    def __init__(self, traveldate):
        self.url = "https://www.billboard.com/charts/hot-100/" + traveldate
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

    def get_html(self):
        response = requests.get(self.url, headers=self.header)


        soup = BeautifulSoup(response.text, "html.parser")
        all_songs = soup.select("li ul li h3")
        song_names = [song.getText().strip() for song in all_songs]
        print(song_names)

        return song_names