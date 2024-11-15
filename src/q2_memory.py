from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
import emoji
from typing import List, Tuple

#Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    resultado =[]
    emoji_counts = contar_emojis(retorna_jsons(file_path))

    # LLAMADA DE RUTINA
    top_10_emojis = emoji_counts.most_common(10)

    # print("Top 10 emojis mais frequentes:")
    for emoji_char, count in top_10_emojis:
        resultado.append((emoji_char, count))
        # print(f"{emoji_char}: {count}")
    return resultado
        # print(f"{emoji_char}: {count}")
    

#RUTINA DE LECTURA DE JSON    
def retorna_jsons(filepath):
    Array_jsons=[]    
    with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                json_data = json.loads(line.strip())  # Usando .strip() para remover las quebras de lineas extras
                Array_jsons.append(json_data) #salvando json en array
    return Array_jsons

#RUTINA PARA CONTAR EMOJIS
def contar_emojis(jsons):
    emoji_counter = Counter()

    for tweet in jsons:
        content = tweet.get("content", "")
        
        # EXTRACCION DE EMOJIS
        emojis = [char for char in content if emoji.is_emoji(char)]
        
        # COUNT DE EMOJIS
        emoji_counter.update(emojis)
         
    return emoji_counter #list(emoji_counter.items())

# file_path = "C:\\Users\\mathe\\Documents\\Desafio Latam\\farmers-protest-tweets-2021-2-4.json"
# data = q2_memory(file_path)
# print(data)