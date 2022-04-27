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