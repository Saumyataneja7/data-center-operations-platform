import random
from datetime import date, timedelta

from config import (
    DEVICE_TYPES,
    MANUFACTURERS,
    MODELS,
    PLANTS,
    BUILDINGS,
    PRODUCTION_LINES
)


class Device:

    def __init__(self, device_number):

        self.device_id = f"DEV-{device_number:05d}"
        self.machine_id = f"MCH-{device_number:05d}"

        self.device_type = random.choice(DEVICE_TYPES)
        self.manufacturer = random.choice(MANUFACTURERS)
        self.model = random.choice(MODELS)

        self.plant = random.choice(PLANTS)
        self.building = random.choice(BUILDINGS)
        self.production_line = random.choice(PRODUCTION_LINES)

        # Random installation date within the last 5 years
        days_back = random.randint(0, 5 * 365)
        self.installation_date = (date.today() - timedelta(days=days_back)).isoformat()