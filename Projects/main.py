import requests

API_KEY = "0bcc0df70a63eef71b1ee778c6166546"

city = input("Enter a city: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}&units=imperial"
)

response = requests.get(url)

if response.status_code == 200:
    print(data)
    print("\nWeather Report")
    print("----------------")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°F")
    print(f"Feels Like: {data['main']['feels_like']}°F")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Condition: {data['weather'][0]['description']}")
    print(f"Wind Speed: {data['wind']['speed']} mph")

else:
    print("Error:", response.status_code)
    print(response.json())
