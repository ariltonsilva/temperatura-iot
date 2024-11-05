# Dashboard IoT de Monitoramento de Temperatura

Este projeto é um **dashboard IoT** desenvolvido com **Streamlit** para monitorar e analisar dados de temperatura provenientes de dispositivos IoT. Os dados são carregados de um arquivo CSV e armazenados em um banco de dados **PostgreSQL** para exibição em gráficos interativos com **Plotly**.

## Funcionalidades

- **Detecção automática de codificação**: Utiliza `chardet` para detectar a codificação do CSV e garantir a leitura correta dos dados.
- **Armazenamento no PostgreSQL**: Insere e armazena os dados de temperatura no banco de dados PostgreSQL.
- **Visualizações interativas**:
  - Gráfico de média de temperatura por dispositivo.
  - Gráfico de contagem de leituras por hora.
  - Gráfico de temperaturas máximas e mínimas por dia.

## Requisitos

- **Python 3.12**
- **Streamlit**
- **Pandas**
- **Plotly**
- **SQLAlchemy**
- **chardet**
- **PostgreSQL**

### Instalação das Dependências

Instale as bibliotecas necessárias com o comando:

```bash
pip install streamlit pandas plotly sqlalchemy chardet psycopg2
```

> **Nota**: Certifique-se de que o PostgreSQL esteja instalado e configurado em seu sistema.

## Configuração do Banco de Dados

1. **Configure o PostgreSQL**:
   - Substitua as informações da conexão com o banco de dados (usuário, senha e nome do banco) na URL da conexão (`postgresql://usuario:senha@localhost:porta/nome_do_banco`).
   - Crie as views no banco de dados para `avg_temp_por_dispositivo`, `leituras_por_hora`, e `temp_max_min_por_dia`, para exibir os dados nos gráficos adequados.

2. **Arquivo CSV**:
   - Verifique se o arquivo CSV está no caminho correto (`csv/IOT-temp.csv`) e com o nome especificado. 

## Estrutura do Código

1. **Função `load_csv_data()`**:
   - Detecta a codificação do arquivo CSV e carrega os dados em um DataFrame.
  
2. **Função `inserir_dados()`**:
   - Insere os dados carregados do CSV no banco de dados PostgreSQL.

3. **Função `load_data()`**:
   - Carrega dados de uma view específica no banco de dados para exibição no dashboard.

4. **Visualizações com Plotly**:
   - **Média de Temperatura por Dispositivo**: Exibe a média de temperatura para cada dispositivo.
   - **Leituras por Hora do Dia**: Mostra a contagem de leituras ao longo das horas do dia.
   - **Temperaturas Máximas e Mínimas por Dia**: Mostra as temperaturas máximas e mínimas registradas diariamente.

## Executando o Projeto

1. **Insira os dados no PostgreSQL**:
   - Abra o projeto no VS Code ou no terminal, e execute `inserir_dados(df)` para garantir que os dados estejam no banco de dados.

2. **Inicie o Dashboard**:
   - No terminal, rode o comando abaixo para iniciar o Streamlit:

     ```bash
     streamlit run app.py
     ```

     > Substitua `app.py` pelo nome do arquivo, caso ele seja diferente.

3. **Acesse o Dashboard**:
   - O Streamlit iniciará o dashboard no navegador, onde você poderá visualizar e interagir com os gráficos.

## Observações

- Se precisar ajustar a URL de conexão com o PostgreSQL, edite as linhas de criação da engine de conexão no código.
- Certifique-se de que as views no banco de dados estão corretamente configuradas para gerar as visualizações desejadas.
