import pytest
from pydantic import ValidationError
from fetch_weather import CurrentWeather, parse_current_weather


def test_parse_current_weather_valid_data():
    """A well-formed API response should parse into a CurrentWeather object."""
    raw_data = {
        "current": {
            "temperature_2m": 25.1,
            "wind_speed_10m": 6.9,
            "time": "2026-10-04T15:00",
        }
    }
    weather = parse_current_weather(raw_data)
    assert weather.temperature_2m == 25.1
    assert weather.wind_speed_10m == 6.9
    assert weather.time == "2026-10-04T15:00"


def test_parse_current_weather_missing_field():
    """If a required field is missing, pydantic should raise an error."""
    raw_data = {
        "current": {
            "temperature_2m": 25.1,
            # wind_speed_10m is missing on purpose
            "time": "2026-10-04T15:00",
        }
    }
    with pytest.raises(ValidationError):
        parse_current_weather(raw_data)


def test_parse_current_weather_wrong_type():
    """If a field has the wrong type, pydantic should raise an error."""
    raw_data = {
        "current": {
            "temperature_2m": "not-a-number",
            "wind_speed_10m": 6.9,
            "time": "2026-10-04T15:00",
        }
    }
    with pytest.raises(ValidationError):
        parse_current_weather(raw_data)