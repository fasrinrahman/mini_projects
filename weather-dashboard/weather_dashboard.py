# =========================
# MINI PROJECT 7
# Weather Dashboard
# =========================

import requests


def get_weather(city):

    url = "https://wttr.in/" + city + "?format=j1"

    try:

        response = requests.get(url)

        data = response.json()

        current = data["current_condition"][0]

        print("\n===== WEATHER REPORT =====")

        print("City:", city)

        print("Temperature:", current["temp_C"], "°C")

        print("Humidity:", current["humidity"], "%")

        print("Weather:", current["weatherDesc"][0]["value"])

    except Exception as error:

        print("Error occurred:", error)


while True:

    city = input("\nEnter city name (or exit): ")

    if city.lower() == "exit":
        print("===================")
        print("==== Thank you ====")
        print("===================")
        break

    get_weather(city)
