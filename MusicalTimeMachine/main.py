from billboard import Billboard
import os



def main():
    travel_date = input("Which year do you want to travelto? Type the date in this format YYYY-MM-DD: ")
    billboard = Billboard(travel_date)
    song_names = billboard.get_html()

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    

if __name__ == "__main__":
    main()