import json
import random
import uuid
from pathlib import Path
from datetime import datetime, timedelta

# Configuration

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "telemetry_data.json"

NUM_DEVICES = 500
RECORDS = 100000

PLANTS = ["Plant-A", "Plant-B", "Plant-C", "Plant-D"]

BUILDINGS = [
    "Building-1",
    "Building-2",
    "Building-3"
]

LINES = [
    "Line-1",
    "Line-2",
    "Line-3",
    "Line-4",
    "Line-5"
]

DEVICE_TYPES = [
    "Temperature Sensor",
    "Pressure Sensor",
    "Humidity Sensor",
    "Power Meter",
    "PLC Controller"
]

MANUFACTURERS = [
    "Siemens",
    "ABB",
    "Honeywell",
    "Bosch",
    "Schneider"
]

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

# Device Master

devices = []

for i in range(1, NUM_DEVICES + 1):

    devices.append({

        "device_id": f"DEV-{i:05d}",

        "machine_id": f"MCH-{i:05d}",

        "device_type": random.choice(DEVICE_TYPES),

        "manufacturer": random.choice(MANUFACTURERS),

        "model": f"M-{random.randint(100,999)}",

        "plant": random.choice(PLANTS),

        "building": random.choice(BUILDINGS),

        "production_line": random.choice(LINES),

        "installation_date": (
            datetime.now()
            - timedelta(days=random.randint(30, 1800))
        ).date().isoformat()

    })

# Time Window

start = datetime.now() - timedelta(days=30)

seconds = int((datetime.now() - start).total_seconds())

records = []

# Data Quality Issues

def inject_quality_issues(record):

    p = random.random()

    if p < 0.02:
        record["temperature"] = None

    elif p < 0.04:
        record["humidity"] = 150

    elif p < 0.05:
        record["voltage"] = 600

    elif p < 0.06:
        record["device_id"] = None

    elif p < 0.07:
        record["power_consumption_kw"] = -20

    elif p < 0.08:
        record["event_timestamp"] = (
            datetime.now()
            + timedelta(days=5)
        ).isoformat()

    elif p < 0.09:
        record["battery_level"] = 150

    elif p < 0.10:
        record["plant"] = "Plant-X"

    return record

# Generate Telemetry

