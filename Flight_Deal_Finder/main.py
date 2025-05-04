from Data_Manager import DataManager
from Flight_Search import FlightSearch
from Flight_Data import FlightData
import time
from datetime import datetime, timedelta
def main():
    data_manager = DataManager()
    data_sheet = data_manager.get_data()

    flight_search = FlightSearch()
    flight_search._get_new_token()

    flight_data = FlightData()
    flight_data.find_cheapest_flight()

    ORIGIN_CITY_IATA = "LON"


    if data_sheet[0]["iataCode"] == "":
        for value in data_sheet:
            value["iataCode"] = flight_search.get_destination(value["city"])
            time.sleep(2)

        print(f"data_sheet:\n {data_sheet}")
    
    data_manager.destination_data = data_sheet
    data_manager.update_data()
    
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in data_sheet:
        print(f"Getting flights for {destination['city']}...")
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today, 
        )
        cheapest_flight = flight_data.find_cheapest_flight(flights)
        print(f"{destination['city']}: £{cheapest_flight.price}")
        # Slowing down requests to avoid rate limit
        time.sleep(2)




if __name__ == "__main__":
    main()