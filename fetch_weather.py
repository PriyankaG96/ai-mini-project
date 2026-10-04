import json
import requests
from pydantic import BaseModel, Field

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 12.97,
    "longitude": 77.59,
    "current": "temperature_2m,wind_speed_10m",
}


class CurrentWeather(BaseModel):
    temperature_2m: float = Field(..., description="Temperature in Celsius")
    wind_speed_10m: float = Field(..., description="Wind speed in km/h")
    time: str


def fetch_weather() -> dict:
    """Call the API and return the raw JSON."""
    response = requests.get(URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    return response.json()


def parse_current_weather(raw_data: dict) -> CurrentWeather:
    """Validate and parse the 'current' section into a typed model."""
    return CurrentWeather(**raw_data["current"])


def save_json(data: dict, filename: str = "weather.json") -> None:
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    try:
        raw_data = fetch_weather()
        weather = parse_current_weather(raw_data)
        print(weather)
        save_json(raw_data)
        print("Saved to weather.json")
    except requests.RequestException as error:
        print(f"Request failed: {error}")
    except Exception as error:
        print(f"Could not parse weather data: {error}")