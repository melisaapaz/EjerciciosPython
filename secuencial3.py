'''
Ejercicio 3:
Leer un período en segundos e imprimirlo expresado en días, horas, minutos y
segundos.
Por ejemplo, 200.000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos
'''

print ("Introduzca la nota de un estudiante (-1 para salir): ")
grado = int(input())
while grado != -1:
    total = total + grado
    contar = contar + 1
    print ("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
promedio = total / contar
print ("Promedio de notas del grado escolar es: " + str(promedio))