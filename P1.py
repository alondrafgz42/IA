
# JUEGO DEL GATO (TIC TAC TOE)

#Librerias
import random     #Genera variables aleatorias

#Funcion que imprime el tablero del juego 
def print_board(board):
    print("    A   B   C ")
    print("  +---+---+---+")
    for i in range(3):
        print(f"{i + 1} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("  +---+---+---+")


#Funcion que verifica si un jugador ha ganado el juego 
#Comprueba las combinaciones posibles de tres en línea en filas, columnas y diagonales
def check_if_won(board, symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol: #Comprueba si hay una fila con el mismo símbolo
            return True
        if board[0][i] == board[1][i] == board[2][i] == symbol: #Comprueba si hay una columna con el mismo símbolo
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol: #Comprueba si hay una diagonal con el mismo símbolo
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol: #Comprueba si hay otra diagonal con el mismo símbol
        return True
    return False

#Funcion para comprobar si hay empate
#Recorre las filas, si hay una en blanco todavia no acaba el juego
#False es que el juego no ha terminado empate, True si ha terminado empate
def check_if_tied(board):
    for row in board:
        if ' ' in row:
            return False
    return True


#Funcion principal
def main():
    #Se inicializa el tablero 
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    playing = True
    
    #Menu para seleccionar el modo de juego
    while playing:
        print_board(game_board)
        option = input("Modo de juego:\n1. Humano vs Computadora\n2. Computadora vs Computadora\n3. Salir\n")

        if option == '1': #Humano vs Computadora
            while True:
                print_board(game_board)
                move = input("Es tu turno. Escoge la fila y columna (e.j. 'A1'):") 
                #Se ingresan los datos por fila y columna
                #Convierte la letra ingresada en un índice numérico correspondiente en el tablero
                col = ord(move[0].upper()) - ord('A') 
                #Convierte el numero ingresado en un índice numérico correspondiente en el tablero
                row = int(move[1]) - 1
                
                
                #Se verifica si la casilla se encuentra vacia
                if game_board[row][col] != ' ':
                    print("Esta casilla ya está ocupada. Intenta de nuevo.")
                    continue
                
                #Simbolo x corresponde al humano
                #Se posiciona la X en el espacio especificado
                game_board[row][col] = 'X'
                
                #Se verifica si ha ganado despues del movimiento
                if check_if_won(game_board, 'X'):
                    print_board(game_board)
                    print("¡Ganaste!")
                    break
                
                #Se verifica si ha terminado el juego en empate
                if check_if_tied(game_board):
                    print_board(game_board)
                    print("¡Empate!")
                    break

                # O corresponde a la computadora
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if game_board[row][col] == ' ':
                        game_board[row][col] = 'O'
                        break
                    
                #Se verifica si ha ganado despues del movimiento
                if check_if_won(game_board, 'O'):
                    print_board(game_board)
                    print("¡Perdiste!")
                    break
                
                #Se verifica si el juego ha terminado en empate
                if check_if_tied(game_board):
                    print_board(game_board)
                    print("¡Empate!")
                    break

        elif option == '2': #Computadora vs computadora
        #Ambas computadoras colocan x y o de forma aleatoria
            while True:
                print_board(game_board)

                #X corresponde a la computadora 1 
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if game_board[row][col] == ' ':
                        game_board[row][col] = 'X'
                        break
                    
                #Se verifica si ha ganado despues del movimiento   
                if check_if_won(game_board, 'X'):
                    print_board(game_board)
                    print("¡Gano la PC 1!")
                    break
                
                #Se verifica si el juego ha terminado en empate
                if check_if_tied(game_board):
                    print_board(game_board)
                    print("¡Empate!")
                    break

                # Turno de la computadora 2
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if game_board[row][col] == ' ':
                        game_board[row][col] = 'O'
                        break
                    
                #Se verifica si ha ganado despues del movimiento 
                if check_if_won(game_board, 'O'):
                    print_board(game_board)
                    print("¡Gano la PC 2!")
                    break
                
                #Se verifica si el juego ha terminado en empate
                if check_if_tied(game_board):
                    print_board(game_board)
                    print("¡Empate!")
                    break
        
        #Salir del juego
        elif option == '3':
            break
        
        #Al terminar el juego se puede seleccionar si se desea volver a jugar
        play_again = input("¿Quieres jugar de nuevo? (S/N)").strip().upper()
        if play_again != 'S':
            playing = False
        else:
            game_board = [[' ' for _ in range(3)] for _ in range(3)]

if __name__ == "__main__":
    main()
