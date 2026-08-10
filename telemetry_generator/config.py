from pathlib import Path


# Project Paths

BASE_DIR = Path(__file__).resolve().parent

DATA_FOLDER = BASE_DIR / "data"
GENERATED_DATA = DATA_FOLDER / "generated"
ARCHIVE_DATA = DATA_FOLDER / "archive"
LOG_FOLDER = BASE_DIR / "logs"

GENERATED_DATA.mkdir(parents=True, exist_ok=True)
ARCHIVE_DATA.mkdir(parents=True, exist_ok=True)
LOG_FOLDER.mkdir(parents=True, exist_ok=True)


# Data Generation Configuration

NUMBER_OF_DEVICES = 500
RECORDS_PER_FILE = 100000


# Manufacturing Plants

PLANTS = [
    "Plant-A",
    "Plant-B",
    "Plant-C",
    "Plant-D"
]

BUILDINGS = [
    "Building-1",
    "Building-2",
    "Building-3"
]

PRODUCTION_LINES = [
    "Line-1",
    "Line-2",
    "Line-3",
    "Line-4",
    "Line-5"
]


# Device Information

DEVICE_TYPES = [
    "Temperature Sensor",
    "Pressure Sensor",
    "Humidity Sensor",
    "Power Meter",
    "Vibration Sensor",
    "Flow Sensor",
    "PLC Controller"
]

MANUFACTURERS = [
    "Siemens",
    "ABB",
    "Schneider Electric",
    "Honeywell",
    "Emerson",
    "Bosch"
]

MODELS = [
    "X100",
    "X200",
    "A500",
    "P300",
    "S900",
    "M700"
]


# Machine Status

STATUSES = [
    "Running",
    "Idle",
    "Stopped",
    "Maintenance"
]

SHIFTS = [
    "Morning",
    "Evening",
    "Night"
]


# Maintenance

ERROR_CODES = [
    "None",
    "TEMP_HIGH",
    "PRESSURE_LOW",
    "POWER_DROP",
    "VIBRATION_HIGH",
    "LOW_BATTERY",
    "NETWORK_FAILURE"
]

WARNING_LEVELS = [
    "Low",
    "Medium",
    "High",
    "Critical"
]


# Sensor Ranges

TEMPERATURE_RANGE = (20.0, 90.0)

HUMIDITY_RANGE = (30.0, 95.0)

PRESSURE_RANGE = (90.0, 160.0)

VIBRATION_RANGE = (0.0, 10.0)

VOLTAGE_RANGE = (210.0, 250.0)

CURRENT_RANGE = (5.0, 50.0)

POWER_FACTOR_RANGE = (0.80, 1.00)

POWER_CONSUMPTION_RANGE = (50.0, 500.0)

ENERGY_KWH_RANGE = (1.0, 100.0)

BATTERY_RANGE = (20, 100)

SIGNAL_STRENGTH_RANGE = (50, 100)

OPERATING_HOURS_RANGE = (100, 10000)

PRODUCTION_COUNT_RANGE = (0, 500)

DOWNTIME_RANGE = (0, 120)


# Output File

OUTPUT_FILENAME = "telemetry_data.json"