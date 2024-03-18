# Declaracion de bibliotecas
from arbol import Nodo
import psutil
from timeit import default_timer

def costo_movimiento(estado_actual, estado_siguiente):
    # Calcular el costo como la diferencia entre los estados
    costo = 0
    for i in range(len(estado_actual)):
        if estado_actual[i] != estado_siguiente[i]:
            costo += 1
    return costo

def distancia(estado_actual, estado_objetivo):
    # Calcular la distancia como la suma de las diferencias absolutas entre los números
    distancia = sum(abs(a - b) for a, b in zip(estado_actual, estado_objetivo))
    return distancia

def buscar_solucion_costo_heuristica_distancia(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodoInicial.set_coste(0)  # El costo inicial es cero
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodos_frontera.sort(key=lambda x: x.get_coste() + distancia(x.get_datos(), solucion))  # Ordenar por costo + distancia
        nodo = nodos_frontera.pop(0)  # Tomar el nodo con menor costo + distancia
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            print("Costo total de la solución:", nodo.get_coste())  # Imprimir el costo total
            return nodo
        else:
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()
            costo_nodo = nodo.get_coste()
            # operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            costo_hijo = costo_movimiento(dato_nodo, hijo)
            hijo_izquierdo = Nodo(hijo)
            hijo_izquierdo.set_coste(costo_nodo + costo_hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                    and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)
            # operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            costo_hijo = costo_movimiento(dato_nodo, hijo)
            hijo_central = Nodo(hijo)
            hijo_central.set_coste(costo_nodo + costo_hijo)
            if not hijo_central.en_lista(nodos_visitados) \
                    and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)
            # operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            costo_hijo = costo_movimiento(dato_nodo, hijo)
            hijo_derecho = Nodo(hijo)
            hijo_derecho.set_coste(costo_nodo + costo_hijo)
            if not hijo_derecho.en_lista(nodos_visitados) \
                    and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)

            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

if __name__ == "__main__":
    inicio = default_timer()
    estado_inicial = [4, 3, 2, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_costo_heuristica_distancia(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)

    # Medición del tiempo de ejecución y el monitoreo del uso de memoria
    final = default_timer()
    tiempo = final - inicio
    print("\n Tiempo final:", tiempo)
    memoria = psutil.virtual_memory()
    print("\n Uso de memoria total:", memoria.total)
    print("\n Uso de memoria disponible:", memoria.available)
    print("\n Porcentaje de memoria utilizada:", memoria.percent)
    print("\n Uso de memoria en uso:", memoria.used)
    print("\n Uso de memoria libre:", memoria.free)
