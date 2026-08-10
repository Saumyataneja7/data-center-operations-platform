import random

from config import (
    TEMPERATURE_RANGE,
    HUMIDITY_RANGE,
    PRESSURE_RANGE,
    VIBRATION_RANGE,
    VOLTAGE_RANGE,
    CURRENT_RANGE,
    POWER_FACTOR_RANGE,
    POWER_CONSUMPTION_RANGE,
    ENERGY_KWH_RANGE,
    BATTERY_RANGE,
    SIGNAL_STRENGTH_RANGE,
    OPERATING_HOURS_RANGE,
    PRODUCTION_COUNT_RANGE,
    DOWNTIME_RANGE,
    ERROR_CODES,
    WARNING_LEVELS,
    STATUSES,
    SHIFTS
)


class Sensor:

    @staticmethod
    def temperature():
        return round(random.uniform(*TEMPERATURE_RANGE), 2)

    @staticmethod
    def humidity():
        return round(random.uniform(*HUMIDITY_RANGE), 2)

    @staticmethod
    def pressure():
        return round(random.uniform(*PRESSURE_RANGE), 2)

    @staticmethod
    def vibration():
        return round(random.uniform(*VIBRATION_RANGE), 2)

    @staticmethod
    def voltage():
        return round(random.uniform(*VOLTAGE_RANGE), 2)

    @staticmethod
    def current():
        return round(random.uniform(*CURRENT_RANGE), 2)

    @staticmethod
    def power_factor():
        return round(random.uniform(*POWER_FACTOR_RANGE), 2)

    @staticmethod
    def power_consumption():
        return round(random.uniform(*POWER_CONSUMPTION_RANGE), 2)

    @staticmethod
    def energy_kwh():
        return round(random.uniform(*ENERGY_KWH_RANGE), 2)

    @staticmethod
    def battery_level():
        return random.randint(*BATTERY_RANGE)

    @staticmethod
    def signal_strength():
        return random.randint(*SIGNAL_STRENGTH_RANGE)

    @staticmethod
    def operating_hours():
        return random.randint(*OPERATING_HOURS_RANGE)

    @staticmethod
    def production_count():
        return random.randint(*PRODUCTION_COUNT_RANGE)

    @staticmethod
    def downtime_minutes():
        return random.randint(*DOWNTIME_RANGE)

    @staticmethod
    def machine_status():
        return random.choice(STATUSES)

    @staticmethod
    def shift():
        return random.choice(SHIFTS)

    @staticmethod
    def maintenance_due():
        return random.choice([True, False])

    @staticmethod
    def error_code():
        return random.choice(ERROR_CODES)

    @staticmethod
    def warning_level():
        return random.choice(WARNING_LEVELS)