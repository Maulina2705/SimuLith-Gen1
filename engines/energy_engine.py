class EnergyEngine:

    def update(self, world):

        total_power = 0

        for device_name, device_data in world.devices.items():
            total_power += device_data["power_w"]

        voltage = 220

        total_current = round(total_power / voltage, 2)

        # kWh per menit
        energy_kwh = total_power / 1000 / 60

        # simpan cumulative
        previous_kwh = world.energy.get("total_energy_kwh", 0)

        cumulative_kwh = previous_kwh + energy_kwh

        world.energy = {
            "total_power_w": total_power,
            "total_current_a": total_current,
            "voltage_v": voltage,
            "total_energy_kwh": round(cumulative_kwh, 4)
        }