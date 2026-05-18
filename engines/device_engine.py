class DeviceEngine:

    def update(self, world):

        activity = world.human["activity"]

        devices = {}

        # AC Logic
        inside_temp = world.environment["inside_temp"]

        target_temp = 16

        temp_difference = inside_temp - target_temp

        ac_power = 0
        ac_mode = "OFF"

        if world.human["occupancy"] > 0:

            # MAX COOLING
            if temp_difference > 8:
                ac_power = 750
                ac_mode = "MAX_COOLING"

            # NORMAL COOLING
            elif temp_difference > 4:
                ac_power = 500
                ac_mode = "COOLING"

            # MAINTAIN TEMP
            elif temp_difference > 1:
                ac_power = 280
                ac_mode = "MAINTAIN"

            # IDLE
            else:
                ac_power = 120
                ac_mode = "IDLE"

        devices["ac"] = {
            "state": ac_mode,
            "target_temp": target_temp,
            "power_w": ac_power
        }

        # PC Logic
        if activity == "Gaming":
            devices["pc"] = {
                "state": "GAMING",
                "power_w": 350
            }
        else:
            devices["pc"] = {
                "state": "OFF",
                "power_w": 0
            }

        # Desk Lamp Logic
        if activity == "Gaming":
            devices["desk_lamp"] = {
                "state": "ON",
                "power_w": 8
            }
        else:
            devices["desk_lamp"] = {
                "state": "OFF",
                "power_w": 0
            }
        
        # MAIN LAMP LOGIC
        lamp_power = 0
        lamp_state = "OFF"

        hour = world.time["hour"]

        weather_type = world.weather["weather_type"]

        occupancy = world.human["occupancy"]

        # Malam hari
        if hour >= 18 or hour < 6:

            if occupancy > 0:
                lamp_state = "ON"
                lamp_power = 18

        # Siang mendung/hujan
        elif weather_type == "Cloudy":

            if occupancy > 0:
                lamp_state = "ON"
                lamp_power = 18

        devices["main_lamp"] = {
            "state": lamp_state,
            "power_w": lamp_power
        }
        
        # RICE COOKER LOGIC
        rice_state = "OFF"
        rice_power = 0

        activity = world.human["activity"]

        current_minute = world.time["minute"]

        # Masak pagi
        if activity in ["Morning Routine", "Cooking"]:

            # Awal jam → cooking
            if current_minute < 20:

                rice_state = "COOKING"
                rice_power = 300

            # Setelah masak → warm
            else:

                rice_state = "WARM"
                rice_power = 35

        devices["rice_cooker"] = {
            "state": rice_state,
            "power_w": rice_power
        }
        
        # WASHING MACHINE LOGIC
        washing_state = "OFF"
        washing_power = 0

        current_hour = world.time["hour"]

        current_minute = world.time["minute"]

        active_event = world.events["active_event"]

        # Laundry Event
        if active_event == "Laundry Day":

            # Total cycle ~ 60 menit

            # Fill Water
            if current_minute < 10:

                washing_state = "FILL"
                washing_power = 120

            # Wash
            elif current_minute < 35:

                washing_state = "WASH"
                washing_power = 350

            # Rinse
            elif current_minute < 50:

                washing_state = "RINSE"
                washing_power = 250

            # Spin
            else:

                washing_state = "SPIN"
                washing_power = 500

        devices["washing_machine"] = {
            "state": washing_state,
            "power_w": washing_power
        }

        world.devices = devices