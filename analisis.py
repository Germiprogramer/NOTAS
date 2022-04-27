import pandas as pd

notas = pd.read_csv("Student_Performance_new.csv", header=0)

#CREAMOS EL DICCIONARIO A PARTIR DE LOS DATOS DEL DATASET

notas_mates = list(notas["math percentage"])
notas_lectura = list(notas["reading score percentage"])
notas_escritura = list(notas["writing score percentage"])

l = len(notas_mates)

for i in range (1,l):
    diccionario = {"notas_mates":notas_mates, "notas_lectura":notas_lectura, "notas_escritura":notas_escritura}
print(l)

#1. Cantidad de observaciones

print("- CANTIDAD DE OBSERVACIONES -")
print("Cantidad de observaciones = {}".format(l))

#2. Valores mínimos y máximos

print("- VALORES MÁXIMOS -")
max_value = None

for num in notas_mates:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor nota MATES:', max_value)

for num in notas_lectura:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor nota LECTURA:', max_value)

for num in notas_escritura:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor nota ESCRITURA:', max_value)

print(" -VALORES MÍNIMOS- ")

min_value = None

for num in notas_mates:
    if (min_value is None or num < min_value):
        min_value = num

print('Mejor nota MATES:', min_value)

for num in notas_lectura:
    if (min_value is None or num < min_value):
        min_value = num

print('Mejor nota LECTURA:', min_value)

for num in notas_escritura:
    if (min_value is None or num < min_value):
        min_value = num

print('Mejor nota ESCRITURA:', min_value)

# 3. MEDIA ARITMÉTICA

print("- NOTAS MEDIAS -")
suma_notas_mates = sum(notas_mates)
media_mates = suma_notas_mates / l
print("La media de Mates es {}".format(media_mates))

suma_notas_lectura = sum(notas_lectura)
media_lectura = suma_notas_lectura / l
print("La media de Lectura es {}".format(media_lectura))

suma_notas_escritura = sum(notas_escritura)
media_escritura = suma_notas_escritura / l
print("La media de Escritura es {}".format(media_escritura))

# 4. MEDIANA
print("- MEDIANA -")
valor_medio = int(l/2)

mediana_mates = (notas_mates[valor_medio] + notas_mates[valor_medio + 1])/2
print("La mediana de las notas de mates es: {}".format(mediana_mates))

mediana_lectura = (notas_lectura[valor_medio] + notas_lectura[valor_medio + 1])/2
print("La mediana de las notas de lectura es: {}".format(mediana_lectura))

mediana_escritura = (notas_escritura[valor_medio] + notas_escritura[valor_medio + 1])/2
print("La mediana de las notas de escritura  es: {}".format(mediana_escritura))

# 5.MODA
print("- MODA -")

diccionario_conteo_mates = {}
for numero in notas_mates:
    clave = str(numero)
   
    if not clave in diccionario_conteo_mates:
        
        diccionario_conteo_mates[clave] = 1
    
    else:
        
        diccionario_conteo_mates[clave] += 1

frecuencia_mayor = 0
numero_mas_repetido = notas_mates[0]

for numero in diccionario_conteo_mates:
    if diccionario_conteo_mates[numero] > frecuencia_mayor:
        numero_mas_repetido = numero
        frecuencia_mayor = diccionario_conteo_mates[numero]

conteo = diccionario_conteo_mates[str(numero_mas_repetido)]
print(f"La nota de mates más repetida es {numero_mas_repetido} (encontrado {conteo} ocasiones)")



diccionario_conteo_lectura = {}
for numero in notas_lectura:
    clave = str(numero)
   
    if not clave in diccionario_conteo_lectura:
        
        diccionario_conteo_lectura[clave] = 1
    
    else:
        
        diccionario_conteo_lectura[clave] += 1

frecuencia_mayor = 0
numero_mas_repetido = notas_lectura[0]

for numero in diccionario_conteo_lectura:
    if diccionario_conteo_lectura[numero] > frecuencia_mayor:
        numero_mas_repetido = numero
        frecuencia_mayor = diccionario_conteo_lectura[numero]

conteo = diccionario_conteo_lectura[str(numero_mas_repetido)]
print(f"La nota de lectura más repetida es {numero_mas_repetido} (encontrado {conteo} ocasiones)")



diccionario_conteo_escritura = {}
for numero in notas_escritura:
    clave = str(numero)
   
    if not clave in diccionario_conteo_escritura:
        
        diccionario_conteo_escritura[clave] = 1
    
    else:
        
        diccionario_conteo_escritura[clave] += 1

frecuencia_mayor = 0
numero_mas_repetido = notas_escritura[0]

for numero in diccionario_conteo_escritura:
    if diccionario_conteo_escritura[numero] > frecuencia_mayor:
        numero_mas_repetido = numero
        frecuencia_mayor = diccionario_conteo_escritura[numero]

conteo = diccionario_conteo_escritura[str(numero_mas_repetido)]
print(f"La nota de escritura más repetida es {numero_mas_repetido} (encontrado {conteo} ocasiones)")
