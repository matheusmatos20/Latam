from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
import emoji
from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    resultado =[]
    emoji_counts = contar_emojis(retorna_jsons(file_path))

    # Top 10 emojis mais frequentes
    top_10_emojis = emoji_counts.most_common(10)

    # Exibir os resultados
    # print("Top 10 emojis mais frequentes:")
    for emoji_char, count in top_10_emojis:
        resultado.append((emoji_char, count))
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


def contar_emojis(jsons):
    emoji_counter = Counter()

    for tweet in jsons:
        content = tweet.get("content", "")
        
        # Extrai todos os emojis do conteúdo
        emojis = [char for char in content if emoji.is_emoji(char)]
        
        # Conta a ocorrência de cada emoji
        emoji_counter.update(emojis)
         
    return emoji_counter #list(emoji_counter.items())

# file_path = "C:\\Users\\mathe\\Documents\\Desafio Latam\\farmers-protest-tweets-2021-2-4.json"
# Contar os emojis nos tweets

# data = q2_time(file_path)
# print(data)