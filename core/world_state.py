from datetime import datetime

class WorldState:

    def __init__(self):

        # VIRTUAL START TIME
        virtual_start = datetime(
            year=2025,
            month=1,
            day=1,
            hour=0,
            minute=0
        )

        self.time = {
            "timestamp": virtual_start,
            "hour": virtual_start.hour,
            "minute": virtual_start.minute,
            "weekday": virtual_start.strftime("%A"),
            "day": virtual_start.day,
            "month": virtual_start.month,
            "tick": 0
        }

        # WEATHER
        self.weather = {
            "weather_type": "Cloudy",
            "outside_temp": 26,
            "outside_humidity": 85,
            "weather_remaining": 120
        }

        # EVENTS
        self.events = {
            "active_event": None,
            "event_remaining": 0,
            "special_day": None
        }

        # HUMAN
        self.human = {
            "activity": "Sleeping",
            "occupancy": 1,
            "movement_intensity": 2,
            "activity_remaining": 60,
            
            "fatigue": 20,
            "stress": 15,
            "focus": 70,
            "comfort": 75
        }

        # DEVICES
        self.devices = {}

        # ENVIRONMENT
        self.environment = {
            "inside_temp": 28.0,
            "inside_humidity": 70,
            "indoor_brightness": 40
        }

        # ENERGY
        self.energy = {}

        # SENSORS
   
        self.sensors = {
            "temp_drift": 0,
            "humidity_drift": 0,
            "lux_drift": 0
        }