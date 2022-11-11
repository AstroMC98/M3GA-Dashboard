import streamlit as st
from  PIL import Image
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid

header_logo = Image.open(r'images/our_conclusions_header.png')

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
        <strong>Conclusion and Scalability</strong></br>
        <p class="openSans">The methodology presented in this project gives a data-backed prioritization of crops. This can give general guidance as to what crops, when to plant, and which regions to plant certain crops to ensure continuous supply within the country. Policy makers can use this tool for crop planning to incentivize farmers to plant diversified crops sporadically to prevent shortages. </p>

        <p class="openSans">Countries who frequently experience increasingly devastating natural calamities can employ this project to strengthen the resilience of their agricultural efforts. This approach can be scaled up for use regionally or globally, or even scaled down to city and town levels to ensure continuity in supply chains, as long as one identifies crops that are produced plentiful in their land and climate at certain times of the year. In scaling, the spatial part of each node is swappable for different levels of granularity which would depend on the available data, and binarization allows different levels of granularity to be compared with one another. </p>

        <p class="openSans">The approach could be extended to other industries as well besides food, like the textile or clothing industry, which rely on national, regional, and global supply chains.</p>

        <p class="openSans">As the application of this approach is used in scaling or expanding, more and more (bigger) data may need to be gathered. Moreover, with the effects of climate change, topographies and data may change, leading to unforeseen events. The uncertainties of these factors need to be taken into consideration in applying this solution to ensure continuity in supply chains of any size.</p>
        """
        st.markdown(f'{project_rationale}', unsafe_allow_html=True)