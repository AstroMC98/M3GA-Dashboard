import streamlit as st
from  PIL import Image
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid

logo = Image.open(r'images/project-logo.png')

def get_contents():
    col1_space1, col1_1, col1_space1, = st.columns([0.05, 0.8, 0.15])
    with col1_1:
        st.image(logo, use_column_width = 'always')
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.markdown(hide_img_fs, unsafe_allow_html=True)
            
    col3_space1, col3_1, col3_space1, = st.columns([0.15, 0.7, 0.15])
    with col3_1:
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@350&display=swap');

        .openSans {
        font-size:13px ;
        font-family: 'Open Sans', sans-serif;
        color: #000000;
        line-height: 2;
        border-style: dotted;
        border-color: #266041;
        border-width: 0.25px;
        padding : 10px
        }
        </style> """, unsafe_allow_html=True)
        project_rationale ="""
        <strong>Project Rationale</strong></br>
        In a country constantly ravaged by typhoons,
        which in recent years have increased in intensity because of climate change,
        food security becomes all the more a pressing issue.
        These natural disasters, when they make landfall,
        lay waste to plantations of crops that feed the nation,
        causing tons of food to go to waste and leading to an increased demand and prices for a decreased supply.</br></br>This project seeks to use data science,
        specifically network science, 
        to help policymakers manage crop supply in the country through crop diversification.
        This involves planting crops in areas similar to each other but geographically distant,
        so that typhoons and other natural calamities do not cripple supply especially of essential goods.</br></br>This project is envisioned be scalable to include other countries in the region and the world,
        ensuring the robustness of global value chains not only for agriculture but for other industries
        that have cross-border movement of goods and services.
        """
        st.markdown(f'<p class="openSans">{project_rationale}</p>', unsafe_allow_html=True)

    col2_space1, col2_1, col2_space2 = st.columns([0.35, 0.3, 0.35])
    with col2_1:
        st.markdown("""
        <style>
        .button {
        position: relative;
        background-color: #266041;
        border: none;
        color: white;
        padding: 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 2px 2px;
        font-weight: bold;
        }
        a:link{color:white;}
        a:visited{color:white;}
        a:hover{color:white;}
        a:focus{color:white;}
        a:active{color:white;}

        .button-circle {border-radius: 30px;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<a href="https://drive.google.com/file/d/1Q13vDqy4wxeH4Xw2IizTREKlhdH2raW3/view?usp=sharing" class="button button-circle">Link to Project Presentation</a>', unsafe_allow_html = True)
