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
        self.environment = {}
        self.energy = {}
        self.sensors = {}