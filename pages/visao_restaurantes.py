import array
import limpeza_tratamento_dados
import barra_lateral as menu
import funcoes_dataframe as inf_restaurante
import funcoes_graficos as graf_rest

# Libraries
import plotly.express as px
import folium
from haversine import haversine
import plotly.graph_objects as go
import numpy as np

# Bibliotecas necessárias 
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
from datetime import datetime
from PIL import Image

dados1 = limpeza_tratamento_dados.import_limpeza_trat_dados()

st.set_page_config(page_title='Visão Restaurantes', layout="wide")
#===================================================================================================
#========================================== Barra Lateral ==========================================
#===================================================================================================
inf_barra = menu.carrega_barra_lateral(dados1, pmostra_filtro_data=True,
                                       pmostra_cond_transito=True, 
                                       pmostra_cond_clima=True)

date_slider = inf_barra.data_limite
opcoes_trafego = inf_barra.cond_trafego
opcoes_clima = inf_barra.cond_clima 

#===================================================================================================

#Filtro de Datas
dados1 = dados1[dados1['Order_Date'] <= date_slider]

#Filtro de condição do trânsito
linhas_selecionadas = dados1['Road_traffic_density'].isin(opcoes_trafego)
dados1 = dados1.loc[linhas_selecionadas, :]

#Filtro de condição do clima
linhas_selecionadas = dados1['Weatherconditions'].isin(opcoes_clima)
dados1 = dados1.loc[linhas_selecionadas, :]

#===================================================================================================
#======================================== Layout Streamlit =========================================
#===================================================================================================
st.header('Marketplace - Visão Restaurantes')

tab1, tab2, tab3 = st.tabs(['Visão Gerencial', '-', '-'])

inf_rest = inf_restaurante.carrega_inf_restaurante(dados1)
media_c_festival = inf_rest.media_c_festival
media_s_festival = inf_rest.media_s_festival 

desvio_c_festival = inf_rest.desvio_c_festival
desvio_s_festival = inf_rest.desvio_s_festival

#3.0 Visão Geral dos Restaurantes
with tab1:    
    with st.container():                     
        col1, col2, col3, col4, col5, col6 = st.columns(6, gap='large')

        with col1:
            qtde_entreg_unicos = inf_rest.qtde_entreg_unicos
            col1.metric(label='Entregadores', value=qtde_entreg_unicos)

        with col2:
            distancia_media = inf_rest.distancia_media
            col2.metric(label='Distância Média', value=distancia_media)
        
        with col3:            
            col3.metric(label='Média c/ Festival', value=media_c_festival, delta='Min', delta_color='off')

        with col4:
            col4.metric(label='Desvio P. c/ Festival', value=desvio_c_festival)

        with col5:
            col5.metric(label='Média s/ Festival', value=media_s_festival, delta='Min', delta_color='off')

        with col6:
            col6.metric(label='Desvio P. s/ Festival', value=desvio_s_festival)                                     

    with st.container():
        st.markdown('___')
        col1, col2 = st.columns(2, gap='large')

        #3.2 - A distância média dos resturantes e dos locais de entrega
        with col1:
            st.subheader('Distância Média de entrega por cidade')                    
            fig = graf_rest.distancia_media_por_cidade(dados1)
            st.plotly_chart(fig, use_container_width=True)
                
        #3.4 - O tempo médio e o desvio padrão de entrega por cidade e tipo de pedido.    
        with col2:
            st.subheader('Tempo médio e o desvio padrão de entrega por cidade e tipo de pedido.')                       
            df_aux = inf_restaurante.tempo_medio_desvio_entrega_por_cidade(dados1)
            st.dataframe(df_aux)
    
    with st.container():
        st.markdown('___')
        st.subheader('Tempo Médio e o Desvio Padrão')
        col1, col2 = st.columns(2, gap='large')
        
        #3.3 - O tempo médio e o desvio padrão de entrega por cidade
        with col1:
            st.subheader('Tempo médio e o desvio padrão de entrega por cidade')                    
            fig = graf_rest.tempo_medio_desvio_entreg_por_cidade(dados1)
            st.plotly_chart(fig, use_container_width=True)
        
        #3.5 - O tempo médio e o desvio padrão de entrega por cidade e tipo de tráfego.
        with col2:
            st.subheader('Tempo médio e o desvio padrão de entrega por cidade e tipo de tráfego')            
            fig = graf_rest.tempo_medio_desvio_entreg_por_cidade_trafego(dados1)
            st.plotly_chart(fig, use_container_width=True)  
        
#===================================================================================================