'''
Sistema indicador de color de semáforo COVID
Proyecto Final Estructura de Datos y Algoritmos 1. Alumno: Hernandez Solis Brandon. Grupo: 15
'''
#Importar librerias necesarias
import os
import csv
#Declarar variables
edadProm=0
contInfec=0
i=0
#Funcion para limpiar pantalla
def clear():
    os.system("cls")
#Funcion para leer datos y regresar valores en lista
def lecturaDatos(estado):
    if estado==1:
        #Abrimos la base de datos y guardamos el contenido en la lista datos
        with open('bd_Aguascalientes.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        #Escribimos el nombre del estado seleccionado en pantalla
        esc='\nEstado: Aguascalientes'
        print(esc)
        #Guardamos estado seleccionado 'Datos.txt'
        escTex(esc)
    elif estado==2:
        with open('bd_BajaCalifornia.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Baja California'
        print(esc)
        escTex(esc)
    elif estado==3:
        with open('bd_BajaCaliforniaSur.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Baja California Sur'
        print(esc)
        escTex(esc)
    elif estado==4:
        with open('bd_Campeche.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Campeche'
        print(esc)
        escTex(esc)
    elif estado==5:
        with open('bd_Chiapas.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Chiapas'
        print(esc)
        escTex(esc)    
    elif estado==6:
        with open('bd_Chihuahua.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Chihuahua'
        print(esc)
        escTex(esc)
    elif estado==7:
        with open('bd_CiudadDeMexico.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Ciudad De Mexico'
        print(esc)
        escTex(esc)
    elif estado==8:
        with open('bd_Coahuila.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Coahuila'
        print(esc)
        escTex(esc)
    elif estado==9:
        with open('bd_Colima.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Colima'
        print(esc)
        escTex(esc)
    elif estado==10:
        with open('bd_Durango.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Durango'
        print(esc)
        escTex(esc)
    elif estado==11:
        with open('bd_Guanajuato.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Guanajuato'
        print(esc)
        escTex(esc)
    elif estado==12:
        with open('bd_Guerrero.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Guerrero'
        print(esc)
        escTex(esc)
    elif estado==13:
        with open('bd_Hidalgo.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Hidalgo'
        print(esc)
        escTex(esc)
    elif estado==14:
        with open('bd_Jalisco.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Jalisco'
        print(esc)
        escTex(esc)
    elif estado==15:
        with open('bd_EstadoDeMexico.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Estado De Mexico'
        print(esc)
        escTex(esc)
    elif estado==16:
        with open('bd_Michoacan.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Michoacan'
        print(esc)
        escTex(esc)
    elif estado==17:
        with open('bd_Morelos.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Morelos'
        print(esc)
        escTex(esc)
    elif estado==18:
        with open('bd_Nayarit.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Nayarit'
        print(esc)
        escTex(esc)
    elif estado==19:
        with open('bd_NuevoLeon.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Nuevo Leon'
        print(esc)
        escTex(esc)
    elif estado==20:
        with open('bd_Oaxaca.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Oaxaca'
        print(esc)
        escTex(esc)
    elif estado==21:
        with open('bd_Puebla.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Puebla'
        print(esc)
        escTex(esc)
    elif estado==22:
        with open('bd_Queretaro.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Queretaro'
        print(esc)
        escTex(esc)
    elif estado==23:
        with open('bd_QuintanaRoo.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
            esc='\nEstado: Quintana Roo'
        print(esc)
        escTex(esc)
    elif estado==24:
        with open('bd_SanLuisPotosi.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: San Luis Potosi'
        print(esc)
        escTex(esc)
    elif estado==25:
        with open('bd_Sinaloa.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Sinaloa'
        print(esc)
        escTex(esc)
    elif estado==26:
        with open('bd_Sonora.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Sonora'
        print(esc)
        escTex(esc)
    elif estado==27:
        with open('bd_Tabasco.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Tabasco'
        print(esc)
        escTex(esc)
    elif estado==28:
        with open('bd_Tamaulipas.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Tamaulipas'
        print(esc)
        escTex(esc)
    elif estado==29:
        with open('bd_Tlaxcala.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Tlaxcala'
        print(esc)
        escTex(esc)
    elif estado==30:
        with open('bd_Veracruz.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Veracruz'
        print(esc)
        escTex(esc)
    elif estado==31:
        with open('bd_Yucatan.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Yucatan' 
        print(esc)
        escTex(esc)
    elif estado==32:
        with open('bd_Zacatecas.csv') as f:
            bd=csv.reader(f)
            datos=list(bd)
        esc='\nEstado: Zacatecas'
        print(esc)
        escTex(esc)
    #Regresamos datos en la funcion
    return datos
#Funcion para escribir en archivo .txt
def escTex(texto):
    file=open('Datos.txt',"a")
    file.write(texto)
    file.close()
#Funcion para decir el color del semaforo
def semaforo(contInfec):
    #Usamos las estructuras if para elegir el color del semaforo
    if contInfec==0:
        #Mostramos en pantalla el color del semaforo y guardamos en 'Datos.txt'
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Verde')
        esc='\nInfectados: '
        escTex(esc)
        esc=str(contInfec)
        escTex(esc)
        esc='\nColor del semaforo: Verde'
        escTex(esc)
    elif contInfec>0 and contInfec<=30:
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Amarillo')
        esc='\nInfectados: '
        escTex(esc)
        esc=str(contInfec)
        escTex(esc)
        esc='\nColor del semaforo: Amarillo'
        escTex(esc)
    elif contInfec>30 and contInfec<=70:
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Naranja')
        esc='\nInfectados: '
        escTex(esc)
        esc=str(contInfec)
        escTex(esc)
        esc='\nColor del semaforo: Naranja'
        escTex(esc)
    elif contInfec>70 and contInfec<=100:
        print('\nInfectados:',contInfec,'\n\nColor del semaforo: Rojo')
        esc='\nInfectados: '
        escTex(esc)
        esc=str(contInfec)
        escTex(esc)
        esc='\nColor del semaforo: Rojo'
        escTex(esc)
#Funcion para mostrar opciones de estados y obtener seleccion
def opEst():
    #Creamos un ciclo while por si el usuario se equivoca
    e=0
    while(e==0):
        clear()
        #Inicializamos el archivo de texto 'Datos.txt'
        file=open('Datos.txt',"w")
        file.write('\n')
        file.close()
        #Bienvenida al usuario
        esc='\tSistema Nacional\n\nIndicador De Color De Semáforo COVID\n\n'
        print(esc)
        escTex(esc)
        #Pedimos al usuario seleccionar el estado del que desea la informacion
        print('Seleccione el estado del que desea conocer la informacion\n')
        #Mostramos las posibles opciones de estados
        print('1: AGU\t2: BCN\t3: BCS\t4: CAM\t5: CHP\n6: CHH\t7: CMX\t8: COA\t9: COL\t10: DUR')
        print('11: GUA\t12: GRO\t13: HID\t14: JAL\t15: MEX\n16: MIC\t17: MOR\t18: NAY\t19: NLE\t20: OAX')
        print('21: PUE\t22: QUE\t23: ROO\t24: SLP\t25: SIN\n26: SON\t27: TAB\t28: TAM\t29: TLA\t30: VER')
        print('31: YUC\t32: ZAC')
        op=int(input('\nSu opcion en numero: '))
        if op>=1 and op<=32:
            e=1
            clear()
        else:
            input('\n\nOpcion no valida, intente de nuevo...\t')
    return op
#Solicitamos estado seleccionado
estado=opEst()
#Ejecutamos la funcion para obtener los datos del estado seleccionado
datos=lecturaDatos(estado)
#Leemos los datos para saber si tienen covid y saber la edad de los contagiados
for i in range(0,99):
    ind=float(datos[i][1])
    if ind>=0.8:
        contInfec=contInfec+1
        edadProm=edadProm+int(datos[i][0])
#Ejecutamos la funcion para saber el color del semaforo
semaforo(contInfec)
#Mostramos la edad promedio de los contagiados y guardamos 'Datos.txt'
print('\nEdad promedio de los contagiados:',int(edadProm/contInfec),'años')
esc='\nEdad promedio de los contagiados: '
escTex(esc)
esc=str(int(edadProm/contInfec))
escTex(esc)
esc=' años'
escTex(esc)
#Pausa antes de salir
input('\n\nPresione enter para salir...\t')
clear()