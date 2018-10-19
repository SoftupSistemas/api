
#------------------------------------#
#  SISTEMA GESTAO ONLINE API
#  adquirindo estoque atual
#  autor: softupsistemas
#-------------------------------------#


#importa modulo sys
import sys

# importando a biblioteca de requisições
import requests 

# importando a biblioteca de JSON
import json 
  
# definindo url da requisicao
url_request = "https://www.sistemagestaoonline.com.br/sistema/rest/api_sgo.wsconsultaestoque"
  
# definindo produto referencia 
produtoReferencia = "123"

# montando header
header = {'Content-type': 'application/json'}

# definindo chave de acesso 
chaveAcesso = "et53r4g934j90tj39gjhy93jy39jg93=gb"
  
# montando body da requisição 
data = {'Chave':chaveAcesso, 
        'ProdutoReferencia':produtoReferencia} 
  
# fazendo requisição POST
r = requests.post(url = url_request, data = data, headers = header) 
  
# extracting data in json format 
data = r.json() 

# printa resposta
print(data)