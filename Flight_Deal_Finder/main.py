from Data_Manager import DataManager
from Flight_Search import FlightSearch

def main():
    data_manager = DataManager()
    data_sheet = data_manager.get_data()

    flight_search = FlightSearch()

    if data_sheet[0]["iataCode"] == "":
        for value in data_sheet:
            value["iataCode"] = flight_search.get_destination(value["city"])
        print(f"data_sheet:\n {data_sheet}")
   


if __name__ == "__main__":
    main()