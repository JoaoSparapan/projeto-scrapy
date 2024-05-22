import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('../data/scrapping.db')

df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

conn.close()

st.title('Workshop - Web Scrapping ML')

st.subheader('KPIs do sistema')
c1,c2,c3 = st.columns(3)

#KPI 1 - Total de itens
total_itens = df.shape[0]
c1.metric(label="Número total de itens", value=total_itens)

#KPI 2 - Marcas únicas
unique_brands = df['brand'].nunique()
c2.metric(label="Número de marcas únicas", value=unique_brands)

#KPI 3 - Preço médio em reais
average_new_price = df['new_price'].mean()
c3.metric(label="Preço médio (R$)", value=f"{average_new_price:.2f}")

#KPI 4 - Marcas são mais encontradas até página 10
st.subheader('Marcas mais encontradas até a 10ª página')
c1, c2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
c1.bar_chart(top_10_pages_brands)
c2.write(top_10_pages_brands)

#KPI 5 - Preço médio por marca
st.subheader('Preço médio por marca')
c1, c2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
c1.bar_chart(average_price_by_brand)
c2.write(average_price_by_brand)

#KPI 6 - Satisfação por marca
st.subheader('Satisfação por marca')
c1, c2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
c1.bar_chart(satisfaction_by_brand)
c2.write(satisfaction_by_brand)