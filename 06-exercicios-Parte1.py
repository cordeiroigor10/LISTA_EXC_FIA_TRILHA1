# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Crie um programa em Python que receba uma string como entrada e imprima uma nova string com os caracteres na ordem inversa.

# COMMAND ----------

txt = "ABCDEF"
a = txt[::-1]
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as palavras em ordem inversa.

# COMMAND ----------

txt = "esta frase ficou de forma diferente"
txt = txt.title()
a = txt[::-1]
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as vogais substituídas por asteriscos (*)

# COMMAND ----------

vogais = "aeiouAEIOU"
novo_texto = ""
for letra in a:
    if letra in vogais:
        #novo_texto += letra
        novo_texto += "*"
    else:
        novo_texto += letra
print(novo_texto)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as palavras que começam com letra maiúscula.

# COMMAND ----------

palavras = txt.split()
palavras_invertidas = palavras[::-1]
texto_invertido = " ".join(palavras_invertidas)
print(texto_invertido)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Crie um programa em Python que receba uma string como entrada e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda).

# COMMAND ----------

texto1 = input("Digite a primeira string: ")
texto2 = texto1.replace(" ", "")
palavras_invertidas = texto2[::-1]
palavras_invertidas_1 = palavras_invertidas.replace(" ", "")

if palavras_invertidas_1 == texto2:
  print("é palíndromo")
else:
  print("não é palíndromo")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 6. Crie um programa em Python que receba uma string como entrada e verifique se ela é um anagrama de outra string. (ou seja, se elas possuem as mesmas letras em quantidades diferentes)

# COMMAND ----------

texto = [input("digite string: ")]
texto1= [input("digite string: ")]


#palavras_invertidas_1 = texto[::-1]
#palavra_sem_espaco = [texto].replace(" ", "")
#
#palavras_invertidas_2 = texto1[::-1]
#palavra_sem_espaco1 = [texto1].replace(" ", "")

texto2 = texto.sort()
texto3 = texto1.sort()

if texto2 == texto3:
  print("palavra é anagrama")
else:
  print("não é")



# COMMAND ----------

# MAGIC %md
# MAGIC ### 7. Crie um programa em Python que receba uma string como entrada e imprima outra string que é formada pela primeira letra de cada palavra da string original.

# COMMAND ----------

texto = input("Digite uma string: ")
print(texto[0])

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### 8. Crie um programa em Python que receba uma tupla de números inteiros como entrada e retorne uma nova tupla contendo apenas os números primos.

# COMMAND ----------

numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

primos = []
for num in numeros:
  if num > 1:
    for i in range(2, num):
      if (num % i == 0):
        break
      else:
        primos.append(num)
        
def remove_repetidos(primos):
    l = []
    for i in primos:
        if i not in l:
            l.append(i)
    l.sort()
    return l
  
primos = remove_repetidos(primos)
tupla_primos = tuple(primos)

#tupla_primos_remove = tupla_primos.removeDuplicates()
print(tupla_primos)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 9. Crie um programa em Python que receba duas tuplas de números inteiros como entrada e retorne uma nova tupla contendo apenas os elementos que aparecem em ambas as tuplas.

# COMMAND ----------

numeros = (1, 2, 3, 4, 5)
numeros_1 = (2, 5, 6, 7, 8, 9, 10)

tupla_new = tuple(set(numeros).intersection(numeros_1))
print(tupla_new)
#numeros.extend(numeros_1);

# COMMAND ----------

# MAGIC %md
# MAGIC ### 10. Crie um programa em Python que receba uma tupla de strings como entrada e retorne uma nova tupla contendo apenas as strings que começam e terminam com a mesma letra.

# COMMAND ----------

tupla = ("arara", "casa", "mala", "ovo", "paralelepípedo", "pato")

def strings_inic (tupla):
  string_iguais = tuple(filter(lambda s: s[0] == s[-1], tupla))
  return string_iguais

string_iguais = strings_inic(tupla)

print(string_iguais)

# COMMAND ----------

