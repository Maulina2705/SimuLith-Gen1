import random

class EventEngine:

    def update(self, world):

        # Kurangi durasi event
        if world.events["event_remaining"] > 0:

            world.events["event_remaining"] -= 1

            return

        hour = world.time["hour"]
        day = world.time["day"]
        month = world.time["month"]

        weekday = world.time["weekday"]

        active_event = None
        duration = 0
        
        # SPECIAL DAYS
        special_day = None

        # Ramadan (simple simulation)
        if month == 3:

            special_day = "Ramadan"

        # Lebaran
        if month == 4 and 1 <= day <= 5:

            special_day = "Lebaran"

        # New Year
        if month == 1 and day == 1:

            special_day = "New Year"

        # WEEKEND GAMING EVENT

        if True:

            if 18 <= hour <= 23:

                if random.random() < 0.25:

                    active_event = "Weekend Gaming"
                    duration = random.randint(120, 360)

        # LATE NIGHT WORK

        if active_event is None:

            if hour >= 21 or hour <= 1: 

                if random.random() < 0.15:

                    active_event = "Late Night Work"
                    duration = random.randint(60, 180)

        # LAUNDRY DAY

        if active_event is None:

            if 8 <= hour <= 20:

                if random.random() < 0.08:

                    active_event = "Laundry Day"
                    duration = random.randint(40, 90)

        # Save event
        world.events = {
            "active_event": active_event,
            "event_remaining": duration,
            "special_day": special_day
        }