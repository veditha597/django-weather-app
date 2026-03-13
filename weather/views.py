from django.shortcuts import render
import requests

API_KEY = "cec6d5d20b2144d4b39f664b0f2ac8ac"

def index(request):
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        # Check if API returned success
        if response.status_code == 200:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }
        else:
            error = "City not found. Please enter a valid city name."

    return render(request, "index.html", {"weather": weather_data, "error": error})