for i in range(RECORDS):

    if i % 10000 == 0:
        print(f"Generating {i:,}/{RECORDS:,}")

    d = random.choice(devices)

    ts = start + timedelta(seconds=random.randint(0, seconds))

    status = random.choices(
        population=["Running", "Idle", "Stopped", "Maintenance"],
        weights=[90, 6, 3, 1],
        k=1
    )[0]

    # Machine Operating State

    if status == "Running":

        production = random.randint(120, 500)

        downtime = 0

        power = random.uniform(120, 300)

        due = False

    elif status == "Idle":

        production = 0

        downtime = random.randint(1, 10)

        power = random.uniform(20, 60)

        due = False

    elif status == "Stopped":

        production = 0

        downtime = random.randint(10, 40)

        power = random.uniform(0, 8)

        due = False

    else:  # Maintenance

        production = 0

        downtime = random.randint(30, 120)

        power = random.uniform(5, 20)

        due = True

    # Controlled Anomaly Injection (≈4%)

    is_anomaly = random.random() < 0.04

    if is_anomaly:

        anomaly = random.choice([
            "OVERHEATING",
            "POWER_SPIKE",
            "PRESSURE_HIGH",
            "LOW_VOLTAGE",
            "HIGH_VIBRATION"
        ])

        if anomaly == "OVERHEATING":

            temp = round(random.uniform(38, 48), 2)

            vib = round(random.uniform(5, 8), 2)

            pressure = round(random.uniform(2.5, 3.2), 2)

            voltage = round(random.uniform(225, 235), 2)

            current = round(random.uniform(35, 50), 2)

            power = round(random.uniform(350, 500), 2)

            humidity = round(random.uniform(45, 60), 2)

            downtime = random.randint(20, 90)

            warn = "Critical"

            err = "OVERHEATING"

        elif anomaly == "POWER_SPIKE":

            temp = round(random.uniform(27, 33), 2)

            vib = round(random.uniform(1.0, 2.5), 2)

            pressure = round(random.uniform(2.0, 2.5), 2)

            voltage = round(random.uniform(245, 255), 2)

            current = round(random.uniform(45, 60), 2)

            power = round(random.uniform(600, 850), 2)

            humidity = round(random.uniform(40, 55), 2)

            warn = "High"

            err = "POWER_SPIKE"

        elif anomaly == "PRESSURE_HIGH":

            temp = round(random.uniform(28, 32), 2)

            vib = round(random.uniform(1.0, 2.5), 2)

            pressure = round(random.uniform(4.2, 5.5), 2)

            voltage = round(random.uniform(225, 235), 2)

            current = round(random.uniform(20, 30), 2)

            power = round(random.uniform(180, 260), 2)

            humidity = round(random.uniform(45, 60), 2)

            warn = "Medium"

            err = "PRESSURE_HIGH"

        elif anomaly == "LOW_VOLTAGE":

            temp = round(random.uniform(25, 30), 2)

            vib = round(random.uniform(0.5, 2.0), 2)

            pressure = round(random.uniform(2.0, 2.5), 2)

            voltage = round(random.uniform(180, 205), 2)

            current = round(random.uniform(15, 25), 2)

            power = round(random.uniform(150, 250), 2)

            humidity = round(random.uniform(40, 55), 2)

            warn = "Medium"

            err = "LOW_VOLTAGE"

        else:

            temp = round(random.uniform(28, 34), 2)

            vib = round(random.uniform(6, 10), 2)

            pressure = round(random.uniform(2.0, 2.8), 2)

            voltage = round(random.uniform(225, 235), 2)

            current = round(random.uniform(18, 28), 2)

            power = round(random.uniform(180, 260), 2)

            humidity = round(random.uniform(40, 55), 2)

            warn = "High"

            err = "HIGH_VIBRATION"

    else:

        temp = round(random.uniform(22, 30), 2)

        vib = round(random.uniform(0.2, 2.0), 2)

        pressure = round(random.uniform(2.0, 2.8), 2)

        voltage = round(random.uniform(225, 235), 2)

        current = round(random.uniform(10, 30), 2)

        humidity = round(random.uniform(40, 60), 2)

        power = round(power, 2)

        warn = "Low"

        err = "None"

    record = {

        "event_id": str(uuid.uuid4()),

        "event_timestamp": ts.isoformat(),

        **d,

        "shift": random.choice(SHIFTS),

        "machine_status": status,

        "production_count": production,

        "downtime_minutes": downtime,

        "temperature": temp,

        "humidity": humidity,

        "pressure": pressure,

        "vibration": vib,

        "voltage": voltage,

        "current": current,

        "power_factor": round(random.uniform(0.90, 1.00), 2),

        "power_consumption_kw": round(power, 2),

        "energy_kwh": round(power * random.uniform(0.7, 1.2), 2),

        "battery_level": random.randint(60, 100),

        "signal_strength": random.randint(70, 100),

        "operating_hours": random.randint(100, 10000),

        "maintenance_due": due,

        "warning_level": warn,

        "error_code": err

    }

    records.append(inject_quality_issues(record))

# Duplicate Records (~2%)

records.extend(
    random.sample(
        records,
        int(len(records) * 0.02)
    )
)

# Sensor Failure Injection

for _ in range(200):

    r = random.choice(records)

    r["temperature"] = None

    r["humidity"] = None

    r["pressure"] = None

    r["error_code"] = "SENSOR_FAILURE"

    r["warning_level"] = "High"

# Sort

records.sort(key=lambda x: x["event_timestamp"])

# Write JSON

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        records,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nTelemetry Generation Completed")
print(f"Total Records : {len(records):,}")
print(f"Devices       : {NUM_DEVICES}")
print(f"Output File   : {OUTPUT_FILE}")