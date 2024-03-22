class Restaurante:
    def __init__(self):
        self.qtde_entreg_unicos = None
        self.media_c_festival = None
        self.media_s_festival = None
        self.desvio_c_festival = None
        self.desvio_s_festival = None
        self.distancia_media = None              

#================================ DataFrame - Visão Entregadores ===============================
#===============================================================================================

#2.3 - A avaliação média por entregador
def avalia_media_por_entregador(dados1):
     df_aux = (dados1[['Delivery_person_ID', 'Delivery_person_Ratings']].
               groupby(['Delivery_person_ID']).mean().round(2).reset_index())
     
     return df_aux

#2.4 - A avaliação média e o desvio padrão por tipo de tráfego.
def avalia_media_desvio_por_trafego(dados1):
    df_aux = (dados1[['Road_traffic_density','Delivery_person_Ratings']].
              groupby(['Road_traffic_density']).
              agg(Media_Avaliacao=('Delivery_person_Ratings','mean'), 
                  Desvio_Padrao_Avaliacao=('Delivery_person_Ratings','std')).
                  round(2).reset_index())  
    
    return df_aux

#2.5 - A avaliação média e o desvio padrão por condições climáticas.
def avalia_media_desvio_por_clima(dados1):
    df_aux = (dados1[['Weatherconditions','Delivery_person_Ratings']].
              groupby(['Weatherconditions']).
              agg(Media_Avaliacao=('Delivery_person_Ratings','mean'), 
                  Desvio_Padrao_Avaliacao=('Delivery_person_Ratings','std')).
                  round(2).reset_index()) 
    
    return df_aux

#2.6 - Os 10 entregadores mais rápidos por cidade.
#2.7 - Os 10 entregadores mais lentos por cidade.
def entreg_rapidos_lentos_por_cidade(dados1, ordenacao_time):
    ''' A única diferença entre os DataFrames.: 2.6 e 2.7 é a 
        ordenação da coluna.: Time_taken
        quando é informado ordenacao_time=True retorna os entregadores
        mais rápidos, quando informado ordenacao_time=False retorna
        os entregadores mais lentos.
    '''
    df_aux = (dados1[['City', 'Delivery_person_ID', 'Time_taken']].
              groupby(['City','Delivery_person_ID']).
              mean().sort_values(['City','Time_taken'],
                                 ascending=[True, ordenacao_time]).reset_index())

    first_index = 0
    last_index = 0
    index_list = []
    for cidade in df_aux['City'].unique():
        first_index = int(df_aux[df_aux['City'] == cidade].head(1).index.values)
        last_index  = int(df_aux[df_aux['City'] == cidade].tail(1).index.values)

        if df_aux[df_aux['City'] == cidade]['Time_taken'].count() > 10:
            lista = list(range(first_index, first_index+10))
        else:
            lista = list(range(first_index, last_index+1))

        index_list.extend(lista)

    df_aux = df_aux.loc[index_list, :]

    return df_aux

#===============================================================================================


#================================ DataFrame - Visão Restaurantes ===============================
#===============================================================================================

def carrega_inf_restaurante(dados1):
    rest = Restaurante()
    df_aux = (dados1[['Festival','Time_taken']].
              groupby(['Festival']).agg(Media_tempo=('Time_taken', 'mean'), 
                                        Desvio_padrao_tempo=('Time_taken', 'std')).
                                        round(2).reset_index())

    rest.qtde_entreg_unicos = dados1['Delivery_person_ID'].nunique()
    rest.media_c_festival = df_aux[df_aux['Festival'] == 'Yes']['Media_tempo'].values[0]
    rest.media_s_festival = df_aux[df_aux['Festival'] == 'No']['Media_tempo'].values[0]

    rest.desvio_c_festival = df_aux[df_aux['Festival'] == 'Yes']['Desvio_padrao_tempo'].values[0]
    rest.desvio_s_festival = df_aux[df_aux['Festival'] == 'No']['Desvio_padrao_tempo'].values[0]
    rest.distancia_media = dados1['distancia_entrega'].mean().round(2)

    return rest

#3.4 - O tempo médio e o desvio padrão de entrega por cidade e tipo de pedido.
def tempo_medio_desvio_entrega_por_cidade(dados1):
    df_aux = (dados1[['City','Type_of_order','Time_taken']].
              groupby(['City','Type_of_order']).
              agg(Media_tempo=('Time_taken','mean'), 
                  Desvio_Padrao=('Time_taken','std')).round(2).reset_index())
    
    return df_aux

#===============================================================================================