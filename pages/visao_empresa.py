import limpeza_tratamento_dados
import funcoes_graficos as graf_emp
import barra_lateral as menu

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

st.set_page_config(page_title='Visão Empresa', layout='wide')
#===================================================================================================
#========================================== Barra Lateral ==========================================
#===================================================================================================
inf_barra = menu.carrega_barra_lateral(dados1, pmostra_filtro_data=True, 
                                       pmostra_cond_transito=True, 
                                       pmostra_cond_clima=False)

date_slider = inf_barra.data_limite
opcoes_trafego = inf_barra.cond_trafego

#===================================================================================================

#Filtro de Datas
dados1 = dados1[dados1['Order_Date'] <= date_slider]

#Filtro de condição do trânsito
linhas_selecionadas = dados1['Road_traffic_density'].isin(opcoes_trafego)
dados1 = dados1.loc[linhas_selecionadas, :]

#===================================================================================================
#======================================== Layout Streamlit =========================================
#===================================================================================================
st.header('Marketplace - Visão Empresa')
tab1, tab2, tab3 = st.tabs(['Visão Gerencial','Visão Tática', 'Visão Geográfica'])

#1.0 - Visão Empresa
with tab1:
    #1.1 - Quantidade de pedidos por dia
    with st.container():
        st.markdown('## Pedidos por Dia')
                   
        fig = graf_emp.qtde_pedidos_por_dia(dados1) 
        st.plotly_chart(fig, use_container_width=True)

    with st.container():  
        col1, col2 = st.columns(2)
        
        #1.3 - Distribuição dos pedidos por tipo de tráfego
        with col1:
            st.markdown('## Pedidos por tipo de tráfego')                        
            fig = graf_emp.qtde_pedidos_por_trafego(dados1)
            st.plotly_chart(fig, use_container_width=True)

        #1.4 - Comparação do volume de pedidos por cidade e tipo de tráfego    
        with col2:
            st.markdown('## Volume de pedidos por cidade e tipo de tráfego')            
            fig = graf_emp.qtde_pedidos_por_cidade_trafego(dados1)
            st.plotly_chart(fig, use_container_width=True)

with tab2:
    #1.2 - Quantidade de pedidos por semana
    with st.container():
        st.markdown('## Quantidade de pedidos por semana')                
        fig = graf_emp.qtde_pedidos_por_semana(dados1)
        st.plotly_chart(fig, use_container_width=True)

    #1.5 - A quantidade de pedidos por entregador e por semana
    with st.container():
        st.markdown('## Quantidade de pedidos por entregador e por semana')        
        fig = graf_emp.qtde_pedidos_por_entregador_semana(dados1)
        st.plotly_chart(fig, use_container_width=True)


#1.6 - Localização central de cada cidade por tipo de tráfego
with tab3:
    with st.container():
        st.markdown('## Localização central de cada cidade por tipo de tráfego')        
        map = graf_emp.local_central_cidade_por_trafego(dados1)
        folium_static(map, width=1024, height=500)   
                     


#===================================================================================================