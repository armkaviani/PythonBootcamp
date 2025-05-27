from billboard import Billboard



def main():
    travel_date = input("Which year do you want to travelto? Type the date in this format YYYY-MM-DD: ")
    billboard = Billboard(travel_date)
    song_names = billboard.get_html()


    

if __name__ == "__main__":
    main()