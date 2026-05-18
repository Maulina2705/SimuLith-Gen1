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
        if ac_state == "ON":
            inside_temp -= 0.15

        # PC gaming menghasilkan panas
        if pc_state == "GAMING":
            inside_temp += 0.03

        # batas suhu realistis
        inside_temp = max(16, min(35, inside_temp))

        world.environment["inside_temp"] = round(inside_temp, 2)