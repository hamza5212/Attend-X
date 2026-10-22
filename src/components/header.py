import streamlit as st


def header_home():
    st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin:30px 0 40px 0;">
            <svg width="96" height="96" viewBox="0 0 48 48" style="transform:rotate(-6deg); overflow:visible;" role="img" aria-label="Attend-X logo">
                <rect x="4" y="4" width="44" height="44" rx="12" fill="#1A1B3A"/>
                <rect x="0" y="0" width="44" height="44" rx="12" fill="#FFFFFF" stroke="#1A1B3A" stroke-width="2.5"/>
                <g transform="translate(-2 -2)" fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 20V14H20M28 14H34V20M34 28V34H28M20 34H14V28" stroke="#5865F2"/>
                    <path d="M19 24L23 28L30 20" stroke="#EB459E"/>
                </g>
            </svg>
            <h1 style="text-align:center; color:#FFFFFF; margin-top:18px; font-size:clamp(2.6rem, 8vw, 4.8rem) !important; text-shadow:5px 5px 0 #1A1B3A;">ATTEND-X</h1>
        </div>
        """, unsafe_allow_html=True)


def header_dashboard():
    st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; gap:14px; flex-wrap:nowrap;">
            <svg width="64" height="64" viewBox="0 0 48 48" style="transform:rotate(-6deg); overflow:visible; flex-shrink:0;" role="img" aria-label="Attend-X logo">
                <rect x="4" y="4" width="44" height="44" rx="12" fill="#1A1B3A"/>
                <rect x="0" y="0" width="44" height="44" rx="12" fill="#FFFFFF" stroke="#1A1B3A" stroke-width="2.5"/>
                <g transform="translate(-2 -2)" fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 20V14H20M28 14H34V20M34 28V34H28M20 34H14V28" stroke="#5865F2"/>
                    <path d="M19 24L23 28L30 20" stroke="#EB459E"/>
                </g>
            </svg>
            <h2 style="text-align:left; color:#5865F2; white-space:nowrap; margin:0; font-size:1.7rem !important; text-shadow:3px 3px 0 #1A1B3A;">ATTEND-X</h2>
        </div>
        """, unsafe_allow_html=True)