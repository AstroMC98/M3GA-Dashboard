import streamlit as st
from  PIL import Image
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid

from dashboard_pages.landing import get_contents as landing_content
from dashboard_pages.eda import get_contents as data_content
from dashboard_pages.conclusion import get_contents as conclusion_content
from dashboard_pages.methodology import get_contents as methodology_content
from dashboard_pages.recommendations import get_contents as recommendation_content

im = Image.open("images/favicon.ico")
st.set_page_config(
    page_title="Crop Diversity | M3GA",
    page_icon=im,
    layout="wide",
)
st.markdown(
"""
<style>
.css-1siy2j7 {
    background-color: white;
    border-right-style: dashed;
    border-right-color: #266041;
}
</style>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.sidebar.image(f"images/logo.png", use_column_width=True)
    choose = option_menu(None,
                         ["Crop Diversification",
                                   "Our Data",
                                   "Our Approach",
                                   "Conclusions",
                                   "Recommendations"
                                   ],
                         icons=['house', 'boxes', 'diagram-3','card-checklist', 'question-circle'],
                         default_index=2,
                         styles={
                                "container": {
                                            "padding": "5!important",
                                            "background-color": "#FFFFFF"
                                            },
                                "icon": {
                                        "font-size": "25px"
                                        },
                                "icon-selected": {
                                                "color" : "#ffffff"
                                                },
                                "nav-link": {
                                            "font-size": "16px",
                                            "color": "#1D4731",
                                            "text-align": "left",
                                            "margin":"0px",
                                            "--hover-color": "#79AD92",
                                            },
                                "nav-link-selected": {
                                                    "background-color": "#266041",
                                                    "color": "#ffffff",
                                                    },
                                }
    )

if choose == "Crop Diversification":
    landing_content()
elif choose == "Our Data":
    data_content()
elif choose == "Conclusions":
    conclusion_content()
elif choose == "Our Approach":
    methodology_content()
elif choose == "Recommendations":
    recommendation_content()

