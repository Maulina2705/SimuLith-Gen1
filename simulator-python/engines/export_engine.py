import pandas as pd
import os

class ExportEngine:

    def __init__(self):

        self.rows = []

    def update(self, world):

        row = {

            # TIME
            "timestamp": world.time["timestamp"],
            "hour": world.time["hour"],
            "minute": world.time["minute"],
            "weekday": world.time["weekday"],

            # WEATHER
            "weather_type": world.weather["weather_type"],
            "outside_temp": world.weather["outside_temp"],
            "outside_humidity": world.weather["outside_humidity"],
            "weather_remaining": world.weather["weather_remaining"],

            # EVENTS
            "active_event": world.events["active_event"],
            "event_remaining": world.events["event_remaining"],
            "special_day": world.events["special_day"],

            # HUMAN
            "activity": world.human["activity"],
            "occupancy": world.human["occupancy"],
            "movement_intensity": world.human["movement_intensity"],
            "activity_remaining": world.human["activity_remaining"],
            "fatigue": world.human["fatigue"],
            "stress": world.human["stress"],
            "focus": world.human["focus"],
            "comfort": world.human["comfort"],

            # ENVIRONMENT
            "inside_temp": world.environment["inside_temp"],
            "inside_humidity": world.environment["inside_humidity"],
            "indoor_brightness": world.environment["indoor_brightness"],

            # AC
            "ac_state": world.devices["ac"]["state"],
            "ac_power_w": world.devices["ac"]["power_w"],
            "ac_target_temp": world.devices["ac"]["target_temp"],

            # PC
            "pc_state": world.devices["pc"]["state"],
            "pc_power_w": world.devices["pc"]["power_w"],

            # MAIN LAMP
            "main_lamp_state": world.devices["main_lamp"]["state"],
            "main_lamp_power_w": world.devices["main_lamp"]["power_w"],

            # DESK LAMP
            "desk_lamp_state": world.devices["desk_lamp"]["state"],
            "desk_lamp_power_w": world.devices["desk_lamp"]["power_w"],

            # RICE COOKER
            "rice_cooker_state": world.devices["rice_cooker"]["state"],
            "rice_cooker_power_w": world.devices["rice_cooker"]["power_w"],

            # WASHING MACHINE
            "washing_machine_state": world.devices["washing_machine"]["state"],
            "washing_machine_power_w": world.devices["washing_machine"]["power_w"],

            # ENERGY
            "total_power_w": world.energy["total_power_w"],
            "total_current_a": world.energy["total_current_a"],
            "voltage_v": world.energy["voltage_v"],
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