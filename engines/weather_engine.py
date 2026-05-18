class WeatherEngine:
    def update(self, world):

        hour = world.time["hour"]

        if 6 <= hour < 12:
            weather_type = "Sunny"
            outside_temp = 30

        elif 12 <= hour < 18:
            weather_type = "Hot"
            outside_temp = 33

        else:
            weather_type = "Cloudy"
            outside_temp = 26

        world.weather = {
            "weather_type": weather_type,
            "outside_temp": outside_temp
        }