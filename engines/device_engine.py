class DeviceEngine:

    def update(self, world):

        activity = world.human["activity"]

        devices = {}

        # AC Logic
        if world.human["occupancy"] > 0:
            devices["ac"] = {
                "state": "ON",
                "power_w": 500
            }
        else:
            devices["ac"] = {
                "state": "OFF",
                "power_w": 0
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