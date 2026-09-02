## Weather Scraper for Solar/Wind Forecasting
An automated Python script designed to harvest real-time meteorological data for renewable energy forecasting. This tool queries the Open-Meteo API to extract critical weather parameters for Ouarzazate, Morocco, and continuously appends the structured data into a local CSV file for machine learning and energy yield modeling.

### Features

* Live API Data Extraction: Pulls real-time temperature, wind speed, wind direction, and WMO weather codes.
* Geotargeted Tracking: Hardcoded to monitor coordinates (30.93, -6.91)—highly relevant for solar/wind energy analysis in Ouarzazate.
* Persistent Storage: Automatically structures the JSON payload and appends new logs to a weather_data.csv database without overwriting historical data.
* Data-Science Ready: Outputs data directly into a Pandas DataFrame, making it immediately ready for feature engineering and predictive analysis.

### Captured Parameters

* timestamp: Precise ISO 8601 measurement time.
* temperature: Ambient temperature in °C (critical for solar PV efficiency tracking).
* wind_speed: Local wind velocity in km/h.
* wind_degree: Wind direction vector in degrees (0-360°).
* weather_code: WMO Weather interpretation code for cloud cover and precipitation status.

### Tech Stack

* Language: Python 3.x
* Data Handling: Pandas
* Networking: Requests API

### Getting Started
Install the required libraries using pip:
pip install pandas requests

### Data Output Preview
Your data will compile inside weather_data.csv in the following format:

| timestamp | temperature | wind_speed | wind_degree | weather_code |
|---|---|---|---|---|
| 2026-08-30T20:00 | 28.5 | 12.4 | 190 | 0 |

