import requests 

link = http://minhaapi.rafael.rpl.co

requisicao = requests.get(link)

dicionario = requisicao.json()

print(dicionario['total_vendas'])

print(requisicao)
print(requisicao.json())