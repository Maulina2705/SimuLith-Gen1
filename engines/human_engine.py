class HumanEngine:

    def update(self, world):

        hour = world.time["hour"]

        movement = 0

        if activity == "Sleeping":
            movement = 2

        elif activity == "Morning Routine":
            movement = 50

        elif activity == "Gaming":
            movement = 15

        elif activity == "Relaxing":
            movement = 8

        world.human = {
            "activity": activity,
            "occupancy": occupancy,
            "movement_intensity": movement
        }