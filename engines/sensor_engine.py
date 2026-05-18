import random

class SensorEngine:

    def update(self, world):

        # Temperature Sensor
        temp_real = world.environment["inside_temp"]

        temp_sensor = round(
            temp_real + random.uniform(-0.2, 0.2),
            1
        )

        # Humidity Sensor
        humidity_real = world.environment["inside_humidity"]

        humidity_sensor = round(
            humidity_real + random.uniform(-1, 1),
            1
        )

        # PIR Sensor
        pir_sensor = world.human["movement_intensity"]

        # Lux Sensor
        lux_sensor = world.environment["indoor_brightness"]

        world.sensors = {
            "temp_sensor": temp_sensor,
            "humidity_sensor": humidity_sensor,
            "pir_sensor": pir_sensor,
            "lux_sensor": lux_sensor
        }