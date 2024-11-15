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


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    pass