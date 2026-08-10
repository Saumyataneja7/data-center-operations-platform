import json
import random
import uuid
from pathlib import Path
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "telemetry_data.json"

NUM_DEVICES = 500
RECORDS = 100000

PLANTS = ["Plant-A","Plant-B","Plant-C","Plant-D"]
BUILDINGS = ["Building-1","Building-2","Building-3"]
LINES = ["Line-1","Line-2","Line-3","Line-4","Line-5"]
DEVICE_TYPES = ["Temperature Sensor","Pressure Sensor","Humidity Sensor","Power Meter","PLC Controller"]
MANUFACTURERS = ["Siemens","ABB","Honeywell","Bosch","Schneider"]
STATUSES = ["Running","Idle","Stopped","Maintenance"]
SHIFTS = ["Morning","Evening","Night"]

devices=[]
for i in range(1,NUM_DEVICES+1):
    devices.append({
        "device_id":f"DEV-{i:05d}",
        "machine_id":f"MCH-{i:05d}",
        "device_type":random.choice(DEVICE_TYPES),
        "manufacturer":random.choice(MANUFACTURERS),
        "model":f"M-{random.randint(100,999)}",
        "plant":random.choice(PLANTS),
        "building":random.choice(BUILDINGS),
        "production_line":random.choice(LINES),
        "installation_date":(datetime.now()-timedelta(days=random.randint(30,1800))).date().isoformat()
    })

start=datetime.now()-timedelta(days=30)
seconds=int((datetime.now()-start).total_seconds())

records=[]

def inject_quality_issues(r):
    p=random.random()
    if p<0.02:
        r["temperature"]=None
    elif p<0.04:
        r["humidity"]=150
    elif p<0.05:
        r["voltage"]=600
    elif p<0.06:
        r["device_id"]=None
    elif p<0.07:
        r["power_consumption_kw"]=-20
    elif p<0.08:
        r["event_timestamp"]=(datetime.now()+timedelta(days=5)).isoformat()
    elif p<0.09:
        r["battery_level"]=150
    elif p<0.10:
        r["plant"]="Plant-X"
    return r

for i in range(RECORDS):

    if i % 10000 == 0:
        print(f"Generating {i:,}/{RECORDS:,} records...")

    d=random.choice(devices)
    ts=start+timedelta(seconds=random.randint(0,seconds))
    status=random.choice(STATUSES)

    if status=="Running":
        production=random.randint(120,500)
        downtime=0
        power=random.uniform(120,450)
        due=False
    elif status=="Idle":
        production=0
        downtime=random.randint(5,30)
        power=random.uniform(20,80)
        due=False
    elif status=="Stopped":
        production=0
        downtime=random.randint(30,120)
        power=random.uniform(0,15)
        due=False
    else:
        production=0
        downtime=random.randint(60,180)
        power=random.uniform(5,25)
        due=True

    temp=round(random.uniform(20,90),2)
    vib=round(random.uniform(0,10),2)

    warn="Low"
    err="None"

    if temp>75 or vib>8:
        warn="High"
        err="TEMP_HIGH"

    record={
        "event_id":str(uuid.uuid4()),
        "event_timestamp":ts.isoformat(),
        **d,
        "shift":random.choice(SHIFTS),
        "machine_status":status,
        "production_count":production,
        "downtime_minutes":downtime,
        "temperature":temp,
        "humidity":round(random.uniform(30,95),2),
        "pressure":round(random.uniform(90,160),2),
        "vibration":vib,
        "voltage":round(random.uniform(210,250),2),
        "current":round(random.uniform(5,50),2),
        "power_factor":round(random.uniform(0.8,1.0),2),
        "power_consumption_kw":round(power,2),
        "energy_kwh":round(random.uniform(1,100),2),
        "battery_level":random.randint(20,100),
        "signal_strength":random.randint(50,100),
        "operating_hours":random.randint(100,10000),
        "maintenance_due":due,
        "warning_level":warn,
        "error_code":err
    }

    records.append(inject_quality_issues(record))

# duplicates
records.extend(random.sample(records,int(len(records)*0.02)))

# overheating
for _ in range(300):
    r=random.choice(records)
    r["temperature"]=random.randint(90,120)
    r["vibration"]=round(random.uniform(12,20),2)
    r["warning_level"]="Critical"
    r["maintenance_due"]=True
    r["error_code"]="OVERHEATING"

# power spikes
for _ in range(200):
    r=random.choice(records)
    r["power_consumption_kw"]=random.randint(700,1000)
    r["error_code"]="POWER_SPIKE"

# sensor failures
for _ in range(200):
    r=random.choice(records)
    r["temperature"]=None
    r["humidity"]=None
    r["pressure"]=None
    r["error_code"]="SENSOR_FAILURE"

records.sort(key=lambda x:x["event_timestamp"])

with open(OUTPUT_FILE,"w",encoding="utf-8") as f:
    json.dump(records,f,indent=4,ensure_ascii=False)

print("Telemetry Generation Completed")
print(f"Total Records : {len(records):,}")
print(f"Devices       : {NUM_DEVICES}")
print(f"Output File   : {OUTPUT_FILE}")