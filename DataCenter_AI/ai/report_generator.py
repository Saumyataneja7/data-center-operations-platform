from db import execute_query
from gemini import ask_gemini


def generate_daily_report():

    maintenance = execute_query("""
        SELECT COUNT(*) AS maintenance_due
        FROM dc_operations.gold.fact_maintenance
        WHERE maintenance_due = true
    """)

    alerts = execute_query("""
        SELECT COUNT(*) AS critical_alerts
        FROM dc_operations.gold.fact_alerts
        WHERE fault_detected = true
    """)

    health = execute_query("""
        SELECT AVG(health_score) AS avg_health
        FROM dc_operations.gold.fact_maintenance
    """)

    power = execute_query("""
        SELECT SUM(power_consumption_kw) AS total_power
        FROM dc_operations.gold.fact_power
    """)

    prompt = f"""
You are a Senior Data Center Operations Manager.

Using the following metrics, generate a professional Daily Operations Report.

Maintenance:
{maintenance.to_string(index=False)}

Alerts:
{alerts.to_string(index=False)}

Health:
{health.to_string(index=False)}

Power:
{power.to_string(index=False)}

Write the report with:

1. Executive Summary
2. Critical Findings
3. Recommendations

Keep it under 300 words.
"""

    return ask_gemini(prompt)