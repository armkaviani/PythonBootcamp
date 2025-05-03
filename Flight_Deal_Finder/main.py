from Data_Manager import DataManager
from Flight_Search import FlightSearch
import time

def main():
    data_manager = DataManager()
    data_sheet = data_manager.get_data()

    flight_search = FlightSearch()
    flight_search._get_new_token()

    if data_sheet[0]["iataCode"] == "":
        for value in data_sheet:
            value["iataCode"] = flight_search.get_destination(value["city"])
            time.sleep(2)

        print(f"data_sheet:\n {data_sheet}")
    
    data_manager.destination_data = data_sheet
    data_manager.update_data()
    
   


if __name__ == "__main__":
    main()