# Databricks notebook source
# MAGIC %md
# MAGIC ### 11. Crie um programa em Python que receba uma lista de números inteiros como entrada e retorne uma nova lista contendo apenas os números que aparecem um número ímpar de vezes.

# COMMAND ----------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]

numeros.sort()

impares = []
pares = []

for num in numeros:
  if num % 2:
    impares.append(num)
  else:
    pares.append(num)
    
print(impares)
print(pares)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 12. Crie um programa em Python que receba duas listas de números inteiros como entrada e retorne uma nova lista contendo apenas os elementos que aparecem em pelo menos uma das listas, mas não em ambas.

# COMMAND ----------

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [4, 5, 6, 7, 8, 9, 10]

new_list = list(set(lista1).difference(lista2))
print(new_list)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 13. Crie um programa em Python que receba duas listas de números inteiros como entrada e retorne uma nova lista contendo apenas os elementos que aparecem em ambas as listas, mas sem repetições.

# COMMAND ----------

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

new_list = list(set(lista1).intersection(lista2))
print(new_list)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 14. Crie um programa em Python que receba uma lista de dicionários como entrada, onde cada dicionário representa um produto com nome e preço, e retorne o nome do produto mais caro.

# COMMAND ----------

produtos = [{"nome": "celular", "preco": 1500},
            {"nome": "notebook", "preco": 3500},
            {"nome": "tablet", "preco": 1200},
            {"nome": "fones de ouvido", "preco": 200},
            {"nome": "smartwatch", "preco": 800}]


preco_maior = 0
nome_produto_mais_caro = ""

for produto in produtos:
    prod = produto['nome']
    preco = produto['preco']
    if preco > preco_maior:
      preco_maior = preco
      nome_produto_mais_caro = prod
      


print(nome_produto_mais_caro, preco_maior)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 15. Crie um programa em Python que receba um dicionário como entrada, onde as chaves representam nomes de produtos e os valores representam as quantidades disponíveis em estoque, e retorne o nome do produto com estoque mais baixo.

# COMMAND ----------

estoque = {"celular": 50, "notebook": 20, "tablet": 100, "fones de ouvido": 5, "smartwatch": 15}


#vou explicar só p vc entender melhor:

#nome_produto = min(estoque, key=estoque.get)
#
#Utilizamos o min para encontrar o valor minimo do estoque (dicionario). A função min recebe dois argumentos, no caso, o dicionario (estoque) e o argumento key, que é uma função que especifica como os elementos do iterável devem ser comparados para determinar o mínimo, no caso, passamos estoque.get como o valor do argumento key, que é uma função que retorna o valor associado a uma chave em um dicionario.
#
#Ai retorna a chave do dicionário que tem o valor mínimo com base nos valores do dicionário estoque, e essa chave é armazenada na variável nome_produto.
#
#Utilizamos a chave obtida nome_produto para acessar o valor correspondente no dicionário utilizando estoque[nome_produto]. 
#
#qntd_menor = estoque[nome_produto] 
#
#print(nome_produto, qntd_menor)

#nome_produto = min(estoque, key=estoque.get)
#qntd_menor = estoque[nome_produto]
#
#print(nome_produto, qntd_menor)
#
#estoque_menor = 10000
#nome_produto = ""
##valor = estoque.values()
#prod = estoque.keys()

#for est in estoque.items():
#    prod = estoque.keys()
#    qntd = estoque.values()
#    if  qntd < estoque_menor:
#      estoque_menor = qntd
#      nome_produto = prod
      
for nome, qtd in estoque.items():
  if qtd < estoque_menor:
    estoque_menor = qtd
    produto = nome

print(produto, estoque_menor)
    
    #print(nome_produto, estoque_menor)