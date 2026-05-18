import random

class WeatherEngine:

    def update(self, world):

        # Kurangi durasi cuaca
        world.weather["weather_remaining"] -= 1

        # Kalau cuaca masih aktif
        if world.weather["weather_remaining"] > 0:
            return

        hour = world.time["hour"]

        # Pilihan cuaca berdasarkan waktu
        if 6 <= hour < 12:

            weather_type = random.choices(
                ["Sunny", "Cloudy"],
                weights=[70, 30]
            )[0]

        elif 12 <= hour < 18:

            weather_type = random.choices(
                ["Hot", "Sunny", "Cloudy"],
                weights=[50, 30, 20]
            )[0]

        else:

            weather_type = random.choices(
                ["Cloudy", "Light Rain"],
                weights=[70, 30]
            )[0]

        # Temperature & humidity
        if weather_type == "Sunny":
            outside_temp = random.randint(29, 32)
            outside_humidity = random.randint(50, 65)

        elif weather_type == "Hot":
            outside_temp = random.randint(32, 35)
            outside_humidity = random.randint(40, 55)

        elif weather_type == "Cloudy":
            outside_temp = random.randint(25, 29)
            outside_humidity = random.randint(70, 85)

        elif weather_type == "Light Rain":
            outside_temp = random.randint(23, 27)
            outside_humidity = random.randint(85, 95)

        # Durasi cuaca
        duration = random.randint(60, 240)

        world.weather = {
            "weather_type": weather_type,
            "outside_temp": outside_temp,
            "outside_humidity": outside_humidity,
            "weather_remaining": duration
        }