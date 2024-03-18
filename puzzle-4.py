# P u z z l e   L i n e a l   c o n   b ú s q u e d a   e n   p r o f u n d i d a d

#Declaracion de bibliotecas
from arbol import Nodo
import psutil
from timeit import default_timer
def buscar_solucion_DFS(estado_inicial, solucion):
    
    
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while (not solucionado) and len(nodos_frontera) != 0:        
        nodo = nodos_frontera.pop()        
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()            
            # operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                    and not hijo_izquierdo.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_izquierdo)
            # operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) \
                    and not hijo_central.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_central)
            # operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) \
                    and not hijo_derecho.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_derecho)

            
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])           



if __name__ == "__main__":
    inicio=default_timer()
    estado_inicial=[4,2,3,1]
    solucion=[1,2,3,4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    
    
    #Medición del tiempo de ejecución y el monitoreo del uso de memoria 
    final=default_timer()
    tiempo=final-inicio
    print("\n Tiempo final:",tiempo)
    memoria = psutil.virtual_memory()
    print("\n Uso de memoria total:", memoria.total)
    print("\n Uso de memoria disponible:", memoria.available)
    print("\n Porcentaje de memoria utilizada:", memoria.percent)
    print("\n Uso de memoria en uso:", memoria.used)
    print("\n Uso de memoria libre:", memoria.free)
    