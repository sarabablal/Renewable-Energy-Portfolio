# install pandas & requests liberaries
# importing pandas & requests liberaries
import requests
import pandas as pd

# target geogrphical coordinates (ouarzazate, morocco)
lat, lon = 30.93, -6.91  

# Open-Meteo API endpoint for real-time solar and wind parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

# sending HTTP GET Request to retrieve weather data
response = requests.get (url)
print (response.status_code)

# parse JSON response into a Python dictionary
data = response.json ()
print (data.keys())

# extract the current weather object
current = data ['current_weather']
print (current)

# package relevant physical parameters for PV & Wind Turbine modeling
data_dict = {
    'timestamp' : current ['time'],            # Measurement timestamp
    'temperature': current['temperature'],     # Temperature in °C
    'wind_speed' : current ['windspeed'],      # Wind speed in km/h
    'wind_degree' : current ['winddirection'], # Wind direction in degrees
    'weather_code' : current ['weathercode']   # WMO weather code
}

# convert extracted data into a single-row Pandas DataFrame
df = pd.DataFrame([data_dict])
print (df)

# append new data entry (mode='a')
df.to_csv ('weather_data.csv', mode= 'a', index=False)


print("Data successfully stored into CSV!")