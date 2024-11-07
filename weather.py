import requests

# Enter your API key here 
api_key = "a875f7309721606819e5c2191678680e"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = input("Enter city name: ")

# Construct complete URL
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

# Parse the JSON response
x = response.json()

# Print the response for debugging
print(x)  # Debug line to check the response structure

# Check if 'main' key is in the response
if response.status_code == 200 and "main" in x:
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " + str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +
          "\n humidity (in percentage) = " + str(current_humidity) +
          "\n description = " + str(weather_description))
elif response.status_code == 404:
    print("City Not Found")
else:
    print(f"Error: {x.get('message', 'Unknown error')}")
