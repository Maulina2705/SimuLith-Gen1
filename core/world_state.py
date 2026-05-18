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

        self.weather = {}
        self.human = {}
        self.devices = {}
        self.environment = {
            "inside_temp": 28.0,
            "inside_humidity": 70,
            "indoor_brightness": 40
        }
        self.energy = {}
        self.sensors = {}