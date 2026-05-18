from core.world_state import WorldState
from core.tick_engine import TickEngine
from engines.weather_engine import WeatherEngine
from engines.human_engine import HumanEngine
from engines.device_engine import DeviceEngine
from engines.energy_engine import EnergyEngine
from engines.environment_engine import EnvironmentEngine
from engines.sensor_engine import SensorEngine
from engines.export_engine import ExportEngine
from engines.event_engine import EventEngine
from engines.time_engine import TimeEngine

import time

world = WorldState()

tick_engine = TickEngine()
weather_engine = WeatherEngine()
human_engine = HumanEngine()
device_engine = DeviceEngine()
energy_engine = EnergyEngine()
environment_engine = EnvironmentEngine()
sensor_engine = SensorEngine()
export_engine = ExportEngine()
event_engine = EventEngine()
time_engine = TimeEngine()


print("SimuLith Started")

for _ in range(10):

    tick_engine.next_tick(world)
    time_engine.update(world)
    weather_engine.update(world)
    event_engine.update(world)
    human_engine.update(world)
    device_engine.update(world)
    environment_engine.update(world)
    energy_engine.update(world)
    sensor_engine.update(world)
    export_engine.update(world)

    #print(world.weather)
    #print(world.events)
    #print(world.human)
    #print(world.devices)
    #print(world.environment)
    #print(world.energy)
    #print(world.sensors)
    #print(world.human)
    #print("EVENT:", world.events)
  
    time.sleep(0.001)

export_engine.save_csv()