# AI Mini Project
# AI Mini Project

A small Python script that fetches current weather data from the Open-Meteo API, validates it with Pydantic, and saves it to a JSON file.

## What it does
- Calls the Open-Meteo API for current temperature and wind speed
- Validates the response using a Pydantic model (`CurrentWeather`)
- Saves the raw response to `weather.json`
- Handles network and validation errors gracefully

## Setup
\`\`\`
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Run
\`\`\`
python fetch_weather.py
\`\`\`

## Test
\`\`\`
pytest
\`\`\`

## What this demonstrates
- Calling an external API with `requests`
- Structured data validation with `pydantic`
- Writing unit tests with `pytest`