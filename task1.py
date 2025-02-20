import requests
import matplotlib.pyplot as plt

# Replace with your actual API key
api_key = "OPENWEATHER_API_KEY"  # Make sure to replace this with your OpenWeatherMap API key

# Function to get the temperature of a city
def get_temperature(city):
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        temperature_celsius = main_data['temp'] - 273.15  # Convert from Kelvin to Celsius
        return temperature_celsius
    else:
        return None  # If the city is not found or there's an error

# Main code to interact with the user
def main():
    city = input("Enter the name of the city to get the temperature: ").strip()
    temperature = get_temperature(city)
    
    if temperature is not None:
        print(f"The temperature in {city} is {temperature:.2f}°C")
        
        # Create a bar chart for the selected city (you could add more cities if needed)
        plt.bar([city], [temperature], color='skyblue')
        plt.xlabel("City")
        plt.ylabel("Temperature (°C)")
        plt.title(f"Temperature in {city}")
        plt.show()
    else:
        print(f"Sorry, we couldn't retrieve the weather data for {city}. Please check the city name.")

if __name__ == "__main__":
    main()
