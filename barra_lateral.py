from gc import disable
import streamlit as st
from PIL import Image
from datetime import datetime
from st_pages import Page, show_pages, add_page_title, Section, add_indentation

#===================================================================================================
#========================================== Barra Lateral ==========================================
#===================================================================================================

class Menu:
    def __init__(self):
        self.data_limite = None
        self.cond_trafego = None
        self.cond_clima = None

def carrega_barra_lateral(dados1, pmostra_filtro_data, 
                          pmostra_cond_transito, pmostra_cond_clima):
    menu = Menu()    
    
    image_path = "logo_data_science.png"
    image = Image.open(image_path)
    st.sidebar.image(image, width=280)

    st.sidebar.markdown('# Cury Company')
    st.sidebar.markdown('## Entrega mais rápida da cidade')
    st.sidebar.markdown("___")    

    show_pages(
    [        
        Page("streamlit_app.py", "Página Inicial", "🏠"),       
        Page("pages/visao_empresa.py", "Visão Empresa", ":department_store:"),        
        Page("pages/visao_entregadores.py", "Visão Entregadores", ":motor_scooter:"),
        Page("pages/visao_restaurantes.py", "Visão Restaurantes", ":knife_fork_plate:"),
    ]
    )
    #add_indentation()      

    date_slider = 0
    if pmostra_filtro_data:
        st.sidebar.markdown('## Selecione uma data limite')
        date_slider = st.sidebar.slider('Até qual Data ?',
                                        value=datetime(2022, 4, 13),
                                        min_value=dados1['Order_Date'].min(), 
                                        max_value=dados1['Order_Date'].max(),
                                        format='DD-MM-YYYY')
        st.sidebar.markdown("___")

    opcoes_trafego = []
    if pmostra_cond_transito:
        opcoes_trafego = st.sidebar.multiselect(
            'Quais as condições do trânsito ?',
            dados1['Road_traffic_density'].unique(),
            default=dados1['Road_traffic_density'].unique() #'Low'
        )    
        st.sidebar.markdown("___")

    opcoes_clima = []
    if pmostra_cond_clima:     
        opcoes_clima = st.sidebar.multiselect(
            'Quais as condições do clima ?',
            dados1['Weatherconditions'].unique(),
            default=dados1['Weatherconditions'].unique()
        )
        st.sidebar.markdown("___")       

    menu.data_limite = date_slider
    menu.cond_trafego = opcoes_trafego
    menu.cond_clima = opcoes_clima      

    return menu     

#===================================================================================================