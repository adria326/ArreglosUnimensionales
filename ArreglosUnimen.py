# Solicitar la cantidad de temperaturas.
# Inicializar una lista para almacenar las temperaturas
# Solicitar al usuario que ingrese las temperaturas
# Determinar cuántas temperaturas son superiores o iguales a la media
num_temperaturas = int(input("¿Cuántas temperaturas desea ingresar? "))

temperaturas = []

for i in range(num_temperaturas):
    temp = float(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(temp)
    
media = sum(temperaturas) / len(temperaturas)
contador = sum(1 for temp in temperaturas if temp >= media)

print(f"\nLa media de las temperaturas es: {media}")
print(f"Número de temperaturas superiores o iguales a la media: {contador}")