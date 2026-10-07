import json
import subprocess
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class WeatherData:
    city: str
    temperature: int
    country: str


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    result = subprocess.run(
        [
            "curl.exe",
            "-s",
            "--http1.1",
            "--max-time", "5",
            "-H", "Connection: close",
            url
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    response = result.stdout

    current_start = response.index('"current_condition"')
    current_start = response.index("[", current_start)

    decoder = json.JSONDecoder()
    current_condition, _ = decoder.raw_decode(
        response[current_start:]
    )

    area_start = response.index('"nearest_area"')
    area_start = response.index("[", area_start)

    nearest_area, _ = decoder.raw_decode(
        response[area_start:]
    )

    temperature = int(
        current_condition[0]["temp_C"]
    )

    country = (
        nearest_area[0]["country"][0]["value"]
    )

    return WeatherData(
        city=city,
        temperature=temperature,
        country=country
    )


def main():
    with open("cities.txt", "r", encoding="utf-8") as file:
        cities = [
            line.strip()
            for line in file
            if line.strip()
        ]

    unique_cities = set(cities)

    weather_data = []

    for city in unique_cities:
        print(f"Получаю данные для {city}...")

        try:
            weather = get_weather(city)
            weather_data.append(weather)

            print("Получено.")

        except Exception as error:
            print(f"Ошибка: {error}")

    print("\nПогода по городам:")

    for weather in sorted(weather_data, key=lambda x: x.city):
        print(
            f"{weather.city}, {weather.country} "
            f"{weather.temperature:+d} °C"
        )

    countries = defaultdict(list)

    for weather in weather_data:
        countries[weather.country].append(weather)

    print("\nСтатистика по странам:")

    for country, cities_data in sorted(countries.items()):
        temperatures = [
            weather.temperature
            for weather in cities_data
        ]

        count = len(cities_data)
        average = sum(temperatures) / count
        minimum = min(temperatures)
        maximum = max(temperatures)

        print(
            f"{country} - {count} cities, "
            f"avg: {average:+.0f} °C, "
            f"min: {minimum:+d} °C, "
            f"max: {maximum:+d} °C"
        )


if __name__ == "__main__":
    main()