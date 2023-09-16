# (c) 2018 Manikandan
from weather import Weather

def load_api_key():
    try:
        with open('api_key.txt', 'r') as key_file:
            api_key = key_file.read().strip()
        return api_key
    except FileNotFoundError:
        print("API key not found. Please create a file 'api_key.txt' and add your OpenWeatherMap API key.")
        exit(1)

def main():
    api_key = load_api_key()
    weather = Weather(api_key)

    while True:
        print("Weather Forecast App")
        print("1. Get Weather Forecast")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter the city name: ")
            data = weather.get_weather(city)

            if data:
                print(f"Weather in {city}:")
                print(f"Temperature: {data['main']['temp']}°C")
                print(f"Description: {data['weather'][0]['description']}")
            else:
                print("Could not retrieve weather data. Please check the city name and your API key.")

        elif choice == '2':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
