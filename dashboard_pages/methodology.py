import streamlit as st
from  PIL import Image
import networkx as nx
import pandas as pd
import itertools
import geopandas as gpd
from shapely.wkt import loads
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid

header_logo = Image.open(r'images/our_methodology_header.png')

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
        <strong>Step 1 : </strong> Munge data into desired format. 
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
        metho_img = Image.open(r'images/23.png')
        st.image(metho_img, width = 800)
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.write("""
                 Our data is the volume of crop production in three dimensions: Spatial location (in 2 levels of granularity: 16 regions or 83 provinces), Temporal information in years and quarters (11 years, 4 quarters), and Crop type.

                We normalized each location-quarter-crop trio by the annual production for that crop, then averaged over all the years to remove annual noise. 

                Since we want to increase diversity both in location and in time, we combined the spatial and temporal columns to create region-quarter pairs, which were used as nodes in our network. For each node, we have a vector of 342 crops which will be used to make its "crop profile".
                """)
        st.markdown(hide_img_fs, unsafe_allow_html=True)
    
        st.markdown("---")
    
        text_content ="""
        <strong>Step 2 : </strong> Create a crop profile for every spatiotemporal pair. 
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
        metho_img = Image.open(r'images/24.png')
        st.image(metho_img, width = 800)
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.write("""
                 Next step is to create a crop profile for every spatiotemporal pair. This is done by binarizing our information. We keep the top 5 crops per region
                 and keep all the regions that produced more than their "fair share" of each crop. Note that binarizing each row allows us to compare locations of differing granularity, e.g. a small town and an entire region.
                 """)
        st.markdown(hide_img_fs, unsafe_allow_html=True)
        
        st.markdown("---")
        
        text_content ="""
        <strong>Step 3 : </strong> Nodes will be connected by their crop profile similarity. 
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
        metho_img = Image.open(r'images/25.png')
        st.image(metho_img, width = 800)
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.write("""
                For the next step, nodes were connected by their crop profile similarity. 
                To do this, for each crop we added some weight to their top producers.
                For example, nodes 1, 4 and 5 all produce crop 1. So we added 1 to all edges connecting these nodes. We then looped over all crops. 
                """)
        st.markdown(hide_img_fs, unsafe_allow_html=True)
        
        st.markdown("---")
        
        text_content ="""
        <strong>Step 4 : </strong> Remove edges with low weights or connect redundant nodes. 
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
        metho_img = Image.open(r'images/26.png')
        st.image(metho_img, width = 800)
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        st.write("""
                Next, we trimmed the network by removing edges with low weights or connecting redundant nodes. In this step, we implement two rules.

                First, the nodes must be more than 250 km apart. This is the diameter of a typhoon. The logic behind this is so that region-quarter pairs tagged as similar will be far enough to not be affected by the same typhoon at the same time.

                Second, the network was trimmed to edges with a weight higher than 3. This value can be chosen arbitrarily to easily manage the network.

                We chose to use a network approach over various clustering methods due to the ease at which you can add conditions such as the above. 
                """)
        st.markdown(hide_img_fs, unsafe_allow_html=True)
        
        st.markdown("---")
        
        text_content ="""
        <strong>Step 5 : </strong> Identify potential planting alternatives for closer inspection by experts. 
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
        metho_img = Image.open(r'images/27.png')
        st.image(metho_img, width = 800)
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''
        
        st.write("""
                Lastly, we can now identify potential planting alternatives for closer inspection by experts and policymakers.
                 
                Using the network, we can check connected nodes to identify region-quarter pairs that are alternatives to each other.
                
                We can also use degree centrality to identify weakly connected nodes. These are region-quarter pairs that have few crops in common with other region-quarter pairs and can be tagged as lacking diversity. 

                Using degree centrality is intuitive, but other centrality measures may also be explored and prove to be useful.
                 """)
        st.markdown(hide_img_fs, unsafe_allow_html=True)
        
        st.markdown("---")
        
        text_content ="""
        <strong>Crop Network of the Philippines: </strong> Explore the generated network that we generated using our methodology. 
        """
        st.markdown(f'<p class="openSans">{text_content}</p>', unsafe_allow_html=True)
        
        df = pd.read_csv('data/processed/crop production volume.csv')

        # convert to long format
        df = df.set_index(['Crop', 'Geolocation', 'Level'])\
            .melt(ignore_index=False, var_name='quarter', value_name='produced')\
            .reset_index()

        # split the quarter column into year + quarter
        df = df.replace('..', 0) # replace with better method for fillna? 
        df['year'] = df['quarter'].str[:4]
        df['geoloc_quarter'] = df.Geolocation + '_Q' + df['quarter'].str[-1]
        del df['quarter']
        del df['Geolocation']
        
        df['produced'] = df['produced'].astype(float)
        yearly_production = df.query('Level=="PH"').groupby(['year', 'Crop']).produced.sum()#.reset_index()

        # we normalize by weight because the volume of watermelons and peppers aren't comparable
        df = df.set_index(['year', 'Crop'])
        df['yearly_production'] = yearly_production
        df['percent_production'] = df['produced']/df['yearly_production']
        del df['yearly_production']
        df = df.reset_index()
        
        aggregation_level = 'R'
        wide = df[df.Level==aggregation_level].groupby(['geoloc_quarter', 'Crop'], as_index=False).percent_production.mean()
        wide = wide.pivot('geoloc_quarter', 'Crop', 'percent_production')
        
        topN = 5 # for each geoloc_quarter, we will use its topN crops as base profile
        production_ratio = 2 # but we will also add in all those that provide for their own needs multiplied by `production_ratio`
        top_crops = wide.rank(axis=1, ascending=False) <= topN    # ARMM_Q1 produces 50% of crop A, 10% crop B, 5%C  1%D  0.0005%E
        overproduced = wide > (production_ratio/wide.shape[0])    # if it overproduces something and it can support itself + other places, the crop gets retained
        loc_profile = top_crops + overproduced
        loc_profile = loc_profile.astype(bool)
        
        pairs = []
        for crop in loc_profile.columns:
            crop_prod = loc_profile[crop]
            # regions that have crop X in their topN
            nodes = crop_prod[crop_prod].index
            # create pairwise combinations
            pairs += list(itertools.combinations(nodes, 2))
            
        # ignore pairs with weight <= weight_filter
        weight_filter = 2

        # count the number of times two regions were pairs
        edges = [(k[0], k[1], v)
                for k, v 
                in pd.Series(pairs).value_counts().iteritems()]

        edges = pd.DataFrame(edges, columns=['node1', 'node2', 'weight'])
        
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
        
        distance = lambda a, b: psgc[a].distance(psgc[b])
        distances = pd.Series({(n1, n2): distance(n1, n2)
                       for n1,n2 in itertools.permutations(psgc.index, 2)})
        
        edges['distance'] = edges.apply(lambda x: distances[(x.node1.split('_')[0], 
                                                     x.node2.split('_')[0])]
                                if x.node1.split('_')[0]!=x.node2.split('_')[0] else 0, axis=1)
        
        G = nx.from_pandas_edgelist(edges, 'node1', 'node2', edge_attr=True)
        
        latitude = psgc.centroid.y
        longitude = psgc.centroid.x/812732
        pos = pd.DataFrame(index=list(G.nodes()), columns=['x', 'y'])
        pos['x'] = pos.index.str[-1].astype(int) + pos.index.str.split('_').str[0].map(longitude)
        pos['y'] = pos.index.str.split('_').str[0].map(latitude)
        
        def plot_network(edgeweight_filter=3, distance_filter=200000):
            edge_x = []
            edge_y = []
            edges_for_removal = []
            for edge in G.edges(data=True):
                data = edge[-1]
                if data['weight'] > edgeweight_filter and data['distance'] > distance_filter:
                    x0, y0 = pos.loc[edge[0]].values
                    x1, y1 = pos.loc[edge[1]].values
                    edge_x.append(x0)
                    edge_x.append(x1)
                    edge_x.append(None)
                    edge_y.append(y0)
                    edge_y.append(y1)
                    edge_y.append(None)
                else:
                    edges_for_removal.append(edge)
            for node1, node2, data in edges_for_removal:
                G.remove_edge(node1, node2)

            edge_trace = go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=0.5, color='#888'),
                hoverinfo='none',
                mode='lines')

            node_x = []
            node_y = []
            for node in G.nodes():
                x, y = pos.loc[node]
                node_x.append(x)
                node_y.append(y)

            node_trace = go.Scatter(
                x=node_x, y=node_y,
                mode='markers',
                hoverinfo='text',
                marker=dict(
                    showscale=True,

                    # colorscale options
                    #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                    #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                    #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                    colorscale='Reds',
                    reversescale=True,
                    color=[],
                    size=10,
                    colorbar=dict(
                        thickness=15,
                        title='Node Connections',
                        xanchor='left',
                        titleside='right'
                    ),
                    line_width=2))
            
            node_adjacencies = []
            node_text = []
            for node, adjacencies in enumerate(G.adjacency()):
                node_adjacencies.append(len(adjacencies[1]))
                node_text.append(f'{adjacencies[0]} [{len(adjacencies[1])} connections]')

            node_trace.marker.color = node_adjacencies
            node_trace.text = node_text

            # plotting
            fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='Network graph made with Python',
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20,l=5,r=5,t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                            )
            return fig
        
        edgeweight_filter_value = st.slider('Select Minimum Number of Edges', 1, max([x[1] for x in G.degree()]), 3)
        distance_filter_value = st.slider('Select Minimum Distance', 50_000, 500_000, 200_000, 10_000)
            
        st.plotly_chart(plot_network(edgeweight_filter_value, distance_filter_value))

            
            

        
        
        