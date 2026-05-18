from datetime import timedelta

class TickEngine:
    def __init__(self):
        self.tick = 0

    def next_tick(self, world):
        self.tick += 1

        world.time["timestamp"] += timedelta(minutes=1)

        current = world.time["timestamp"]

        world.time["hour"] = current.hour
        world.time["minute"] = current.minute
        world.time["weekday"] = current.strftime("%A")

        print(f"[TICK {self.tick}] {current}")