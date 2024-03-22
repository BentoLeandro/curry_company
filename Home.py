import streamlit as st
from PIL import Image

st.set_page_config(page_title='Home', page_icon='')

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
