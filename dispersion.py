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

lista_var_escritura = []

for i in range(l):
    lista_var_escritura.append((notas_escritura[i] - media_escritura)**2)
print("La varianza de las notas de escritura es {}".format((sum(lista_var_escritura)/l)))

print("La desviación típica de las notas de escritura es {}".format((sum(lista_var_escritura)/l)**0.5))

print("Teniendo en cuenta que el rango es 1, dicha desviación típica implica que las notas no están especialmente dispersadas")

# 3. CUARTILES Y RANGO INTERCUARTILICO

print(" 3.1 CUARTILES")
valor_q1 = int(l/4)
valor_q3 = int(3*l/4)
valor_medio = int(l/2)

q1_mates = (notas_mates[valor_q1] + notas_mates[valor_q1 + 1])/2
mediana_mates = (notas_mates[valor_medio] + notas_mates[valor_medio + 1])/2
q3_mates = (notas_mates[valor_q3] + notas_mates[valor_q3 + 1])/2

print("El 25% de los valores de mate son menores que {}".format(q1_mates))
print("El 50% de los valores de mate son menores que {}".format(media_mates))
print("El 75% de los valores de mate son menores que {}".format(q3_mates))

q1_lectura = (notas_lectura[valor_q1] + notas_lectura[valor_q1 + 1])/2
mediana_lectura = (notas_lectura[valor_medio] + notas_lectura[valor_medio + 1])/2
q3_lectura = (notas_lectura[valor_q3] + notas_lectura[valor_q3 + 1])/2

print("El 25% de los valores de lectura son menores que {}".format(q1_lectura))
print("El 50% de los valores de lectura son menores que {}".format(media_lectura))
print("El 75% de los valores de lectura son menores que {}".format(q3_lectura))

q1_escritura = (notas_escritura[valor_q1] + notas_escritura[valor_q1 + 1])/2
mediana_escritura = (notas_escritura[valor_medio] + notas_escritura[valor_medio + 1])/2
q3_escritura = (notas_escritura[valor_q3] + notas_escritura[valor_q3 + 1])/2

print("El 25% de los valores de escritura son menores que {}".format(q1_escritura))
print("El 50% de los valores de escritura son menores que {}".format(media_escritura))
print("El 75% de los valores de escritura son menores que {}".format(q3_escritura))

print("3.2 RANGO INTERCUARTILICO")

print("Rango intercuartílico mates = {}".format(q3_mates-q1_mates))
print("Rango intercuartílico lectura = {}".format(q3_lectura-q1_lectura))
print("Rango intercuartílico escritura = {}".format(q3_escritura-q1_escritura))

# 4. OUTLIERS
limiteInferior_mates = q1_mates - (1.5 * (q3_mates-q1_mates))  
limiteSuperior_mates = q3_mates + (1.5 * (q3_mates-q1_mates))

outliers_mates = []

for i in range(l):
    if notas_mates[i] < limiteInferior_mates or notas_mates[i] > limiteSuperior_mates:
        outliers_mates.append(notas_mates[i])

print("Los outliers de mates son:")
print(outliers_mates)

limiteInferior_lectura = q1_lectura - (1.5 * (q3_lectura-q1_lectura))  
limiteSuperior_lectura = q3_lectura + (1.5 * (q3_lectura-q1_lectura))

outliers_lectura = []

for i in range(l):
    if notas_lectura[i] < limiteInferior_lectura or notas_lectura[i] > limiteSuperior_lectura:
        outliers_lectura.append(notas_lectura[i])

print(outliers_lectura)

limiteInferior_escritura = q1_escritura - (1.5 * (q3_escritura-q1_escritura))  
limiteSuperior_escritura = q3_escritura + (1.5 * (q3_escritura-q1_escritura))

outliers_escritura = []

for i in range(l):
    if notas_escritura[i] < limiteInferior_escritura or notas_escritura[i] > limiteSuperior_escritura:
        outliers_escritura.append(notas_escritura[i])

print(outliers_escritura)

