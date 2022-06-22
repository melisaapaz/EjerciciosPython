'''
Ejercicio 2:
Tres personas invierten dinero para fundar una empresa (no necesariamente en partes
iguales). Calcular qué porcentaje invirtió cada una.
'''


inversionPersona1 = float(input("Ingrese el monto invertido de la persona 1:", ))
inversionPersona2 = float(input("Ingrese el monto invertido de la persona 2:", ))
inversionPersona3 = float(input("Ingrese el monto invertido de la persona 3:", ))

calculo = inversionPersona1 + inversionPersona2 + inversionPersona3

porcentePersona1 = ((inversionPersona1 * 100) / calculo)
porcentePersona2 = ((inversionPersona2 * 100) / calculo)
porcentePersona3 = ((inversionPersona3 * 100) / calculo)

print("La inversión total es: " , round(calculo, 2))
print("El porcentaje del primer inversionista es: ", round(porcentePersona1, 2) )
print("El porcentaje del segundo inversionista es: ", round(porcentePersona2, 2) )
print("El porcentaje del tercer inversionista es: ", round(porcentePersona3,  2) )

