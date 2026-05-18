import json
import paho.mqtt.client as mqtt


class MqttEngine:

    def __init__(self):

        self.client = mqtt.Client()

        self.client.connect("localhost", 1883, 60)

    def update(self, world):

        payload = {

            "timestamp": str(world.time["timestamp"]),

            # SENSOR
            "temp_sensor": world.sensors["temp_sensor"],
            "humidity_sensor": world.sensors["humidity_sensor"],
            "pir_sensor": world.sensors["pir_sensor"],
            "lux_sensor": world.sensors["lux_sensor"],

            # POWER
            "total_power_w": world.energy["total_power_w"],
            "total_current_a": world.energy["total_current_a"],
            "voltage_v": world.energy["voltage_v"],
            "total_energy_kwh": world.energy["total_energy_kwh"],

            # SMARTPLUG
            "smartplug": {

                "ac": world.devices["ac"]["power_w"],

                "pc": world.devices["pc"]["power_w"],

                "tv": world.devices["tv"]["power_w"],

                "rice_cooker":
                    world.devices["rice_cooker"]["power_w"],

                "washing_machine":
                    world.devices["washing_machine"]["power_w"]
            }
        }

        self.client.publish(
            "simulith/room1",
            json.dumps(payload)
        )