import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_temp(date, data):
    for item in data['list']:
        if date in item['dt_txt']:
            return item['main']['temp']
    return None

def get_wind_speed(date, data):
    for item in data['list']:
        if date in item['dt_txt']:
            return item['wind']['speed']
    return None

def get_pressure(date, data):
    for item in data['list']:
        if date in item['dt_txt']:
            return item['main']['pressure']
    return None

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temp = get_temp(date, data)
            if temp is not None:
                print(f"Temperature on {date}: {temp} K")
            else:
                print("Data not found for the given date.")

        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed(date, data)
            if wind_speed is not None:
                print(f"Wind speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date.")

        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure(date, data)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the given date.")

        elif choice == 0:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
