from analisis import max_value, min_value, notas_mates, notas_lectura, notas_escritura, l, media_mates, media_lectura, media_escritura

import pandas as pd

# 1. EL RANGO
print("1. RANGO")

print("El rango de las notas de las tres asignaturas es {}".format(max_value - min_value))

# 2. DESVIACIÓN TÍPICA
print("2. DESVIACIÓN TÍPICA")

lista_var_mates = []

for i in range(l):
    lista_var_mates.append((notas_mates[i] - media_mates)**2)
print("La varianza de las notas de mates es {}".format((sum(lista_var_mates)/l)))

print("La desviación típica de las notas de mates es {}".format((sum(lista_var_mates)/l)**0.5))

print("Teniendo en cuenta que el rango es 1, dicha desviación típica implica que las notas no están especialmente dispersadas")

lista_var_lectura = []

for i in range(l):
    lista_var_lectura.append((notas_lectura[i] - media_lectura)**2)
print("La varianza de las notas de lectura es {}".format((sum(lista_var_lectura)/l)))

print("La desviación típica de las notas de lectura es {}".format((sum(lista_var_lectura)/l)**0.5))

print("Teniendo en cuenta que el rango es 1, dicha desviación típica implica que las notas no están especialmente dispersadas")

