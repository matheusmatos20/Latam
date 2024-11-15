from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    pass
    

def retorna_jsons(filepath):
    Array_jsons=[]    
    with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                json_data = json.loads(line.strip())  # Usando .strip() para remover las quebras de lineas extras
                Array_jsons.append(json_data) #salvando json en array
    return Array_jsons

