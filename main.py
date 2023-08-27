import pandas as pd
import pandas_gbq
import crecentials_gcp
import schema

""" 
ESTE MÓDULO É O PRINCIPAL, RESPONSÁVEL POR LER OS DADOS DO CSV, TRATAR CAMPOS, E CARREGAR NO BIGQUERY
"""

#Le os dados do csv na web, carrega para um dataframe pandas e altera os nomes dos campos
def extract_and_transform_data():
    df = pd.read_csv('https://opendata.maryland.gov/api/views/ryxx-aeaf/rows.csv?accessType=DOWNLOAD', sep=',')
    
    df = df.rename(columns={'Zip Code': 'cod_postal', 'City': 'cidade', 'County': 'condado'})
    
    return df

#Carrega os dados em uma tabela no bigquery, sempre da o replace nos dados
def load_data_to_bigquery():
    pandas_gbq.context.credentials = crecentials_gcp.conn_gcp()
    pandas_gbq.context.project = "emersondai254"

    pandas_gbq.to_gbq(extract_and_transform_data(), 'homol.Dados_Endereco_Maryland', project_id='emersondai254', if_exists='replace',\
                        table_schema=schema.type_gcp())
    
if __name__ == "__main__":    
    load_data_to_bigquery()
    



