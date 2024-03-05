import random  # Importar el módulo random para generar números aleatorios
import time    # Importar el módulo time para medir el tiempo de ejecución

# Inicialización de la variable de control del bucle
A = False  

# Imprimir encabezado
print("Ejercicio 2 Practica 1 Sistema de Ecuaciones por busqueda Aleatoria\n")

# Bucle principal
while A == False:
    # Generar números aleatorios para las variables B, D, E y F en el rango de -100 a 100
    B = random.randint(-100, 100)
    D = random.randint(-100, 100)
    E = random.randint(-100, 100)
    F = random.randint(-100, 100)
    
    # Calcular las variables G, H, I y J según las ecuaciones dadas
    G = (16 * B) - (6 * D) + (4 * E) + (F)
    H = (B) - (8 * D) + (E) + (F)
    I = (16 * B) + (2 * D) - (4 * E) + (F)
    J = (9 * B) + (8 * D) - (3 * E) + (F)
    
    # Verificar si se satisfacen las condiciones del sistema de ecuaciones
    if G == -16 and H == -64 and I == -4 and J == -64:
        A = True  # Si se satisfacen las condiciones, se establece A como True para salir del bucle
    
    # Imprimir los valores de B, D, E y F en cada iteración del bucle
    print("|B=%d\n" % (B))
    print("|D=%d\n" % (D))
    print("|E=%d\n" % (E))
    print("|F=%d\n" % (F))

# Una vez se encuentran los valores que satisfacen las condiciones, imprimir un mensaje indicando los números encontrados
print("Los Numeros son: B=%d, D=%d, E=%d, F=%d" % (B, D, E, F))
