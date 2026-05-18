import random

class HumanEngine:

    def update(self, world):

        # Kurangi durasi activity
        world.human["activity_remaining"] -= 1

        # Force override by active events
        active_event = world.events["active_event"]

        if active_event in ["Weekend Gaming", "Late Night Work"]:

            world.human["activity_remaining"] = 0

        # Kalau activity masih ada
        if world.human["activity_remaining"] > 0:
            return

        hour = world.time["hour"]
        active_event = world.events["active_event"]

        activity = "Idle"
        occupancy = 1
        duration = 30
        
        # HARD EVENT OVERRIDE
        if active_event == "Weekend Gaming":

            activity = "Gaming"
            occupancy = 1

        elif active_event == "Late Night Work":

            activity = "Side Job"
            occupancy = 1

        else:

            # Midnight - Early Morning
            if 0 <= hour < 6:

                activity = random.choices(
                    ["Sleeping", "Gaming", "Side Job"],
                    weights=[80, 10, 10]
                )[0]

            # Morning
            elif 6 <= hour < 8:

                activity = random.choices(
                    ["Morning Routine", "Cooking", "Relaxing"],
                    weights=[60, 25, 15]
                )[0]

            # Work Hours
            elif 8 <= hour < 17:

                activity = "Outside Working"
                occupancy = 0

            # Evening
            elif 17 <= hour < 22:

                weights = [40, 30, 20, 10]

                activity = random.choices(
                    ["Gaming", "Relaxing", "Side Job", "Watching TV"],
                    weights=weights
                )[0]

            # Late Night
            else:

                activity = random.choices(
                    ["Relaxing", "Sleeping", "Gaming"],
                    weights=[50, 40, 10]
                )[0]

        # Duration realism
        if activity == "Sleeping":
            duration = random.randint(240, 480)

        elif activity == "Gaming":
            duration = random.randint(30, 180)

        elif activity == "Side Job":
            duration = random.randint(60, 240)

        elif activity == "Watching TV":
            duration = random.randint(20, 90)

        elif activity == "Cooking":
            duration = random.randint(10, 40)

        elif activity == "Morning Routine":
            duration = random.randint(20, 60)

        elif activity == "Relaxing":
            duration = random.randint(30, 120)

        elif activity == "Outside Working":
            duration = random.randint(480, 540)

        # Occupancy
        if activity == "Outside Working":
            occupancy = 0
        else:
            occupancy = 1

        # Movement
        movement = 5

        if activity == "Sleeping":
            movement = 2

        elif activity == "Morning Routine":
            movement = 50

        elif activity == "Gaming":
            movement = 15

        elif activity == "Relaxing":
            movement = 8

        elif activity == "Cooking":
            movement = 45

        elif activity == "Side Job":
            movement = 12

        elif activity == "Watching TV":
            movement = 6

        elif activity == "Outside Working":
            movement = 0

        # Save state
        world.human = {
            "activity": activity,
            "occupancy": occupancy,
            "movement_intensity": movement,
            "activity_remaining": duration
        }