import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import chardet

# Função para carregar os dados do CSV
def load_csv_data(file_path='csv/IOT-temp.csv'):
    data = pd.read_csv(file_path, encoding='utf-8')
    return data

# Carregar os dados do CSV
df = load_csv_data()
def load_csv_data(file_path='csv/IOT-temp.csv'):
    
# Detectar a codificação do arquivo
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
        print(f"Detected encoding: {encoding}")
    
    # Carregar o CSV com a codificação detectada
    data = pd.read_csv(file_path, encoding=encoding)
    return data


# Exibir as primeiras linhas para verificar
st.write(df.head())

# Criar uma conexão com o PostgreSQL
engine = create_engine('postgresql://postgres:453900@localhost:5432/temperatura')


# Função para inserir os dados no banco
def inserir_dados(df):
    df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
    st.write("Dados inseridos com sucesso!")

# Insere os dados do CSV no PostgreSQL
inserir_dados(df)

# Conexão com o banco de dados para carregar os dados
engine = create_engine('postgresql://postgres:453900@localhost:5432/postgres')  # Altere 'sua_senha'

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp')
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por horas
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem')
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'])
st.plotly_chart(fig3)