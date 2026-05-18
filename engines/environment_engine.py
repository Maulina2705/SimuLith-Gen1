class EnvironmentEngine:

    def update(self, world):

        inside_temp = world.environment["inside_temp"]

        outside_temp = world.weather["outside_temp"]

        ac_state = world.devices["ac"]["state"]

        pc_state = world.devices["pc"]["state"]

        # suhu luar mempengaruhi suhu dalam
        if outside_temp > inside_temp:
            inside_temp += 0.05
        else:
            inside_temp -= 0.02

        # AC mendinginkan ruangan
        if ac_state == "MAX_COOLING":
            inside_temp -= 0.22

        elif ac_state == "COOLING":
            inside_temp -= 0.15

        elif ac_state == "MAINTAIN":
            inside_temp -= 0.07

        elif ac_state == "IDLE":
            inside_temp -= 0.02

        # PC gaming menghasilkan panas
        if pc_state == "GAMING":
            inside_temp += 0.03

        # batas suhu realistis
        inside_temp = max(16, min(35, inside_temp))

        world.environment["inside_temp"] = round(inside_temp, 2)
        
        # INDOOR BRIGHTNESS
        indoor_brightness = 20

        hour = world.time["hour"]

        weather_type = world.weather["weather_type"]

        main_lamp_state = world.devices["main_lamp"]["state"]

        # Siang
        if 6 <= hour < 18:

            indoor_brightness = 70

            # Mendung lebih gelap
            if weather_type == "Cloudy":
                indoor_brightness = 45

        # Malam
        else:
            indoor_brightness = 5

        # Lampu utama
        if main_lamp_state == "ON":
            indoor_brightness += 55

        # Lampu meja gaming
        if world.devices["desk_lamp"]["state"] == "ON":
            indoor_brightness += 15

        world.environment["indoor_brightness"] = indoor_brightness