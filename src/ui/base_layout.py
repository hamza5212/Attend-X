import streamlit as st


def style_background_home():

    st.markdown("""
        <style>
        .stApp {
            background-color: #5865F2 !important;
            background-image: radial-gradient(rgba(255,255,255,0.22) 1.5px, transparent 1.5px) !important;
            background-size: 26px 26px !important;
        }
        .stApp div[data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            padding: 2.2rem !important;
            border: 4px solid #1A1B3A !important;
            border-radius: 2.5rem !important;
            box-shadow: 10px 10px 0 #1A1B3A !important;
            transform: rotate(-1.2deg);
            transition: transform 0.25s ease, box-shadow 0.25s ease !important;
        }
        .stApp div[data-testid="stColumn"]:nth-child(2) {
            background-color: #FFD9EC !important;
            transform: rotate(1.2deg);
        }
        .stApp div[data-testid="stColumn"]:hover {
            transform: translate(-4px, -4px) rotate(0deg);
            box-shadow: 14px 14px 0 #1A1B3A !important;
        }
        .stApp div[data-testid="stColumn"] h2 {
            color: #1A1B3A !important;
        }
        .stApp div[data-testid="stColumn"] img {
            transition: transform 0.3s ease;
        }
        .stApp div[data-testid="stColumn"]:hover img {
            transform: rotate(-5deg) scale(1.06);
        }
        .stApp div[data-testid="stColumn"] button {
            background-color: #1A1B3A !important;
            color: #FFFFFF !important;
            border-radius: 999px !important;
            box-shadow: 4px 4px 0 #5865F2 !important;
            transition: transform 0.15s, box-shadow 0.15s !important;
        }
        .stApp div[data-testid="stColumn"] button:hover {
            transform: translate(2px, 2px) !important;
            box-shadow: 2px 2px 0 #5865F2 !important;
        }
        .stApp div[data-testid="stColumn"] button:active {
            transform: translate(4px, 4px) !important;
            box-shadow: 0 0 0 #5865F2 !important;
        }
        @media (max-width: 640px) {
            .stApp div[data-testid="stColumn"] {
                padding: 1.5rem !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>
        .stApp {
            background-color: #E0E3FF !important;
            background-image: radial-gradient(rgba(88,101,242,0.18) 1.5px, transparent 1.5px) !important;
            background-size: 26px 26px !important;
        }

        /* dark readable text on the light background (main page area only) */
        [data-testid="stMain"] [data-testid="stHeading"],
        [data-testid="stMain"] [data-testid="stHeading"] *,
        section.main [data-testid="stHeading"],
        section.main [data-testid="stHeading"] * {
            color: #1A1B3A !important;
        }
        [data-testid="stMain"] [data-testid="stWidgetLabel"] *,
        [data-testid="stMain"] [data-testid="stCaptionContainer"] *,
        section.main [data-testid="stWidgetLabel"] *,
        section.main [data-testid="stCaptionContainer"] * {
            color: #1A1B3A !important;
        }
        [data-testid="stMain"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stMain"] [data-testid="stMarkdownContainer"] li,
        section.main [data-testid="stMarkdownContainer"] p,
        section.main [data-testid="stMarkdownContainer"] li {
            color: #1A1B3A;
        }

        /* chunky sticker buttons */
        [data-testid="stMain"] [data-testid="stButton"] button,
        [data-testid="stMain"] [data-testid="stFormSubmitButton"] button,
        [data-testid="stDialog"] [data-testid="stButton"] button {
            border: 3px solid #1A1B3A !important;
            border-radius: 999px !important;
            box-shadow: 4px 4px 0 #1A1B3A !important;
            transition: transform 0.15s, box-shadow 0.15s !important;
        }
        [data-testid="stMain"] [data-testid="stButton"] button:hover,
        [data-testid="stMain"] [data-testid="stFormSubmitButton"] button:hover,
        [data-testid="stDialog"] [data-testid="stButton"] button:hover {
            transform: translate(2px, 2px) !important;
            box-shadow: 2px 2px 0 #1A1B3A !important;
        }
        [data-testid="stMain"] [data-testid="stButton"] button:active,
        [data-testid="stMain"] [data-testid="stFormSubmitButton"] button:active,
        [data-testid="stDialog"] [data-testid="stButton"] button:active {
            transform: translate(4px, 4px) !important;
            box-shadow: 0 0 0 #1A1B3A !important;
        }

        /* inputs, camera, tables, popups */
        [data-testid="stMain"] [data-baseweb="input"] {
            border: 2px solid #1A1B3A !important;
            border-radius: 1rem !important;
        }
        [data-testid="stCameraInput"] video {
            border-radius: 1.5rem !important;
        }
        [data-testid="stDataFrame"] {
            border: 3px solid #1A1B3A;
            border-radius: 1rem;
            overflow: hidden;
        }
        div[role="dialog"] {
            border: 4px solid #1A1B3A !important;
            border-radius: 2rem !important;
            box-shadow: 10px 10px 0 #1A1B3A !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    # asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

         /* Hide Top Bar of streamlit */
            #MainMenu, footer, header {
                visibility: hidden;
            }
            .block-container {
                padding-top:1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
            h3, h4, p {
                font-family: 'Outfit', sans-serif;
            }

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>

                """
                , unsafe_allow_html=True)