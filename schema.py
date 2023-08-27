#Cria explicitamente o schema da tabela no Bigquery, não é obrigatório, mas se não explicitar o bigquery vai setar os tipos automaticamente
def type_gcp():
    schema = [
        {'Zip Code':'BIGNUMERIC'},
        {'City':'STRING'},
        {'County':'STRING'}
    ]