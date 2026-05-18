import random

class WeatherEngine:

    def update(self, world):

        # Kurangi durasi cuaca
        world.weather["weather_remaining"] -= 1

        # Kalau cuaca masih aktif
        if world.weather["weather_remaining"] > 0:
            return

        hour = world.time["hour"]

        weather_types = [
            "Sunny",
            "Cloudy",
            "Light Rain",
            "Heavy Rain"
        ]

        # =========================
        # WEATHER PROBABILITY
        # =========================

        # Siang
        if 6 <= hour < 18:

            weights = [40, 35, 20, 5]

        # Malam
        else:

            weights = [15, 45, 30, 10]

        weather_type = random.choices(
            weather_types,
            weights=weights
        )[0]

        # =========================
        # WEATHER PARAMETERS
        # =========================

        if weather_type == "Sunny":

            outside_temp = random.randint(30, 34)
            outside_humidity = random.randint(45, 65)
            duration = random.randint(120, 360)

        elif weather_type == "Cloudy":

            outside_temp = random.randint(26, 30)
            outside_humidity = random.randint(65, 85)
            duration = random.randint(90, 240)

        elif weather_type == "Light Rain":

            outside_temp = random.randint(24, 28)
            outside_humidity = random.randint(80, 92)
            duration = random.randint(60, 180)

        else:

            outside_temp = random.randint(22, 26)
            outside_humidity = random.randint(90, 98)
            duration = random.randint(45, 120)

        # Save weather
        world.weather = {
            "weather_type": weather_type,
            "outside_temp": outside_temp,
            "outside_humidity": outside_humidity,
            "weather_remaining": duration
        }