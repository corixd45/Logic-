#Operadores

#Operadores Aritmericos

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"DivisionEntera: 10 // 3 = {10 // 3}")

#Operadores Comparacion
print(f"Igualdad: 10 == 3 Is {10 == 3}")
print(f"Desigualdad: 10 != 3 Is {10 != 3}")
print(f"Mayor Que: 10 > 3 Is {10 > 3}")
print(f"Menor Que: 10 < 3 Is {10 < 3}")
print(f"Mayor igual Que: 10 >= 3 Is {10 >= 3}")
print(f"Menor igual  Que: 10 <= 3 Is {10 <= 3}")

#Operadores Logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 is {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 is {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

#Operadores De Asignacion
my_number = 4 #asignacion
print(my_number)
my_number += 1 #suma asiganacion
print(my_number)

my_number -= 1 #Resta  
print(my_number)

my_number  *= 2 #Mutipliacion
print(my_number)

my_number  /= 2 #Division
print(my_number)

my_number  %= 2 #Modulo
print(my_number)

my_number  **= 2 #exponente
print(my_number)

my_number  //= 2 #Division Entera
print(my_number)

#Operadores De Identidad

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'a' in 'andy' = {'y' in 'andy'}")
print(f"'x' not in 'andy' = {'b' not in 'andy'}")

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

#Estructuras De Control
#1-Condicionales

my_string = "Andy"

if my_string == "Andy":
    print("my_string es 'Andy'")
elif my_string == "Andys":
    print("my_string es 'Bencomo'")
else:
    print("my_string no es 'Andy' ni 'Bencomo'")

    # Iterativas

for i in range(10):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1


    # Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

    # DIFICULTAD EXTRA (opcional):
 # Crea un programa que imprima por consola todos los números comprendidos
 # entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 #
 # Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 
 #Solucion 

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)