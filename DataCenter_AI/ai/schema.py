DATABASE_SCHEMA = """
Database Name:
dc_operations

Schema:
gold

Tables:

dim_server
------------
server_key
machine_id
device_id
device_type
manufacturer
model
installation_date

dim_datacenter
------------
datacenter_key
plant
building
production_line

dim_date
------------
date_key
date
day
month
month_name
quarter
year
week
day_name

fact_telemetry
------------
event_id
server_key
datacenter_key
date_key
event_timestamp
battery_level
signal_strength
operating_hours
production_count

fact_power
------------
event_id
server_key
datacenter_key
date_key
event_timestamp
voltage
current
power_consumption_kw
energy_kwh
power_factor

fact_environment
------------
event_id
server_key
datacenter_key
date_key
event_timestamp
temperature
humidity
pressure
vibration

fact_alerts
------------
event_id
server_key
datacenter_key
date_key
event_timestamp
error_code
warning_level
fault_type
fault_severity
fault_detected
health_status

fact_maintenance
------------
event_id
server_key
datacenter_key
date_key
event_timestamp
maintenance_due
downtime_minutes
maintenance_priority
health_score
efficiency_score
energy_efficiency
"""