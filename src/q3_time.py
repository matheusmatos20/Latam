import pandas as pd
import re
from collections import Counter
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    #LE ARQUIVO JSON E COLOCA EN DATAFRAME
    df = pd.read_json(file_path, lines=True, encoding='utf-8')

    # EXPRESIÓN REGULAR PARA IDENTIFICAR MENTION
    pattern = r'@([A-Za-z0-9_]+)'

    # APLICA REGEX PARA EXTRAIR MENTIONS
    df['mentions'] = df['content'].apply(lambda x: re.findall(pattern, x))

    # COMPRIMI A LISTA
    all_mentions = [mention for sublist in df['mentions'] for mention in sublist]

    # CRIA COUNTER PARA MENTIONS
    mention_counter = Counter(all_mentions)

    # TOP 10 USERS
    top_10_users = mention_counter.most_common(10)

    return top_10_users

# LLAMADA DE METODO:
# file_path = "C:\\Users\\mathe\\Documents\\Desafio Latam\\farmers-protest-tweets-2021-2-4.json"
# resultado = q3_memory(file_path)
# print(resultado)
