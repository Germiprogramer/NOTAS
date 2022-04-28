# NOTAS

El link al repositorio es el siguiente: https://github.com/Germiprogramer/NOTAS.git

_________________________________________________________________________________________________________________________________________________________________________

El dataset empleado es el siguiente: [Student_Performance_new.csv](https://github.com/Germiprogramer/NOTAS/files/8578510/Student_Performance_new.csv)

Al analizar el dataset, podemos encontrar las notas de 1000 alumnos en 3 asignaturas distintas: matemáticas, lectura y escritura. El trabajo consiste en analizar dichos datos.

# Parte 1

A la hora de analizar un dataset, lo primero es sacar los datos relevantes que lo definen. Tales datos son la cantidad de registros, los valores máximos y mínimos, la media, la mediana y la moda. Algunos de estos datos nos ayudarán más tarde a entender el dataset y realizar los histogramas.

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
    

# Parte 2

En la segunda parte, se calculan datos como el rango, ñla desviación típica y los valores extremos. Entre otras cosas, estos datos sirven para averiguar la variedad de la muestra de datos, y la relación que tienen estos entre sí.

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

# Parte 3

En base a los datos recabados, se realizan gráficos para dar un mayor sentido a la muestra.

    import matplotlib.pyplot as plt
    from analisis import max_value, min_value, notas_mates, notas_lectura, notas_escritura, l, media_mates, media_lectura, media_escritura
    from dispersion import q1_mates, q1_lectura, q1_escritura, q3_mates, q3_lectura, q3_escritura, mediana_escritura, mediana_lectura, mediana_mates

    class Grafico():
        def __init__(self, lista, media, mediana, cuartil_1, cuartil_2, cuartil_3):
            self.lista = lista
            self.media = media
            self.mediana = mediana
            self.cuartil_1 = cuartil_1
            self.cuartil_2 = cuartil_2
            self.cuartil_3 = cuartil_3

        def visualizacion(self):  

            plt.subplot(2, 2, 1)  
            plt.hist(self.lista)  
            plt.title("Histograma y media")  
            plt.axvline(self.media, color='red', linestyle='dashed',  
            linewidth=1,label = str(self.media))  
            plt.legend(loc='upper right')  

            plt.subplot(2, 2, 2)  
            plt.hist(self.lista)  
            plt.title("Histograma y mediana")  
            plt.axvline(self.mediana, color='green', linestyle='dashed',  
            linewidth=1,label = str(self.mediana))  
            plt.legend(loc='upper right')  

            plt.subplot(2, 2, 3)  
            plt.hist(self.lista)  
            plt.title("Histograma y cuartiles")  
            plt.axvline(self.cuartil_1, color='orange', linestyle='dashed',  
            linewidth=1,label = "Q1: "+str(self.cuartil_1))  
            plt.axvline(self.cuartil_2, color='orange', linestyle='dashed',  
            linewidth=1,label = "Q2: "+str(self.cuartil_2))  
            plt.axvline(self.cuartil_3, color='orange', linestyle='dashed',  
            linewidth=1,label = "Q3: "+str(self.cuartil_3))  
            plt.legend(loc='upper right')  

            plt.subplot(2, 2, 4)  
            plt.boxplot(self.lista)  
            plt.title("Diagrama de caja y bigotes")  
            plt.show() 

    grafico_mates = Grafico(notas_mates, media_mates, mediana_mates, q1_mates, mediana_mates, q3_mates)

    grafico_mates.visualizacion()

    grafico_lectura = Grafico(notas_lectura, media_lectura, mediana_lectura, q1_lectura, mediana_lectura, q3_lectura)

    grafico_lectura.visualizacion()

    grafico_escritura = Grafico(notas_escritura, media_escritura, mediana_escritura, q1_escritura, mediana_escritura, q3_escritura)

    grafico_escritura.visualizacion()
    
<img width="457" alt="2022-04-28 (3)" src="https://user-images.githubusercontent.com/91720991/165650308-389bdaa8-8a06-459b-a0c0-7ce930671753.png">
<img width="452" alt="2022-04-28 (6)" src="https://user-images.githubusercontent.com/91720991/165650375-3c681cd5-6<img width="452" alt="2022-04-28 (5)" 
<img width="479" alt="2022-04-28 (4)" src="https://user-images.githubusercontent.com/91720991/165650438-02f21cca-545d-4bb1-95bf-b3fabde536c9.png">


En conclusión, al ver que la desviacón típica no es muy grande, se muestra que los datos están bastante centrados.


