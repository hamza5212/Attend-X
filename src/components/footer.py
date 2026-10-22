import streamlit as st


def footer_home():
    st.markdown(
        """
        <div style="text-align:center; margin-top:2.5rem;">
            <span style="display:inline-block; background:#1A1B3A; color:#FFFFFF; font-size:0.95rem; padding:0.5rem 1.2rem; border-radius:999px; transform:rotate(-1.5deg);">
                Attend-X • Smart attendance for modern classrooms
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    st.markdown(
        """
        <div style="text-align: center; color: #5865F2; margin-top: 2rem; font-size: 0.9rem;">
            Attend-X • Smart attendance for modern classrooms
        </div>
        """,
        unsafe_allow_html=True,
    )