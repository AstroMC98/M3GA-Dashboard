import streamlit as st
from PIL import Image
import plotly.figure_factory as ff
import plotly.graph_objects as go
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

# -------------- LAYOUT --------------------
header_logo = Image.open(r'images/our_data_header.png')

def get_contents():
    col1_space1, col1_1, col1_space1, = st.columns([0.1, 0.8, 0.1])
    with col1_1:
        st.image(header_logo, width = 400)
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.markdown(hide_img_fs, unsafe_allow_html=True)
        
    row1_spacer1, row1_1, row1_spacer2 = st.columns((.105, 0.8, .1))
    with row1_1:
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@350&display=swap');

        .openSans {
        font-size:14px ;
        font-family: 'Open Sans', sans-serif;
        color: #000000;
        line-height: 2;
        }
        </style> """, unsafe_allow_html=True)
        text_content ="""
        There are two data sources used for this project, all of which are from publicly available sources:
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
    innerrow1_outer1, left_col, mid_space ,right_col, innerrow1_outer2 = st.columns((.125, 0.3, 0.05, 0.3 , .125))
    with left_col:
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@350&display=swap');

        .openSans {
        font-size:14px ;
        font-family: 'Open Sans', sans-serif;
        color: #266041;
        line-height: 2;
        }
        </style> """, unsafe_allow_html=True)
        text_content ="""
        
        """
        st.markdown("""
                    <p class="openSans"><strong>Other Crops : Volume of Production by Region and by Province, by Quarter and Semester, 2010-2020</strong></p>
                    <hr style="height:0.5px; border-style:solid; color:#266041; background-color:#266041" />
                    <a class="openSans" style = "font-size:11px" href = "https://openstat.psa.gov.ph/Metadata/2E4EVCP1"> From Philippines Statistics Authority OpenStat portal </a>
                    """,
                    unsafe_allow_html=True)
        

    with right_col:
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@350&display=swap');

        .openSans {
        font-size:14px ;
        font-family: 'Open Sans', sans-serif;
        color: #266041;
        line-height: 2;
        }
        </style> """, unsafe_allow_html=True)
        text_content ="""
        
        """
        st.markdown("""
                    <p class="openSans"><strong>Food Prices data for Philippines, by Region and by Province, 2000-2022</strong></p>
                    <hr style="height:0.5px; border-style:solid; color:#266041; background-color:#266041" />
                    <a class="openSans" style = "font-size:11px" href = "https://data.humdata.org/dataset/wfp-food-prices-for-philippines"> From World Food Programme Price Database </a>
                    """,
                    unsafe_allow_html=True)
        
    row1_spacer3, row3_3, row3_spacer2 = st.columns((.105, 0.8, .1))
    with row3_3:
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@350&display=swap');

        .openSans {
        font-size:14px ;
        font-family: 'Open Sans', sans-serif;
        color: #000000;
        line-height: 2;
        }
        </style> """, unsafe_allow_html=True)
        text_content ="""
        The price of goods in the Philippines have steadily increased over the years. In the advent of global warming and natural disasters, the retail prices of crops have frequently fluctuated in response. 
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
        
# The Price of Goods in the Philippines have steadily increased over the years. In the advent of global warming and natural disasters, the retail prices of crops have frequently fluctuated in response. 
#     # <Viz for prices>
    
# An example of this is how the price of Garlic simply responds to the available supply of Garlic in the country. Whereas, low supply of Garlic coincided with high prices. In the same manner, Garlic prices dropped when supply went up.  
#     # <Viz of garlic supply>

# Our team, M3GA, hopes to address this specific issue by optimizing the agricultural supply chain through crop diversification. As of now, there are certain crops that highly concentrated in one location in a specific quarter which in turn results in lower prices at that location for that specific crop but higher prices for other locations. 
#     # <Choropleths>

# Considering the potential disruption in the agricultural value chain when natural disasters occur for regionally-concentrated crops, there is value in diversifying the types of crops planted across regions. 