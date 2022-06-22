'''
Ejercicio 4:
Ingresar los 3 lados de un triángulo en indicar cuál es su perímetro y cuál es su
superficie (área).
'''

lado1 = int(input("Ingrese el primer lado:", ))
lado2 = int(input("Ingrese el segundo lado:", ))
lado3 = int(input("Ingrese el tercer lado:", ))

perimetro = lado1 + lado2 + lado3

semiPerimetro = (perimetro / 2)
#heron = (semiPerimetro) ** 0.5 #raíz cuadrada
#area = base * altura / 2

area =(semiPerimetro * (semiPerimetro - lado1) * (semiPerimetro - lado2) * (semiPerimetro - lado3)) ** 0.5

print("El períetro del triángulo es: ", perimetro)
print("El períetro del área es: ", round(area, 2))
