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
        weather_type = world.weather["weather_type"]
        weekday = world.time["weekday"]

        activity = "Idle"
        occupancy = 1
        duration = 30
        
        fatigue = world.human["fatigue"]
        stress = world.human["stress"]
        focus = world.human["focus"]
        comfort = world.human["comfort"]
        
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

                sleeping_weight = 80 + (fatigue * 0.4)

                gaming_weight = 10

                sidejob_weight = 10 + (stress * 0.2)

                activity = random.choices(
                    ["Sleeping", "Gaming", "Side Job"],
                    weights=[
                        sleeping_weight,
                        gaming_weight,
                        sidejob_weight
                    ]
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

            # EVENING
            elif 17 <= hour < 22:

                gaming_weight = 30

                relaxing_weight = 30 + (fatigue * 0.2)

                sidejob_weight = (
                    15
                    + (stress * 0.3)
                    + (focus * 0.1)
                )

                tv_weight = 10

                # Weather influence
                if weather_type == "Heavy Rain":

                    gaming_weight += 15

                elif weather_type == "Light Rain":

                    gaming_weight += 8

                activity = random.choices(
                    ["Gaming", "Relaxing", "Side Job", "Watching TV"],
                    weights=[
                        gaming_weight,
                        relaxing_weight,
                        sidejob_weight,
                        tv_weight
                    ]
                )[0]

            # Late Night
            else:

                if weather_type == "Heavy Rain":

                    weights = [50, 35, 15]

                elif weather_type == "Light Rain":

                    weights = [40, 40, 20]

                else:

                    weights = [50, 40, 10]

                activity = random.choices(
                    ["Relaxing", "Sleeping", "Gaming"],
                    weights=weights
                )[0]

        # Duration realism
        if activity == "Sleeping":
            duration = random.randint(240, 480)

        elif activity == "Gaming":
            duration = random.randint(30, 180)

        elif activity == "Side Job":

            duration = random.randint(60,120 + int(focus))

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
        
        # INTERNAL HUMAN STATE
        fatigue = world.human["fatigue"]
        stress = world.human["stress"]
        focus = world.human["focus"]
        comfort = world.human["comfort"]

        inside_temp = world.environment["inside_temp"]

        # FATIGUE LOGIC

        if activity == "Sleeping":

            fatigue -= random.randint(8, 15)

        elif activity in ["Gaming", "Side Job"]:

            fatigue += random.randint(4, 8)

        elif activity == "Outside Working":

            fatigue += random.randint(6, 10)

        else:

            fatigue += random.randint(1, 3)

        # STRESS LOGIC

        if activity == "Side Job":

            stress += random.randint(3, 7)

        elif activity in ["Relaxing", "Watching TV"]:

            stress -= random.randint(2, 5)

        elif activity == "Sleeping":

            stress -= random.randint(1, 4)

        # FOCUS LOGIC

        if activity == "Side Job":

            focus += random.randint(1, 4)

        elif activity == "Gaming":

            focus -= random.randint(1, 3)

        elif activity == "Sleeping":

            focus += random.randint(2, 5)

        # COMFORT LOGIC

        if 22 <= inside_temp <= 26:

            comfort += random.randint(1, 3)

        else:

            comfort -= random.randint(2, 5)

        # Clamp values
        fatigue = max(0, min(100, fatigue))
        stress = max(0, min(100, stress))
        focus = max(0, min(100, focus))
        comfort = max(0, min(100, comfort))

        # Save state
        world.human = {
            "activity": activity,
            "occupancy": occupancy,
            "movement_intensity": movement,
            "activity_remaining": duration,
            
            "fatigue": fatigue,
            "stress": stress,
            "focus": focus,
            "comfort": comfort
        }