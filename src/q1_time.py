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

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    pass