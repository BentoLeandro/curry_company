import streamlit as st
from PIL import Image

dark = '''
<style>
    .stSidebar {
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        color: rgb(250, 250, 250);
        color-scheme: dark;        
        background-color: rgb(38, 39, 48);        
    } 

    .stSidebarNavSeparator {
        color-scheme: dark;
        color: rgba(250, 250, 250, 0.6);
        border-bottom: 1px solid rgba(250, 250, 250, 0.2);
    }  

    .stApp {         
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        background: rgb(14, 17, 23);
        color: rgb(250, 250, 250);
        color-scheme: dark;          
    }     
</style>
'''

st.set_page_config(page_title='Home', page_icon='')
st.session_state.theme = "dark" 
st.markdown(dark, unsafe_allow_html=True)

image_path = "logo_data_science.png"
image = Image.open(image_path)
st.sidebar.image(image, width=280)  

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Entrega mais rápida da cidade')
st.sidebar.markdown("___") 



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
        - @leandroreisbento
    '''
)
