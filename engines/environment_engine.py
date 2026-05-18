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