import random

class Node:
    def __init__(self):
        self.is_empty = True  # Indica si la celda está vacía
        self.has_wall = False  # Indica si la celda tiene una pared
        self.player = None     # Jugador en la celda (None si está vacía)
        self.next = None       # Enlace al nodo siguiente

class LinkedListMatrix:
    def __init__(self, N):
        self.N = N
        self.matrix = [[Node() for _ in range(N)] for _ in range(N)]
        self.initialize_links()

    def initialize_links(self):
        for row in range(self.N):
            for col in range(self.N):
                # Establecer enlaces horizontales
                if col < self.N - 1:
                    self.matrix[row][col].next = self.matrix[row][col + 1]

                # Establecer enlaces verticales
                if row < self.N - 1:
                    self.matrix[row][col].next_vertical = self.matrix[row + 1][col]

    def initialize_players(self):
        # Inicializar el jugador X en la fila 0
        x_row = 0
        x_col = random.randint(0, self.N - 1)  # Columna aleatoria
        self.matrix[x_row][x_col].is_empty = False
        self.matrix[x_row][x_col].player = 'X'

        # Inicializar el jugador Y en la última fila (fila N-1)
        y_row = self.N - 1
        y_col = random.randint(0, self.N - 1)  # Columna aleatoria
        self.matrix[y_row][y_col].is_empty = False
        self.matrix[y_row][y_col].player = 'Y'

    def print_board(self):
        for row in self.matrix:
            row_str = ""
            for cell in row:
                if cell.is_empty:
                    if cell.has_wall:
                        row_str += "# "  # Casilla eliminada
                    else:
                        row_str += "- "  # Celda vacía
                else:
                    row_str += cell.player + " "  # Jugador en la celda
            print(row_str)

    def has_won(self, player):
        # Verificar si el jugador ha ganado
        if player == 'X':
            for col in range(self.N):
                if not self.matrix[self.N - 1][col].is_empty and self.matrix[self.N - 1][col].player == 'X':
                    return True  # El jugador X llegó a la fila n-1
        elif player == 'Y':
            for col in range(self.N):
                if not self.matrix[0][col].is_empty and self.matrix[0][col].player == 'Y':
                    return True  # El jugador Y llegó a la fila 0
        return False

    def move_player(self, player, direction):
        # Obtener la posición actual del jugador
        current_row, current_col = self.find_player_position(player)

        # Definir los posibles movimientos
        possible_moves = {
            'left': (0, -1),
            'right': (0, 1),
            'up': (-1, 0),
            'down': (1, 0)
        }

        # Verificar si el movimiento es válido y aplicarlo
        if direction in possible_moves:
            new_row = current_row + possible_moves[direction][0]
            new_col = current_col + possible_moves[direction][1]

            # Verificar si la nueva posición es válida y no está ocupada
            if self.is_valid_position(new_row, new_col) and not self.matrix[new_row][new_col].has_wall:
                # Realizar el movimiento y desenlazar el nodo
                self.matrix[current_row][current_col].is_empty = True
                self.matrix[current_row][current_col].player = None
                self.matrix[new_row][new_col].is_empty = False
                self.matrix[new_row][new_col].player = player
                return True

        return False

    def remove_cell(self, row, col, player):
        # Verificar si la casilla a eliminar no tiene una pared y no está ocupada por un jugador
        if not self.matrix[row][col].has_wall and self.matrix[row][col].is_empty:
            # Temporalmente, marca la casilla como eliminada para verificar el acceso
            self.matrix[row][col].has_wall = True

            # Verificar si el jugador puede llegar a su fila de victoria
            can_reach_victory = self.can_reach_victory(player)

            # Restaurar la casilla
            self.matrix[row][col].has_wall = False

            if not can_reach_victory:
                return False

            # Eliminar la casilla (desenlazar el nodo)
            self.matrix[row][col].has_wall = True
            self.matrix[row][col].is_empty = True
            self.matrix[row][col].player = None
            return True

        return False

    def can_reach_victory(self, player):
        def dfs(row, col):
            # Marcamos la casilla actual como visitada
            visited[row][col] = True

            # Si el jugador alcanza su fila de victoria, retornamos True
            if (player == 'X' and row == self.N - 1) or (player == 'Y' and row == 0):
                return True

            # Direcciones posibles para moverse
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Verificamos si la nueva posición es válida y si la casilla no está bloqueada y no ha sido visitada
                if (0 <= new_row < self.N and 0 <= new_col < self.N
                        and not visited[new_row][new_col]
                        and not self.matrix[new_row][new_col].has_wall):
                    if dfs(new_row, new_col):
                        return True

            return False

        # Inicializamos una matriz para marcar las casillas visitadas
        visited = [[False for _ in range(self.N)] for _ in range(self.N)]

        # Encontramos la posición inicial del jugador
        start_row, start_col = self.find_player_position(player)

        return dfs(start_row, start_col)

    def is_valid_position(self, row, col):
        return 0 <= row < self.N and 0 <= col < self.N

    def find_player_position(self, player):
        for row in range(self.N):
            for col in range(self.N):
                if not self.matrix[row][col].is_empty and self.matrix[row][col].player == player:
                    return row, col

# Crear un tablero de 5x5
board = LinkedListMatrix(5)

# Inicializar jugadores en posiciones aleatorias
board.initialize_players()

while True:
   # Turno del jugador X
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

    # Turno del jugador Y
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

