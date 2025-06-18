import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual API key
api_key = "5dfe1d2dd87128f61cdba9b8f1dcf9d8"
city_name = "New Delhi"  # You can change this to any city in India
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric" # Use metric for Celsius

try:
    response = requests.get(complete_url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = {
            "temperature": main_data["temp"],
            "feels_like": main_data["feels_like"],
            "humidity": main_data["humidity"],
            "pressure": main_data["pressure"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
            "city": data["name"],
            "country": data["sys"]["country"]
        }
        print("Weather data fetched successfully:")
        print(json.dumps(weather_data, indent=4))

        # Convert to Pandas DataFrame for easier plotting
        df = pd.DataFrame([weather_data])

        # Data Visualization
        plt.figure(figsize=(10, 6))
        sns.barplot(x=["Temperature", "Feels Like", "Humidity", "Pressure", "Wind Speed"],
                    y=[df["temperature"][0], df["feels_like"][0], df["humidity"][0], df["pressure"][0], df["wind_speed"][0]])
        plt.title(f"Current Weather in {df['city'][0]}, {df['country'][0]}")
        plt.ylabel("Value")
        plt.xlabel("Weather Parameter")
        plt.show()

        print("\nSimple bar plot showing the main weather parameters has been generated.")

    else:
        print("City not found.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except KeyError as e:
    print(f"Error accessing data: Key '{e}' not found in the API response.")