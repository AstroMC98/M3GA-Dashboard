import streamlit as st
from  PIL import Image
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid

from dashboard_pages.landing import get_contents as landing_content

st.set_page_config(layout="wide")
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
                                   "How to Scale?",
                                   "FAQs"],
                         icons=['house', 'boxes', 'diagram-3', 'graph-up-arrow','card-checklist', 'question-circle'],
                         default_index=0,
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
# elif choose == "Data Overview":
#     overview_content()
# elif choose == "Skill Analysis":
#     skill_content()
# elif choose == "Emerging Jobs":
#     emerging_content()
# elif choose == "Curriculum Evaluation":
#     compare_content()
# elif choose == "FAQs":
#     faq_content()
