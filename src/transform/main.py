# Vamos importar o que precisamos
import pandas as pd
import sqlite3
from datetime import datetime

# Definir o caminho para o arquivo JSON
df = pd.read_json('data/data.json')

# setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# Adicionar a coluna_source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/notebook?sb=rb#D[A:notebook]"

# Adicionar a coluna _data_coleta com a data e hora atuais
df['_data_coleta'] = datetime.now()

#tratar nulos
df['old_money'] = df['old_money'].fillna('0')
df['new_money'] = df['new_money'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['review_amount'] = df['review_amount'].fillna('0')

# Garantir que estão como strings antes de usar .str
df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['review_amount'] = df['review_amount'].astype(str).str.replace(r'[\(\)]', '', regex=True)

# converter para numéricos 
df['old_money'] = df['old_money'].astype(float)
df['new_money'] = df['new_money'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['review_amount'] = df['review_amount'].astype(int)

# manter apenas os produtos com preço entre 1000 e 10000 reais
df = df[
    (df['old_money'] >= 1000) & (df['old_money'] <= 10000) &
    (df['new_money'] >= 1000) & (df['new_money'] <= 10000)
]

# conectar ao banco de dados SQLite
conn = sqlite3.connect('data/mercadolivre.db')

# salvar o dataframe no banco de dados SQLite
df.to_sql('notebook', conn, if_exists='replace', index=False)

# fechar a conexão com o banco de dados
conn.close()