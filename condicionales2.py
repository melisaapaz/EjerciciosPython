'''
Ejercicio 2: Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea válido e informar en caso que no lo sea.
'''

def calcularMes(unMes):
    if unMes == 1:
        return "Enero"
    elif unMes==2:
        return "Febrero"
    elif unMes==3:
        return "Marzo"
    elif unMes==4:
        return "Abril"
    elif unMes==5:
        return "Mayo"
    elif unMes==6:
        return "Junio"
    elif unMes==7:
        return "Julio"
    elif unMes==8:
        return "Agosto"
    elif unMes==9:
        return "Septiembre"
    elif unMes==10:
        return "Octubre"
    elif unMes==11:
        return "Noviembre"
    elif unMes==12:
        return "Diciembre"
    else:
        return "Hasta luego..."

bandera = 1
while bandera > 0:
    opcion = int(input("Ingrese un nro. de mes o 0 para salir: "))
    bandera = opcion
    if (bandera < 1 and bandera != 0) or bandera >= 12:
        print("Opción incorrecta")
        bandera = 1
        continue
    else:
        print(calcularMes(opcion))

