import streamlit as st
from PIL import Image
import plotly.figure_factory as ff
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import networkx as nx
import itertools
import geopandas as gpd
from shapely.wkt import loads
import seaborn as sns
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
        
    row1_spacer1, row1_1, row1_spacer2 = st.columns((.125, 0.75, .125))
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
        
    innerrow1_outer1, mid_space, innerrow1_outer2 = st.columns((.125, 0.75, .125))
    with mid_space:
        st.markdown('---')

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
        
        
        df = pd.read_csv('data/processed/wfp_food_prices_phl.csv')
        df = df.iloc[1:,:]
        df['date'] = pd.to_datetime(df['date'])
        df['price'] = df.price.apply(lambda x: str(x).split('.')[0])
        df['price'] = pd.to_numeric(df["price"], downcast="float")
        df = df[df.pricetype == 'Retail']
        df = df[['date', 'market', 'commodity', 'price']]
        
        unique_items = sorted(df.commodity.unique().tolist())
        crop_selected = st.selectbox('Select commodity to plot', unique_items, index = 0)
        prices = df[df.commodity==crop_selected]
        
        fig, ax = plt.subplots()
        prices.groupby([prices['date'].dt.date]).price.mean().plot(figsize=(20,4), ax = ax)
        ax.set_title(crop_selected)
        ax.set_ylabel('Price (in Php)')
        ax.set_ylim(bottom=0)
        st.pyplot(fig)
        
        st.markdown('---')
        
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
        text_content2 ="""
        An example of this is how the price of Garlic simply responds to the available supply of Garlic in the country. Whereas, low supply of Garlic coincided with high prices. In the same manner, Garlic prices dropped when supply went up.        """
        st.markdown(f'<p class="openSans">{text_content2}</p>', unsafe_allow_html=True)
        
        garlic_pic = Image.open(r'images/garlic_submission.png')
        st.image(garlic_pic, use_column_width=True)
        hide_img_fs2 = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.markdown(hide_img_fs2, unsafe_allow_html=True)
        
        
        st.markdown('---')
        
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
        text_content3 ="""
        Our team, M3GA, hopes to address this specific issue by optimizing the agricultural supply chain through crop diversification. As of now, there are certain crops that highly concentrated in one location in a specific quarter which in turn results in lower prices at that location for that specific crop but higher prices for other locations. 
        """
        st.markdown(f'<p class="openSans">{text_content3}</p>', unsafe_allow_html=True)
        
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
        
        df_chloro = pd.read_csv('data/processed/crop_volume_long_form.csv')
        unique_crop = sorted(df_chloro.Crop.unique().tolist())
        crop_selected = st.selectbox('Select Crop to explore', unique_crop, index = 0)
        def crop_plotter(crop = 'Calamansi'):
            
            psgc = pd.read_csv('data/raw/psgc.csv')
            psgc['geometry'] = psgc.geometry.map(loads)
            psgc = gpd.GeoDataFrame(psgc)
            psgc = psgc.dissolve(by='region')[['geometry']]
            psgc.crs = 'EPSG:4326'
            psgc = psgc.to_crs('EPSG:32651')
            psgc['name'] = psgc.index.map({
                'AUTONOMOUS REGION IN MUSLIM MINDANAO (ARMM)': 'AUTONOMOUS REGION IN MUSLIM MINDANAO',
                'REGION XIII (Caraga)': 'REGION XIII (CARAGA)'})
            psgc.index = psgc['name'].combine_first(pd.Series(psgc.index, psgc.index))
            del psgc['name']
            psgc = psgc.simplify(200)
            
            df = pd.read_csv('data/processed/crop_volume_long_form.csv')
            df = df[df.Level=='R']
            df = df.groupby(['Crop', 'geoloc_quarter'], as_index=False).percent_production.mean()
            df['geoloc'] = df.geoloc_quarter.str.split('_').str[0]
            df['quarter'] = df.geoloc_quarter.str.split('_').str[1]
            del df['geoloc_quarter']
            df = df[['Crop', 'geoloc', 'quarter', 'percent_production']]
            
            df_chloro = df.copy()
            
        
            df2 = df_chloro[df_chloro.Crop==crop]
            df2 = df2.join(psgc.to_frame(name='geometry'), on='geoloc', how='left')
            df2 = gpd.GeoDataFrame(df2)

            fig, axes = plt.subplots(1, 4, figsize=(20, 10), dpi=240)
            for quarter in range(1,5):
                ax = axes[quarter-1]
                quarter = f'Q{quarter}'
                df2[df2.quarter==quarter].plot(column='percent_production', ax=ax, edgecolor='#222', vmin=0, vmax=0.1, cmap='OrRd')
                ax.set_axis_off()
                ax.set_title(quarter, fontsize=20, fontweight='bold')
            plt.suptitle(crop, fontsize=24, fontweight='bold')
            plt.tight_layout()
            
            return fig
        
        def crop_plotter2(crop = 'Calamansi'):
            
            psgc = pd.read_csv('data/raw/psgc.csv')
            psgc['geometry'] = psgc.geometry.map(loads)
            psgc = gpd.GeoDataFrame(psgc)
            psgc = psgc.dissolve(by='region')[['geometry']]
            psgc.crs = 'EPSG:4326'
            psgc = psgc.to_crs('EPSG:32651')
            psgc['name'] = psgc.index.map({
                'AUTONOMOUS REGION IN MUSLIM MINDANAO (ARMM)': 'AUTONOMOUS REGION IN MUSLIM MINDANAO',
                'REGION XIII (Caraga)': 'REGION XIII (CARAGA)'})
            psgc.index = psgc['name'].combine_first(pd.Series(psgc.index, psgc.index))
            del psgc['name']
            psgc = psgc.simplify(200)
            
            df = pd.read_csv('data/processed/crop_volume_long_form.csv')
            df = df[df.Level=='R']
            df = df.groupby(['Crop', 'geoloc_quarter'], as_index=False).percent_production.mean()
            df['geoloc'] = df.geoloc_quarter.str.split('_').str[0]
            df['quarter'] = df.geoloc_quarter.str.split('_').str[1]
            del df['geoloc_quarter']
            df = df[['Crop', 'geoloc', 'quarter', 'percent_production']]
            
            df_chloro = df.copy()
            
        
            df2 = df_chloro[df_chloro.Crop==crop]
            df2 = df2.join(psgc.to_frame(name='geometry'), on='geoloc', how='left')
            df2 = gpd.GeoDataFrame(df2)

            fig, ax = plt.subplots()
            df2.groupby('quarter').percent_production.sum().plot(kind='barh')
            ax.set_title(f'Average Production of {crop} per Quarter')
            ax.set_xlabel('Fraction of annual production')
            ax.set_ylabel('Quarter')
            
            return fig
        
        

        st.pyplot(crop_plotter(crop_selected))
        st.pyplot(crop_plotter2(crop_selected))
        
        st.markdown('---')
        
        text_content4 ="""
        Considering the potential disruption in the agricultural value chain when natural disasters occur for regionally-concentrated crops, there is value in diversifying the types of crops planted across regions. 
        """
        st.markdown(f'<p class="openSans">{text_content4}</p>', unsafe_allow_html=True)
        
        
        
# The Price of Goods in the Philippines have steadily increased over the years. In the advent of global warming and natural disasters, the retail prices of crops have frequently fluctuated in response. 
#     # <Viz for prices>
    
# An example of this is how the price of Garlic simply responds to the available supply of Garlic in the country. Whereas, low supply of Garlic coincided with high prices. In the same manner, Garlic prices dropped when supply went up.  
#     # <Viz of garlic supply>

# Our team, M3GA, hopes to address this specific issue by optimizing the agricultural supply chain through crop diversification. As of now, there are certain crops that highly concentrated in one location in a specific quarter which in turn results in lower prices at that location for that specific crop but higher prices for other locations. 
#     # <Choropleths>

# Considering the potential disruption in the agricultural value chain when natural disasters occur for regionally-concentrated crops, there is value in diversifying the types of crops planted across regions. 