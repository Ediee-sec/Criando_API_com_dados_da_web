from google.oauth2 import service_account

#Cria a conexão com o bigquery, usando a service account json
def conn_gcp():
    key_path = "/home/emerson/Área de Trabalho/Codes/amb_vir_python_3_10_6/Data_Engeenier/ETL/Criando_API_com_dados_da_web/doc/emersondai254-dd3a10e2ae65.json"
    credentials = service_account.Credentials.from_service_account_file(key_path)
    
    return credentials