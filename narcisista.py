# -*- coding: utf-8 -*-
"""narcisista.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PNIuek_uMQ-l8zA2fzyHG-Fvs6jTa6ih
"""

numero = input("Digite um número:")
numeros = list(numero)
tamanho = len(numeros)
potencia = tamanho
total = 0

for i in numeros:
  total += int(i) ** potencia

if (int(numero) == total):
  print("Ah danadinho, seu narcisita")
else:
  print("Humilde de mais")