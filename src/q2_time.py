from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
import emoji
from typing import List, Tuple


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

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    pass