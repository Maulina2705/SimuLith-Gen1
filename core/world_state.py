from datetime import datetime

class WorldState:
    def __init__(self):
        now = datetime.now()

        self.time = {
            "timestamp": now,
            "hour": now.hour,
            "minute": now.minute,
            "weekday": now.strftime("%A")
        }

        self.weather = {
            "weather_type": "Cloudy",
            "outside_temp": 26,
            "outside_humidity": 85,
            "weather_remaining": 120
        }
        self.human = {
            "activity": "Sleeping",
            "occupancy": 1,
            "movement_intensity": 2,
            "activity_remaining": 60
        }
        self.devices = {}
        self.environment = {
            "inside_temp": 28.0,
            "inside_humidity": 70,
            "indoor_brightness": 40
        }
        self.energy = {}
        self.sensors = {}