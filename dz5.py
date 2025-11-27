import requests
import pprint

class OpenWeatherMap:
    def __init__(self, city):
        self.__city = city
        self.__key = '668498292f008dbe9785969c99c8dd16'
        self.__data = self.__get_data()

    def __str__(self):
        return f"{self.get_city()}: {self.get_temp()} °C, {self.get_weather()}, Wind {self.get_wind()} m/s"

    def __get_data(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={self.__city}&appid={self.__key}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get weather data for {self.__city}")

    def get_temp(self):
        pprint.pprint(self.__get_data())
        temp = self.__data.get('main', {}).get('temp', 0)
        return round(temp - 273.15, 1)

    def get_weather(self):
        return self.__data.get('weather', {})[0].get('main', 'Unknown')

    def get_wind(self):
        return self.__data.get('wind', {}).get('speed', 'no data')

    def get_city(self):
        return self.__data.get('name', self.__city)

    def print_result(self):
        text = (
            f"City: {self.get_city()}\n"
            f"Temperature: {self.get_temp()} °C\n"
            f"Weather: {self.get_weather()}\n"
            f"Wind Speed: {self.get_wind()} m/s"

        )
        return text

    def get_any_key(self, *args):
        data = self.__data
        try:
            for key in args:
                data = data[key]
            return data
        except (KeyError, TypeError):
            return "Invalid path"

class ExtendedWeather(OpenWeatherMap):
    def get_humidity(self):
        return self.get_any_key('main', 'humidity')

    def get_full_report(self):
        return self.print_result() + f"\nHumidity: {self.get_humidity()}%"

def show_weather():
    city = input("Enter city name: ")
    try:
        weather = ExtendedWeather(city)
        print(weather.get_full_report())
    except Exception as e:
        print(f"Error: {e}")


show_weather()