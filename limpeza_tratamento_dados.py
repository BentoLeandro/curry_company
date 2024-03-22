import pandas as pd
from haversine import haversine

def calcula_distancia(dt_aux):
    restaurante = (dt_aux['Restaurant_latitude'], dt_aux['Restaurant_longitude'])
    cliente = (dt_aux['Delivery_location_latitude'], dt_aux['Delivery_location_longitude'])

    distancia = haversine(restaurante, cliente)
    distancia = round(distancia, 4)

    return distancia

#===================================================================================================
#============================ Importação, Limpeza e tratamento dos Dados ===========================
#===================================================================================================
def import_limpeza_trat_dados():
    '''Esta função é utilizada para importar, limpar e tratar o dataframe

        Tipos de limpeza:
        1. Remoção dos dados NaN
        2. Mudança do tipo da coluna de dados
        3. Remoção dos espaços das variáveis de texto
        4. Formatação da coluna de datas
        5. Limpeza da coluna de tempo (remoção do texto (min))

        Input.: DataFrame
        Output.: DataFrame
    '''

    # Import dataset
    dados = pd.read_csv('dataset/train.crdownload')
    dados1 = dados.copy()

    dados1 = dados1[(dados1['City'] != 'NaN') & (dados1['City'] != 'NaN ')].copy()
    linhas_selecionadas = (dados1['Delivery_person_Age'] != 'NaN ') & (dados1['Delivery_person_Age'] != 'NaN')

    dados1 = dados1.loc[linhas_selecionadas, :].copy()
    dados1['Delivery_person_Age'] = dados1['Delivery_person_Age'].astype(int)
    dados1['Delivery_person_Ratings'] = dados1['Delivery_person_Ratings'].astype(float)

    dados1['Order_Date'] = pd.to_datetime(dados1['Order_Date'], format='%d-%m-%Y')

    index_nan = (dados1['multiple_deliveries'] == 'NaN ') | (dados1['multiple_deliveries'].isna())
    dados1 = dados1[~index_nan].copy()

    dados1 = dados1[(dados1['Road_traffic_density'] != 'NaN') & (dados1['Road_traffic_density'] != 'NaN ')].copy()

    index_festival_nan = (dados1['Festival'] == 'NaN') | (dados1['Festival'] == 'NaN ')
    dados1.loc[index_festival_nan, ['Festival']] = 'No'

    dados1['Time_taken'] = dados1['Time_taken(min)'].apply(lambda x: x.replace('(min)','').strip())
    dados1['Time_taken'] = dados1['Time_taken'].astype(int)

    dados1['multiple_deliveries'] = dados1['multiple_deliveries'].astype(int)

    dados1.reset_index(drop=True, inplace=True)

    for i in range(len(dados1)):
        dados1.loc[i, 'ID'] = dados1.loc[i, 'ID'].strip()

    dados1.loc[ : ,'Delivery_person_ID'] = dados1.loc[ : ,'Delivery_person_ID'].str.strip()
    dados1.loc[ : ,'Road_traffic_density'] = dados1.loc[ : ,'Road_traffic_density'].str.strip()
    dados1.loc[ : ,'Type_of_order'] = dados1.loc [ : ,'Type_of_order'].str.strip()
    dados1.loc[ : ,'Type_of_vehicle'] = dados1.loc[ : ,'Type_of_vehicle'].str.strip()
    dados1.loc[ : ,'Festival'] = dados1.loc[ : ,'Festival'].str.strip()
    dados1.loc[ : ,'City'] = dados1.loc[ : ,'City'].str.strip()

    dados1['week_of_year'] = dados1['Order_Date'].dt.strftime('%U')    

    dados1['distancia_entrega'] = dados1.apply(calcula_distancia, axis=1)

    return dados1
#=================================================================================================== 
