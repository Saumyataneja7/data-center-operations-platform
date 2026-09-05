import streamlit as st


def render():

    st.subheader("Quick Questions")

    c1, c2 = st.columns(2)

    question = None

    with c1:

        if st.button(
            "🔧 Servers requiring maintenance",
            use_container_width=True
        ):
            question = "Which servers require maintenance?"

        if st.button(
            "⚡ Highest power consumption",
            use_container_width=True
        ):
            question = "Show highest power consumption."

    with c2:

        if st.button(
            "🚨 Critical alerts today",
            use_container_width=True
        ):
            question = "Show today's critical alerts."

        if st.button(
            "📉 Lowest health score",
            use_container_width=True
        ):
            question = "Show lowest health score servers."

    return question