# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Some todos os números de 1 até 100

# COMMAND ----------

soma = 0
for i in range(101):
    soma+=i
print(soma)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Some todos os números pares de 1 até 100

# COMMAND ----------

soma = 0
for i in range(100):
  if i % 2:
    soma+= i + 1
print(soma)



# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Some todos os números ímpares de 1 até 100

# COMMAND ----------

soma = 0
for i in range(100):
  resto = i / 2
  if resto % 1:
    soma+= i
print(soma)



# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Dada a lista abaixo, some todos os elementos inteiros positivos

# COMMAND ----------

lista = [-2, 2, 'celular', 10, -99, False]
lista

# COMMAND ----------

n = lista[1]  
i = lista[3]
 
print(n+i)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Dada a String

# COMMAND ----------

string = 'pYthOn É A mELhoR LiNguaGEM De PRoGRaMaçãO'
string

# COMMAND ----------

# MAGIC %md
# MAGIC Formate-a com as primeiras letras maiúsculas:

# COMMAND ----------

string.title()

# COMMAND ----------

# MAGIC %md
# MAGIC Com todas as letras minúsculas

# COMMAND ----------

string.upper()

# COMMAND ----------

# MAGIC %md
# MAGIC Com todas as letras maiúsculas

# COMMAND ----------

string.lower()

# COMMAND ----------

