class TickEngine:

    def __init__(self):
        self.tick = 0

    def next_tick(self, world):

        self.tick += 1

        print(f"[TICK {self.tick}]")