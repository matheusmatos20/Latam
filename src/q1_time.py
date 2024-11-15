import pandas as pd
from datetime import datetime
from typing import List, Tuple

# Neste ejercicio, el principal problema se deu por causa de la coluna user.username y la dificuldad de pandas en leer ninhos.
# Para esto, se fué necessario una normalizacion.

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    try:
        # # LECTURA DE JSON PARA DATAFRAME
        df = pd.read_json(file_path, lines=True, encoding='utf-8')

        # # NORMALIZACION DA COLUNA USER.USERNAME PARA UNA NUEVA COLUNA
        df = pd.json_normalize(df.to_dict(orient='records'))

        # CONVERSION DE CAMPO DATA PARA AYUDAR EN AGRUPAMIENTO
        df['date'] = pd.to_datetime(df['date'])

        # CREANDO UNA NUEVA COLUNA 'date_str' coN formato YYYY-MM-DD
        df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')

        # AGRUPANDO POR FECHA Y USUARIO, CONTANDO EL NUMERO DE TWEETS POR USUARIO EN CADA FECHA
        grouped = df.groupby(['date_str', 'user.username']).size().reset_index(name='tweet_count')

        # Para cada data, encontra o usuário com o maior número de tweets
        top_user_p_day = grouped.loc[grouped.groupby('date_str')['tweet_count'].idxmax()]

        # Formata os resultados em uma lista de tuplas (data, usuário)
        resultados = [(row['date_str'], row['user.username']) for _, row in top_user_p_day.iterrows()]

        return resultados
    
    except ValueError as e:
        print(f"Erro ao converter data: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

##-------------------------------------TESTE ----------------------------------##
# file_path = "C:\\Users\\mathe\\Documents\\Desafio Latam\\farmers-protest-tweets-2021-2-4.json"
# data = q1_memory(file_path)
# print(data)



# --------------------------------------------------------OBSERVAÇÃO ---------------------------------------------------------#
# Se fosse um banco de dados relacional e tivessemos as tabelas Tweet, TweetUser, User, para resolver esse exercicio seria somente necessário o comando abaixo
# Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días.

# with Max_tweets as (
#         select top 10 count(*) as qtd ,t.date 
#         from tweet t
#         inner join user u on u.user_id = t.user_id
#         group by t.date
#         order by 1 desc)
# , count_users as (
#      select t.date, u.username,Count(*) as qtd
#         from tweet t
#         inner join user u on u.user_id = t.user_id
#         inner join cte  c on c.date = t.date
#         group by t.date,u.username
# )
# , top_users as (
#      select date,username, qtd, row_number() over(partition by date, order by qtd desc) as rank
#      from count_users
# )
# select date,username
# from top_users
# where rank=1