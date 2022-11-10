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
        Crop diversification has been an ongoing strategy by the Department of Agriculture
        because of its benefits such as increased overall production, reduced overdependence on
        importation, and better food security. This falls under the assumption that the more varieties of
        crops a specific area has, the less dependence there is to a particular area and, as such, supply
        shock issues such as typhoons or pestilence caused by the affected area can be avoided. In
        this paper, we used the network theory methodology to find alternative areas and quarters to
        produce a crop. Prior to developing the network, we conducted exploratory data analysis and
        discovered seasonal trends for certain crops which supports the need to identify alternatives
        based on time. In addition, provincial clustering displayed groupings that support our intuition
        that distant areas can have similar traits. Acting on these findings, the network was able to
        return three alternatives for each crop that are not in the same quarter and are far enough to be
        unaffected by the same typhoon. We observed that for four out of the five crops, at least one of
        the three alternatives was a top-5 producer. We can therefore conclude that these
        recommendations are sensible and the rest of the recommendations should be further explored.
        We recommend that the Department of Agriculture build on the results by exploring the crop
        recommendation relationships and assessing the supply chain effects brought about by this
        study
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
