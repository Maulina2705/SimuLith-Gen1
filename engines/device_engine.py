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

        world.devices = devices