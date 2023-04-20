# Databricks notebook source
# MAGIC %md
# MAGIC ### 16. Crie um programa em Python que receba uma lista de dicionários como entrada, onde cada dicionário representa um aluno com nome e notas em diferentes disciplinas, e retorne o nome do aluno com a maior média ponderada, sendo que a média ponderada deve ser calculada utilizando as notas como pesos.

# COMMAND ----------

alunos = [{"nome": "João", "notas": {"Matemática": 8.5, "Português": 9.0, "História": 7.0}},
          {"nome": "Maria", "notas": {"Matemática": 9.5, "Português": 8.5, "História": 6.0}},
          {"nome": "Pedro", "notas": {"Matemática": 7.0, "Português": 6.5, "História": 9.0}},
          {"nome": "Ana", "notas": {"Matemática": 8.0, "Português": 7.5, "História": 8.0}}]

# os pesos são, respectivamente: 2, 3, 2
#maior_media = 0
#nome_aluno = ""

maior_media = 0
media = 0
aluno = {}

for classe in alunos:#.items():
    valores = []
    notas = classe['notas']
    for materia, valor in notas.items():
      valores.append(valor)
    media = (valores[0]*2 + valores[1]*3 + valores[2]*2)/7
    if media > maior_media:
      maior_nota = nota
      nome_aluno = nome
      
print(nome_aluno, maior_nota)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 17. Crie um programa em Python que receba três números como entrada e imprima "Maior" se o primeiro número for maior do que a soma dos outros dois, "Menor" se o primeiro número for menor do que a soma dos outros dois, ou "Igual" caso contrário.

# COMMAND ----------

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


if num1 >= num2 + num3:
  print(num1)
else:
  print("Primeiro número menor")
#if num2 >= num1 + num3:
#  print(num2)
#if num3 >= num1 + num2:/
#  print(num2)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 18. Crie um programa em Python que receba a idade e a altura de uma pessoa como entrada e classifique-a de acordo com as seguintes regras: se a idade for menor do que 18 anos e a altura for menor do que 1,60 m, imprimir "Adolescente Baixo"; se a idade for menor do que 18 anos e a altura for maior do que 1,60 m, imprimir "Adolescente Alto"; se a idade for maior ou igual a 18 anos e a altura for menor do que 1,60 m, imprimir "Adulto Baixo"; se a idade for maior ou igual a 18 anos e a altura for maior do que 1,60 m, imprimir "Adulto Alto".

# COMMAND ----------

idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura em metros: "))

if idade < 18:
    if (altura < 1.60):
      print("Adolescente Baixo")
    elif (altura > 1.60):
        print("Adolescente Alto")
  
if idade >= 18:
  if (altura < 1.60):
    print("Adulto Baixo") 
  elif (altura > 1.60):
    print("Adulto Alto")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 19. Crie um programa em Python que receba uma string como entrada e imprima "Palíndromo" se a string for um palíndromo (ou seja, se a string lida de trás para frente for igual à string original), ou "Não Palíndromo" caso contrário.

# COMMAND ----------

texto = input("Digite um texto: ")

texto2 = texto.replace(" ", "")
palavras_invertidas = texto2[::-1]
palavras_invertidas_1 = palavras_invertidas.replace(" ", "")

if palavras_invertidas_1 == texto2:
  print("é palíndromo")
else:
  print("não é palíndromo")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 20. Crie um programa em Python que receba uma lista de números inteiros como entrada e calcule a soma dos quadrados dos números ímpares da lista.

# COMMAND ----------

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for lis in lista:
  if lis % 2:
    soma+=lis
print(soma)

# COMMAND ----------

