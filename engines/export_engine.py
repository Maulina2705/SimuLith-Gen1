import pandas as pd
import os

class ExportEngine:

    def __init__(self):

        self.rows = []

    def update(self, world):

        row = {

            # TIME
            "timestamp": world.time["timestamp"],

            # WEATHER
            "weather_type": world.weather["weather_type"],
            "outside_temp": world.weather["outside_temp"],

            # HUMAN
            "activity": world.human["activity"],
            "occupancy": world.human["occupancy"],
            "movement_intensity": world.human["movement_intensity"],

            # ENVIRONMENT
            "inside_temp": world.environment["inside_temp"],
            "inside_humidity": world.environment["inside_humidity"],

            # ENERGY
            "total_power_w": world.energy["total_power_w"],
            "total_energy_kwh": world.energy["total_energy_kwh"],

            # SENSOR
            "temp_sensor": world.sensors["temp_sensor"],
            "humidity_sensor": world.sensors["humidity_sensor"],
            "pir_sensor": world.sensors["pir_sensor"],
            "lux_sensor": world.sensors["lux_sensor"]

        }

        self.rows.append(row)

    def save_csv(self):

        os.makedirs("simulation", exist_ok=True)

        df = pd.DataFrame(self.rows)

        df.to_csv("simulation/simulated_data.csv", index=False)

        print("CSV Saved Successfully")