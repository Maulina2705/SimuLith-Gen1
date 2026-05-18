import random

class DeviceEngine:

    def update(self, world):

        activity = world.human["activity"]
        comfort = world.human["comfort"]
        fatigue = world.human["fatigue"]
        stress = world.human["stress"]

        day = world.time["day"]

        weather_type = world.weather["weather_type"]

        hour = world.time["hour"]

        indoor_brightness = world.environment["indoor_brightness"]

        devices = {}

        # AC LOGIC
        occupancy = world.human["occupancy"]

        if occupancy > 0:

            inside_temp = world.environment["inside_temp"]

                        # Comfort-based AC behavior
            if comfort < 40:

                ac_state = "MAX_COOLING"
                ac_power = 820
                target_temp = 16

            elif inside_temp >= 28:

                ac_state = "MAX_COOLING"
                ac_power = 750
                target_temp = 16

            elif inside_temp >= 25:

                ac_state = "COOLING"
                ac_power = 520
                target_temp = 18

                # End of month saving behavior
                if day >= 25:

                    target_temp = 20

                    if ac_power > 500:
                        ac_power -= 80

                ac_state = "MAINTAIN"
                ac_power = 320
                target_temp = 21

            else:

                ac_state = "IDLE"
                ac_power = 120
                target_temp = 22

        else:

            ac_state = "OFF"
            ac_power = 0
            target_temp = None

        devices["ac"] = {
            "state": ac_state,
            "target_temp": target_temp,
            "power_w": ac_power
        }

        # MAIN LAMP
        lamp_state = "OFF"
        lamp_power = 0

        # malam
        if hour >= 18 or hour <= 5:

            if activity in ["Gaming", "Watching TV"]:

                if random.random() < 0.4:

                    lamp_state = "ON"
                    lamp_power = 18

            elif activity in ["Side Job", "Cooking"]:

                lamp_state = "ON"
                lamp_power = 18

            elif activity == "Sleeping":

                lamp_state = "OFF"
                lamp_power = 0

            else:

                if random.random() < 0.5:

                    lamp_state = "ON"
                    lamp_power = 18

        # siang cloudy
        elif indoor_brightness < 40:

            if occupancy > 0:

                if random.random() < 0.3:

                    lamp_state = "ON"
                    lamp_power = 18

        devices["main_lamp"] = {
            "state": lamp_state,
            "power_w": lamp_power
        }

        # DESK LAMP
        desk_state = "OFF"
        desk_power = 0

        if activity in ["Gaming", "Side Job"]:

            desk_state = "ON"
            desk_power = 8

        devices["desk_lamp"] = {
            "state": desk_state,
            "power_w": desk_power
        }

        # PC LOGIC
        pc_state = "OFF"
        pc_power = 0

        if activity == "Gaming":

            pc_state = "GAMING"
            pc_power = random.randint(320, 450)

        elif activity == "Side Job":

            if random.random() < 0.7:

                pc_state = "WORKING"
                pc_power = random.randint(120, 220)

        devices["pc"] = {
            "state": pc_state,
            "power_w": pc_power
        }

        # TV LOGIC
        tv_state = "OFF"
        tv_power = 0

        if activity == "Watching TV":

            tv_state = "ON"
            tv_power = random.randint(45, 90)

        elif activity == "Gaming":

            if random.random() < 0.25:

                tv_state = "ON"
                tv_power = random.randint(45, 90)

        devices["tv"] = {
            "state": tv_state,
            "power_w": tv_power
        }

        # RICE COOKER
        rice_state = "OFF"
        rice_power = 0

        if activity == "Cooking":

            rice_state = "COOKING"
            rice_power = 300

        else:

            if random.random() < 0.15:

                rice_state = "WARM"
                rice_power = 35

        devices["rice_cooker"] = {
            "state": rice_state,
            "power_w": rice_power
        }

        # WASHING MACHINE
        wm_state = "OFF"
        wm_power = 0

        if world.events["active_event"] == "Laundry Day":

            wm_state = "RUNNING"
            wm_power = random.randint(300, 450)

        devices["washing_machine"] = {
            "state": wm_state,
            "power_w": wm_power
        }

        world.devices = devices