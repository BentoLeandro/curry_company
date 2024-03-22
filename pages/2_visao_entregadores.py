import limpeza_tratamento_dados
import barra_lateral as menu
import funcoes_dataframe as df_entreg

# Libraries
import plotly.express as px
#import plotly.graph_objetcs as go
import folium
from haversine import haversine

# Bibliotecas necessárias 
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
from datetime import datetime
from PIL import Image

dados1 = limpeza_tratamento_dados.import_limpeza_trat_dados()

st.set_page_config(layout="wide")
#===================================================================================================
#========================================== Barra Lateral ==========================================
#===================================================================================================
inf_barra = menu.carrega_barra_lateral(dados1, pmostra_cond_transito=True, 
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
st.header('Marketplace - Visão Entregadores')
tab1, tab2, tab3 = st.tabs(['Visão Gerencial','-','-'])

#2.0 Visão Geral dos Entregadores
with tab1:
    with st.container():       
        maior_idade = dados1['Delivery_person_Age'].max()
        menor_idade = dados1['Delivery_person_Age'].min()
        melhor_cond = dados1['Vehicle_condition'].max()
        pior_cond = dados1['Vehicle_condition'].min()

        col1, col2, col3, col4 = st.columns(4, gap='large')

        #Maior idade dos entregadores
        with col1:
            col1.metric('Maior idade',value=maior_idade)

        #Menor idade dos entregadores
        with col2:
            col2.metric(label='Menor idade',value=menor_idade) 

        #Melhor condição de veículo
        with col3:
            col3.metric(label='Melhor condição de veículo', value=melhor_cond)

        #Pior condição de veículo
        with col4:   
            col4.metric(label='Pior condição de veículo', value=pior_cond)

    with st.container():
        st.markdown('___')
        st.header('Avaliações')        
        col1, col2 = st.columns(2, gap='large')

        #2.3 - A avaliação média por entregador
        with col1:
            st.markdown('#### Avaliação média por Entregador')                        
            df_media_entregador = df_entreg.avalia_media_por_entregador(dados1)
            st.dataframe(df_media_entregador)    
        
        with col2:      
            #2.4 - A avaliação média e o desvio padrão por tipo de tráfego.      
            st.markdown('#### Avaliação média por trânsito')             
            df_media_desvio_trafego = df_entreg.avalia_media_desvio_por_trafego(dados1)
            st.dataframe(df_media_desvio_trafego)                        
            
            st.markdown('___')
            #2.5 - A avaliação média e o desvio padrão por condições climáticas.
            st.markdown('#### Avaliação média por clima')                                    
            df_media_desvio_clima = df_entreg.avalia_media_desvio_por_clima(dados1)
            st.dataframe(df_media_desvio_clima) 

    with st.container():
        st.markdown('___')
        st.header('Velocidade de entrega por Cidade') 

        col1, col2 = st.columns(2, gap='large')

        with col1:
            #2.6 - Os 10 entregadores mais rápidos por cidade.
            st.markdown('#### Entregadores mais rápidos')                
            df_entreg_mais_rapidos = df_entreg.entreg_rapidos_lentos_por_cidade(dados1, ordenacao_time=True) 
            st.dataframe(df_entreg_mais_rapidos)

        with col2:
            #2.7 - Os 10 entregadores mais lentos por cidade.
            st.markdown('#### Entregadores mais lentos')            
            df_entreg_mais_lentos = df_entreg.entreg_rapidos_lentos_por_cidade(dados1, ordenacao_time=False)
            st.dataframe(df_entreg_mais_lentos)         

                 

#===================================================================================================