# archivos.py
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ejemplos_archivos():
    # Leer CSV
    df = pd.read_csv('datos.csv')
    df.head()

    # Estadísticas básicas
    df.describe()
    print(df['Parcial 1'].mean())
    print(df['Parcial 1'].min())
    print(df['Parcial 1'].max())

    # Promedio por fila y estatus
    df['prom'] = df[['Parcial 1','Parcial 2','Parcial 3']].mean(axis=1)
    df['estatus'] = np.where(df['prom']>=7, 'Aprobado', 'Reprobado')
    print(df)

    # Gráfico evolución alumno
    alumno = 5
    notas = df[df['ID']==alumno][['Parcial 1','Parcial 2','Parcial 3']].iloc[0]
    plt.plot(['Parcial 1','Parcial 2','Parcial 3'], notas)
    plt.ylim(0,10)
    plt.ylabel('Calificaciones')
    plt.title('Evolución del alumno')
    plt.show()

    # Leer y modificar Excel
    df = pd.read_excel('datos.xlsx')
    df['prom'] = df[['Parcial 1','Parcial 2','Parcial 3']].mean(axis=1)
    df['estatus'] = np.where(df['prom']>=7,'Aprobado','Reprobado')
    df.to_excel('datos_mod.xlsx', index=False)

    # Gráfico línea simple
    tiempo = [1,4,6,8,10,12]
    temperatura = [20,23,27,25,23,19]
    plt.plot(tiempo, temperatura)
    plt.xlabel('Tiempo (hrs)')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.show()

    # Gráfico barras
    categorias = ['A','B','C','D','E']
    valores = [5,7,3,8,6]
    plt.bar(categorias, valores)
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.title('Gráfico de barras ejemplo')
    plt.show()

    # NumPy: arrays
    temps = np.array([20,23,27,25,23,19])
    print('Temperaturas: ', temps)
    print('Promedio: ', temps.mean())
    print('Mínimo: ', temps.min())
    print('Máximo: ', temps.max())

    voltajes = np.array([5,5,5,5])
    corrientes = np.array([1,2,3,4])
    potencias = voltajes * corrientes
    print('Potencias: ', potencias)

    calificaciones = np.array([60,70,45,67,89,34,23,4,56,65,98])
    plt.hist(calificaciones, bins=5, color='lightblue', edgecolor='black')
    plt.xlabel('Calificaciones')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Calificaciones')
    plt.show()
