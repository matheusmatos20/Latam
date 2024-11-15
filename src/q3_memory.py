from typing import List, Tuple
import json
from collections import Counter
import re
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    resultado =[]
    mention_count = contar_mencoes(retorna_jsons(file_path))

    # Top 10 emojis mais frequentes
    top_10_users = mention_count.most_common(10)

    # Exibir os resultados
    # print("Top 10 emojis mais frequentes:")
    for mention, count in top_10_users:
        resultado.append((mention, count))
        # print(f"{emoji_char}: {count}")
    return resultado
        # print(f"{emoji_char}: {count}")
#Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:
    
def retorna_jsons(filepath):
    Array_jsons=[]    
    with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                json_data = json.loads(line.strip())  # Usando .strip() para remover las quebras de lineas extras
                Array_jsons.append(json_data) #salvando json en array
    return Array_jsons


def contar_mencoes(jsons):
    mention_counter = Counter()

    for tweet in jsons:
        content = tweet.get("content", "")

        # Expressão regular para capturar menções de usuários (@username)
        pattern = r'@([A-Za-z0-9_]+)'

        # Encontrar todas as menções no conteúdo
        mentions = re.findall(pattern, content)
        # Conta a ocorrência de cada emoji
        mention_counter.update(mentions)
         
    return mention_counter #list(emoji_counter.items())

# file_path = "C:\\Users\\mathe\\Documents\\Desafio Latam\\farmers-protest-tweets-2021-2-4.json"
# # Contar os emojis nos tweets

# data = q3_memory(file_path)
# print(data)