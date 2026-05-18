from datetime import timedelta

class TimeEngine:

    def update(self, world):

        # tambah 1 menit virtual
        world.time["timestamp"] += timedelta(minutes=1)

        # update tick
        world.time["tick"] += 1

        # update shortcut values
        timestamp = world.time["timestamp"]

        world.time["hour"] = timestamp.hour
        world.time["minute"] = timestamp.minute
        world.time["weekday"] = timestamp.strftime("%A")
        world.time["day"] = timestamp.day
        world.time["month"] = timestamp.month