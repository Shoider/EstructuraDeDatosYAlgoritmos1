'''
Sistema indicador de color de semáforo COVID
Proyecto Final Estructura de Datos y Algoritmos 1. Alumno: Hernandez Solis Brandon. Grupo: 15
'''
#Importar librerias necesarias
import os
import csv
#Limpiar pantalla
os.system("cls")
#Declarar variables
op='0'
edadProm=0
contInfec=0
i=0
baseDeDatos='bd.csv'
#Creamos funcion para decir el color del semaforo
def semaforo(contInfec):
    if contInfec == 0:
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Verde')
    elif contInfec > 0 and contInfec <= 30:
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Amarillo')
    elif contInfec > 30 and contInfec <= 70:
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Naranja')
    elif contInfec > 70 and contInfec <= 100:
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Rojo')
#Abrimos la base de datos y guardamos el contenido en la lista datos
with open(baseDeDatos) as f:
    bd=csv.reader(f)
    datos=list(bd)
#Leemos los datos para saber si tienen covid y saber la edad de los contagiados
for i in range(0,99):
    ind=float(datos[i][2])
    if ind>=0.8:
        contInfec=contInfec+1
        edadProm=edadProm+int(datos[i][1])
#Ejecutamos la funcion para saber el color del semaforo
print('\nSistema Indicador De Color De Semáforo COVID')
semaforo(contInfec)
#Mostramos la edad promedio de los contagiados
print("\nEdad promedio de los contagiados:",int(edadProm/contInfec),'años')