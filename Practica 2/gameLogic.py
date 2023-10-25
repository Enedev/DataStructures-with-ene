from linkedList import LinkedListMatrix

def play_game():
    # Crear un tablero de 5x5
    board = LinkedListMatrix(5)

    # Inicializar jugadores en posiciones aleatorias
    board.initialize_players()

    while True:
        player = 'X'
        board.print_board()
        action = input("Jugador X, ¿qué acción deseas realizar? (m para mover, e para eliminar): ")

        if action == 'm':
            while not board.move_player(player, input("Dirección de movimiento (left, right, up, down): ")):
                print("Movimiento inválido o la casilla está eliminada. Repite tu turno.")
            if board.has_won(player):
                board.print_board()
                print("¡El jugador X ha ganado!")
                break
        elif action == 'e':
            while not board.remove_cell(int(input("Fila de la casilla a eliminar: ")), int(input("Columna de la casilla a eliminar: ")), player):
                print("La casilla seleccionada no puede ser eliminada. Repite tu turno.")
            if board.has_won(player):
                board.print_board()
                print("¡El jugador X ha ganado!")
                break

        player = 'Y'
        board.print_board()
        action = input("Jugador Y, ¿qué acción deseas realizar? (m para mover, e para eliminar): ")

        if action == 'm':
            while not board.move_player(player, input("Dirección de movimiento (left, right, up, down): ")):
                print("Movimiento inválido o la casilla está eliminada. Repite tu turno.")
            if board.has_won(player):
                board.print_board()
                print("¡El jugador Y ha ganado!")
                break
        elif action == 'e':
            while not board.remove_cell(int(input("Fila de la casilla a eliminar: ")), int(input("Columna de la casilla a eliminar: ")), player):
                print("La casilla seleccionada no puede ser eliminada. Repite tu turno.")
            if board.has_won(player):
                board.print_board()
                print("¡El jugador Y ha ganado!")
                break

if __name__ == "__main__":
    play_game()
