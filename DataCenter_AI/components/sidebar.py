import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/server.png",
            width=70
        )

        st.title("Data Center AI")

        st.caption("Enterprise Operations Copilot")

        st.divider()

        clear_chat = st.button(
            "🗑 Clear Chat",
            use_container_width=True
        )

        generate_report = st.button(
            "📄 Daily AI Report",
            use_container_width=True
        )

        st.divider()

        st.subheader("Technology Stack")

        st.markdown("""
            - Azure Data Factory
            - Azure Databricks
            - Unity Catalog
            - SQL Warehouse
            - Streamlit
            - Gemini 3.6 Flash
        """)

        return clear_chat, generate_report