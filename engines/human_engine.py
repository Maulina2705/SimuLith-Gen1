class HumanEngine:

    def update(self, world):

        hour = world.time["hour"]

        # Tentukan activity berdasarkan jam
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

        # Movement intensity
        movement = 0

        if activity == "Sleeping":
            movement = 2

        elif activity == "Morning Routine":
            movement = 50

        elif activity == "Gaming":
            movement = 15

        elif activity == "Relaxing":
            movement = 8

        elif activity == "Outside Working":
            movement = 0

        # Simpan ke world state
        world.human = {
            "activity": activity,
            "occupancy": occupancy,
            "movement_intensity": movement
        }