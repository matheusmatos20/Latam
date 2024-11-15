import pandas as pd
import emoji
from collections import Counter
from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # LECTURA DE JSON
    df = pd.read_json(file_path, lines=True, encoding='utf-8')

    # EXTRACCION DE EMOJIS
    df['emojis'] = df['content'].apply(lambda content: [char for char in content if emoji.is_emoji(char)])

    # COMPRIMI LA LISTA
    all_emojis = [emoji for sublist in df['emojis'] for emoji in sublist]

    # COUNT DE EMOJIS
    emoji_counter = Counter(all_emojis)

    # TOP 10 EMOJIS
    top_10_emojis = emoji_counter.most_common(10)

    return top_10_emojis

# LLAMADA DE TESTE:
# file_path = "C:\\Users\\mathe\\Documents\\Desafio Latam\\farmers-protest-tweets-2021-2-4.json"
# resultado = q2_time(file_path)
# print(resultado)