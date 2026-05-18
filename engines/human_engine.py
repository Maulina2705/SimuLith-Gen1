class HumanEngine:

    def update(self, world):

        hour = world.time["hour"]

        if 0 <= hour < 6:
            activity = "Sleeping"
            occupancy = 1

        elif 6 <= hour < 8:
            activity = "Morning Routine"
            occupancy = 1

        elif 8 <= hour < 17:
            activity = "Outside Working"
            occupancy = 0

        elif 17 <= hour < 22:
            activity = "Gaming"
            occupancy = 1

        else:
            activity = "Relaxing"
            occupancy = 1

        world.human = {
            "activity": activity,
            "occupancy": occupancy
        }