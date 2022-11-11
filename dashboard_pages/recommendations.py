import streamlit as st
from  PIL import Image
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid

header_logo = Image.open(r'images/our_recommendations_header.png')

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
        
    innerrow1_outer1, mid_space, innerrow1_outer2 = st.columns((.125, 0.75, .125))
    with mid_space:
        
        metho_img = Image.open(r'images/recos_img.png')
        st.image(metho_img, width = 800)
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.markdown(hide_img_fs, unsafe_allow_html=True)
    
        