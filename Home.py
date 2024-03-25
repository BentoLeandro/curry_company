import streamlit as st
from PIL import Image
import barra_lateral as menu

css = """<style>
            [data-testid=stApp] {
                background-color: #0E1117;
                color: #FAFAFA;
            }   
                              
            [data-testid=stSidebar] {
                background-color: #262730;
                color: #FAFAFA;
            }
            
            [data-testid=stSidebarNavSeparator] {
                color: rgba(250, 250, 250, 0.6);
                border-bottom: 1px solid rgba(250, 250, 250, 0.2);    
            }    
            
            h1, h2, h3, h4, h5 {            
                color: #FAFAFA;
            }                        
         </style>
      """

st.set_page_config(page_title='Página Inicial', page_icon='🏠')

#st.markdown(css, unsafe_allow_html=True)

inf_barra = menu.carrega_barra_lateral(None, pmostra_filtro_data=False, 
                                       pmostra_cond_transito=False, 
                                       pmostra_cond_clima=False)



st.write('# Curry Company Growth Dashboard')
st.markdown(
    '''
    Growth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes.
    ### Como utilizar esse Growth Dashboard ?
    - Visão Empresa:
        - Visão Gerencial.: Métricas gerais de comportamento.
        - Visão Tática.: Indicadores semanais de crescimento.
        - Visão Geográfica.: Insights de geolocalização
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restaurantes:
        - Indicadores semanais de crescimento dos restaurantes.
    ### Contato
    @leandroreisbento
    '''
)
