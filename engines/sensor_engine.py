import random

class SensorEngine:

    def update(self, world):

        # SENSOR DRIFT UPDATE

        world.sensors["temp_drift"] += random.uniform(-0.02, 0.02)

        world.sensors["humidity_drift"] += random.uniform(-0.05, 0.05)

        world.sensors["lux_drift"] += random.uniform(-0.1, 0.1)
        
        # Temperature Sensor
        temp_real = world.environment["inside_temp"]

        temp_sensor = round(
            temp_real
            + world.sensors["temp_drift"]
            + random.uniform(-0.2, 0.2),
            1
        )

        # Humidity Sensor
        humidity_real = world.environment["inside_humidity"]

        humidity_sensor = round(
            humidity_real
            + world.sensors["humidity_drift"]
            + random.uniform(-1, 1),
            1
        )
        # PIR Sensor
        pir_sensor = world.human["movement_intensity"]

        # False positive chance
        if random.random() < 0.02:

            pir_sensor += random.randint(1, 5)

        # Lux Sensor
        lux_sensor = round(
            world.environment["indoor_brightness"]
            + world.sensors["lux_drift"]
            + random.uniform(-2, 2)
        )

        world.sensors = {
            "temp_sensor": temp_sensor,
            "humidity_sensor": humidity_sensor,
            "pir_sensor": pir_sensor,
            "lux_sensor": lux_sensor
        }