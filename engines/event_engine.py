import random

class EventEngine:

    def update(self, world):

        # Kurangi durasi event
        if world.events["event_remaining"] > 0:

            world.events["event_remaining"] -= 1

            return

        hour = world.time["hour"]

        weekday = world.time["weekday"]

        active_event = None
        duration = 0

        # WEEKEND GAMING EVENT

        if weekday in ["Saturday", "Sunday"]:

            if 18 <= hour <= 23:

                if random.random() < 0.25:

                    active_event = "Weekend Gaming"
                    duration = random.randint(120, 360)

        # LATE NIGHT WORK

        if active_event is None:

            if 21 <= hour <= 1:

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
            "event_remaining": duration
        }