import plotly.express as px
import folium
import plotly.graph_objects as go
import numpy as np
#import pandas as pd

#=================================== Graficos - Visão Empresa ==================================
#===============================================================================================
def qtde_pedidos_por_dia(dados1):
    #1.1 - Quantidade de pedidos por dia
    colunas = ['ID','Order_Date']
    df_aux = dados1[colunas].groupby(['Order_Date']).count().reset_index()
    
    fig = px.bar(df_aux, x='Order_Date', y='ID')

    return fig  

def qtde_pedidos_por_trafego(dados1):
    #1.3 - Distribuição dos pedidos por tipo de tráfego
    df_aux = dados1[['Road_traffic_density','ID']].groupby(['Road_traffic_density']).count().reset_index()
    df_aux['entregas_perc'] = (df_aux['ID'] / df_aux['ID'].sum()).round(2) * 100

    fig = px.pie(df_aux, values='entregas_perc', names='Road_traffic_density')

    return fig

#1.4 - Comparação do volume de pedidos por cidade e tipo de tráfego    
def qtde_pedidos_por_cidade_trafego(dados1):
    df_aux = dados1.loc[:, ['City', 'Road_traffic_density', 'ID']].groupby(['City','Road_traffic_density']).count().reset_index()            
    fig = px.scatter(df_aux, x='City', y='Road_traffic_density', size='ID', color='City')

    return fig

#1.2 - Quantidade de pedidos por semana
def qtde_pedidos_por_semana(dados1):
    df_aux = dados1.loc[:, ['week_of_year', 'ID']].groupby(['week_of_year']).count().reset_index()
    fig = px.line(df_aux, x='week_of_year', y='ID')

    return fig

#1.5 - A quantidade de pedidos por entregador e por semana
def qtde_pedidos_por_entregador_semana(dados1):    
    df_aux = dados1[['week_of_year','ID','Delivery_person_ID']].groupby(['week_of_year']).agg(Qtde_Pedidos=('ID', 'count'), Qtde_Uni_Entregadores=('Delivery_person_ID', 'nunique')).reset_index()
    df_aux['order_by_deliver'] = df_aux['Qtde_Pedidos'] / df_aux['Qtde_Uni_Entregadores']

    fig = px.line(df_aux, x='week_of_year', y='order_by_deliver')

    return fig

#1.6 - Localização central de cada cidade por tipo de tráfego
def local_central_cidade_por_trafego(dados1):
    df_aux = dados1.loc[:, ['Road_traffic_density','City', 'Delivery_location_latitude','Delivery_location_longitude']].groupby(['City','Road_traffic_density']).median().reset_index()
    
    map = folium.Map()

    for index, location_info in df_aux.iterrows():  
        folium.Marker([location_info['Delivery_location_latitude'],
                       location_info['Delivery_location_longitude']],
                       popup=location_info[['City','Road_traffic_density']]).add_to(map)

    return map    

#===============================================================================================


#================================= Graficos - Visão Restaurante ================================
#===============================================================================================

#3.2 - A distância média dos resturantes e dos locais de entrega
def distancia_media_por_cidade(dados1):
    df_aux = dados1[['City','distancia_entrega']].groupby(['City']).mean().reset_index()
    fig = (go.Figure( data=[ go.Pie(labels=df_aux['City'],
                                    values=df_aux['distancia_entrega'], 
                                    pull=[0, 0.1, 0])]))
    
    return fig

#3.3 - O tempo médio e o desvio padrão de entrega por cidade
def tempo_medio_desvio_entreg_por_cidade(dados1):
    df_aux = (dados1[['City','Time_taken']].
              groupby(['City']).agg(Media_tempo=('Time_taken','mean'), 
                                    Desvio_Padrao=('Time_taken','std')).round(2).reset_index())
    
    fig = go.Figure()
    fig.add_trace( go.Bar(name='Control', x=df_aux['City'], y=df_aux['Media_tempo'],
                          error_y=dict( type='data', array=df_aux['Desvio_Padrao'])))                                
    fig.update_layout(barmode='group')

    return fig

#3.5 - O tempo médio e o desvio padrão de entrega por cidade e tipo de tráfego.
def tempo_medio_desvio_entreg_por_cidade_trafego(dados1):
    df_aux = (dados1[['City','Road_traffic_density','Time_taken']].
              groupby(['City','Road_traffic_density']).
              agg(Media_tempo=('Time_taken','mean'), 
                  Desvio_Padrao=('Time_taken','std')).round(2).reset_index()) 

    fig = px.sunburst(df_aux, path=['City', 'Road_traffic_density'], values='Media_tempo',
                      color='Desvio_Padrao', color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df_aux['Desvio_Padrao'])) 
    
    return fig



#===============================================================================================

