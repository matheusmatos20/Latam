from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict

def retorna_jsons(filepath):
    Array_jsons=[]    
    try:
         
        with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    json_data = json.loads(line.strip())  # Usando .strip() para remover las quebras de lineas extras
                    Array_jsons.append(json_data) #salvando json en array

    except json.JSONDecodeError as e:
        print   (f"Erro ao decodificar JSON na linha: {line}. Erro: {e}")
    return Array_jsons

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    #El Json és un arquivo con vários Jsons y no una lista de Jsons, por esto necessitaremos crear una lista para realizar la lectura.

    #resultado a ser exportado
    resultados: List[Tuple[datetime.date, str]] = []
    #receberá la lista de jsons
    jsons = []
    
    agrupamento = defaultdict(int)
    agrupamento_datas_usuarios = defaultdict(lambda: defaultdict(int))  # Agrupar por fecha y usuários

    #1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días. Debe incluir las siguientes funciones:```python   
    try:
        #Realizando abertura de lo arquivo
        jsons = retorna_jsons(file_path)
       
        for item in jsons:
            data_str = item['date']
            user = item['user']['username']  # Nombre de usuário
            data_obj = datetime.fromisoformat(data_str)  
            #Formata la Fecha para yyyy-mm-dd para poder realizar el agrupamento por fecha
            data_formatada = data_obj.strftime('%Y-%m-%d')  
            #Realiza la contage de usuários por fecha
            agrupamento_datas_usuarios[data_formatada][user] += 1
            #conta el numeros de itens para cada fecha
            agrupamento[data_formatada] += 1  

        # top_10_datas = sorted(agrupamento.items(), key=lambda x: x[1], reverse=True)[:10]

        # print(top_10_datas)

        for data, usuarios in agrupamento_datas_usuarios.items():
            # print(f"Data: {data},{usuario}")
            # Ordena los usuários pela cuantida de publicaciones
            usuarios_ordenados = sorted(usuarios.items(), key=lambda x: x[1], reverse=True)
            if usuarios_ordenados:
                top_usuario, top_count = usuarios_ordenados[0]
            data_obj = datetime.strptime(data, '%Y-%m-%d').date()
            resultados.append((data, top_usuario))
            # print(f"Data: {data}, Usuário: {top_usuario}, Postagens: {top_count}")
        return resultados       

    except KeyError:
            print("Erro: Campo 'date' ou 'Usuario' não encontrado no item.")
    except ValueError as e:
            print(f"Erro ao converter data: {e}")
    

##-------------------------------------TESTE ----------------------------------##
file_path = "C:\\Users\\mathe\\Documents\\Desafio Latam\\farmers-protest-tweets-2021-2-4.json"
data = q1_memory(file_path)
print(data)



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