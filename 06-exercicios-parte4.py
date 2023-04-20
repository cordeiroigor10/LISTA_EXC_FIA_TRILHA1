# Databricks notebook source
# MAGIC %md
# MAGIC ### 21. Crie um programa em Python que receba uma string como entrada e imprima a string sem as vogais.

# COMMAND ----------

a = "textao"
vogais = "aeiou"

novo_texto = ""
for letra in a:
    if letra in vogais:
        #novo_texto += letra
        novo_texto += ""
    else:
        novo_texto += letra
print(novo_texto)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 22. Crie um programa em Python que imprima a soma dos n primeiros números primos, onde n é um número fornecido pelo usuário.

# COMMAND ----------

#n = int(input("Digite um número: "))
#
numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
soma = 0
n = int(input("Digite um número: "))

for i in range(n):
  soma = soma + numeros_primos[i]
  
print(soma)
#    
#
#
#
#print(list_primos)
#  

# COMMAND ----------

# MAGIC %md
# MAGIC ### 23. Crie um programa em Python que receba uma lista de números e imprima a soma dos números pares e a soma dos números ímpares presentes na lista.

# COMMAND ----------

lista = [10, 20, 30, 40, 50]

sum(lista)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 24. Crie um programa em Python que receba uma lista de strings e retorne uma lista com todas as strings que começam e terminam com a mesma letra.

# COMMAND ----------

palavras = ["amor", "futebol", "verdade", "banana", "arara", "casa", "sol"]

palavras_selecionadas = []
def strings_inic (tupla):
  string_iguais = list(filter(lambda s: s[0] == s[-1], palavras))
  return string_iguais

string_iguais = strings_inic(palavras)

print(string_iguais)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 25. Crie um programa em Python que leia um número do usuário e verifique se ele é um número perfeito. Um número perfeito é aquele que é igual à soma de seus divisores próprios (ou seja, a soma de seus fatores inteiros positivos, excluindo ele próprio).

# COMMAND ----------

numero = int(input("Digite um número: "))

soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0: 
        soma_divisores += i  

if soma_divisores == numero:  # Se a soma dos divisores for igual ao número
    print(f"{numero} é um número perfeito")
else:
    print(f"{numero} não é um número perfeito")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 26. Crie um programa em Python que calcule a série de Fibonacci para um determinado número de termos fornecido pelo usuário. A série de Fibonacci é uma sequência em que cada número é a soma dos dois números anteriores: 0, 1, 1, 2, 3, 5, 8, 13, ...

# COMMAND ----------

termos = int(input("Digite o número de termos desejados: "))


n1, n2 = 0, 1
count = 0


if termos <= 0:
   print("Insira um numero positivo")

elif termos == 1:
   print("Sequencia Fibonacci: ",termos,":")
   print(n1)

else:
   print("Sequencia Fibonacci: ")
   while count < termos:
       print(n1)
       nth = n1 + n2
       # atualizando valores
       n1 = n2
       n2 = nth
       count += 1

# COMMAND ----------

