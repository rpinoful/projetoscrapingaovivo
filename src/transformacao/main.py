import pandas as pd 
import sqlite3
from datetime import datetime

# ler arquivo json junto com o path 
df = pd.read_json('../../data/mercadolivre.json')


#mostrar todas as columnas de pandas 
pd.set_option('display.max_columns', None)

#criando coluna source
df['source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

# quando foram coletado os dados
df['data_coleta'] = datetime.now()


# remover os nulos
df[['old_price', 'current_price','review']] = df[['old_price', 'current_price','review']].astype(float).fillna(0)






############# BANCO DE DADOS ########################################

#conetar ao banco de dados sql lite -(ABRINDO CONEXÃO)
conn = sqlite3.connect('../../data/quotes.db')

#salvar o dataframe a tabela sql 
df.to_sql('mercadolivre_items',conn,if_exists='replace',index=False)


#fechando conexão
conn.close()

print(df.head())

