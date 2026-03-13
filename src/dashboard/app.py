#import streamlit as st
import pandas as pd 
import sqlite3

#conetar ao banco de dados sql lite -(ABRINDO CONEXÃO)
conn = sqlite3.connect('../../data/quotes.db')

cursor = conn.cursor
cursor.execute("""
    UPDATE mercadolivre_items 
    SET current_price = 243.33 
    WHERE rowid = 432      
""")

# Salvar a alteração
conn.commit()

# Verificar se corrigiu
cursor.execute("SELECT rowid, current_price FROM mercadolivre_items WHERE rowid = 432")
print(cursor.fetchone())

#carregar os dados da tabela 'mercadolivreitems' em um dataframe pandas 
df = pd.read_sql_query("SELECT * FROM mercadolivre_items",conn)

display(df)



#fechar conexão 
conn.close()



# Titulo de aplicação
st.title("Pesquiça de mercado - Tenis esportivo do mercadolivre")


#Melhorar o layout com colunas para KPIs
st.subheader('KPIS principais do sistema')
#divide a tela em 3 partes iguais 
#seria a mesma coisa que col1,col2,col3 = st.columns[1,1,1] , cada columna ocupa 33% da tela
col1,col2,col3 = st.columns(3)


#kpi 1 - Numero total de itens
numero_linhas = len(df)
col1.metric(label="Numero total de itens",value=numero_linhas)


#kpi 2 - Numero de marcas unicas 
numero_marcas_unicas = df['brand'].nunique()
col2.metric(label="Numero de marcas unicas",value=numero_marcas_unicas)


#kpi 3 - Preço medio novo (em reais)
precio_medio = df['current_price'].mean()
col3.metric(label="Precio medio novo (R$)",value=f"{precio_medio:.2f}")


#quais marcas são mais encontradas ate 10 pagina
st.subheader('Marcas mais encontradas ate pagina 10')
# Primeira coluna ocupa  66% da tela
# Segunda coluna ocupa  33,33
col1,col2 = st.columns([4,2])
top_10_pages_brand = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brand)
col2.write(top_10_pages_brand)


#qual o preço medio por marca
st.subheader('Preço medio por marca')
col1,col2 = st.columns([4,2])
precio_medio = df.groupby('brand')['current_price'].mean().round(2).sort_values(ascending=False)
col1.bar_chart(precio_medio)
col2.write(precio_medio)




# #qual a satisfação por marca
# review_brand = df.groupby('brand')['review'].count().sort_values(ascending=False)
# print(review_brand)
olympikus = df[df['brand'] == 'OLYMPIKUS']['current_price']
st.dataframe(olympikus)