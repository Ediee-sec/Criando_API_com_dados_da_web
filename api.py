from flask import Flask, request
from flask import jsonify
import pandas_gbq
import crecentials_gcp


""" 
ESTE MÓDULO É RESPONSÁVEL POR CRIAR A API COM BASE NOS DADOS DO BIGQUERY
"""

app = Flask(__name__)

#Cria a rota principal onde será informado as demais rotas
@app.route('/',methods=['GET'])
def page_one():
    msg = [{'ROUTE MARYLAND':'http://127.0.0.1:5000/maryland'}]
    
    return jsonify(msg)


#Cria a rota da cidade de maryland
@app.route('/maryland', methods=['GET'])
def data_maryland():
    pandas_gbq.context.credentials = crecentials_gcp.conn_gcp()
    pandas_gbq.context.project = "emersondai254"

    df = pandas_gbq.read_gbq("SELECT * FROM homol.Dados_Endereco_Maryland")
    
    data = df.to_dict(orient='records')

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
