from db import execute_query
import streamlit as st


def render_kpis():

    servers = execute_query("""
    SELECT COUNT(*) total
    FROM dc_operations.gold.dim_server
    """)

    alerts = execute_query("""
    SELECT COUNT(*) total
    FROM dc_operations.gold.fact_alerts
    WHERE fault_detected = true
    """)

    health = execute_query("""
    SELECT ROUND(AVG(health_score),2) avg_health
    FROM dc_operations.gold.fact_maintenance
    """)

    power = execute_query("""
    SELECT ROUND(SUM(power_consumption_kw),2) total_power
    FROM dc_operations.gold.fact_power
    """)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Servers",
        int(servers.iloc[0,0])
    )

    c2.metric(
        "Active Alerts",
        int(alerts.iloc[0,0])
    )

    c3.metric(
        "Avg Health",
        f"{health.iloc[0,0]} %"
    )

    c4.metric(
        "Power (kW)",
        f"{power.iloc[0,0]}"
    )

    st.divider()
