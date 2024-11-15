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