from core.world_state import WorldState
from core.tick_engine import TickEngine
from engines.weather_engine import WeatherEngine
from engines.human_engine import HumanEngine
from engines.device_engine import DeviceEngine
from engines.energy_engine import EnergyEngine

import time

world = WorldState()

tick_engine = TickEngine()
weather_engine = WeatherEngine()
human_engine = HumanEngine()
device_engine = DeviceEngine()
energy_engine = EnergyEngine()

print("SimuLith Started")

for _ in range(5):

    tick_engine.next_tick(world)
    weather_engine.update(world)
    human_engine.update(world)
    device_engine.update(world)
    energy_engine.update(world)

    print(world.weather)
    print(world.human)
    print(world.devices)
    print(world.energy)

    time.sleep(1)