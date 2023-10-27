import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.up = None
        self.down = None
        self.is_removed = False 

    def remove(self):
        # Desenlazar el nodo
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        if self.up:
            self.up.down = self.down
        if self.down:
            self.down.up = self.upe


class MatrixLinkedList:
    def __init__(self, n):
        self.n = n
        self.head = self.build_matrix(n)

    def build_matrix(self, n):
        head = Node(None)
        current_row = head

        for i in range(n):
            current_col = current_row
            for j in range(n):
                new_node = Node(None)
                new_node.prev = current_col
                current_col.next = new_node
                current_col = new_node

            if i < n - 1:
                next_row = Node(None)
                current_row.down = next_row
                next_row.up = current_row
                current_row = next_row

        return head

    def get_node(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.n:
            current = self.head

            for _ in range(row):
                current = current.down

            for _ in range(col):
                current = current.next

            return current

    def __getitem__(self, index):
        row, col = index
        node = self.get_node(row, col)
        if node:
            return node.value
        else:
            raise IndexError("Índices fuera de rango")

    def set_value(self, row, col, value):
        node = self.get_node(row, col)
        if node:
            node.value = value

    def initialize_players(self):
        # Inicializar el jugador X en la fila 0
        x_row = 0
        x_col = random.randint(0, self.n - 1)  # Columna aleatoria
        self.set_value(x_row, x_col, 'X')

        # Inicializar el jugador Y en la última fila (fila n-1)
        y_row = self.n - 1
        y_col = random.randint(0, self.n - 1)  # Columna aleatoria
        self.set_value(y_row, y_col, 'Y')


    def print_matrix(self):
        for row in range(self.n):
            current = self.get_node(row, 0)
            row_str = ""
            
            for _ in range(self.n):
                if current.value is None:
                    if current.is_removed:
                        row_str += "#"
                    else:
                        row_str += "□"
                else:
                    row_str += str(current.value)
                current = current.next

            print(row_str)

    
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
            move_row, move_col = possible_moves[direction]
            new_row = current_row + move_row
            new_col = current_col + move_col

            if self.is_valid_position(new_row, new_col):
                current_node = self.get_node(current_row, current_col)
                new_node = self.get_node(new_row, new_col)

                if not new_node.is_removed and not new_node.value:  # Verificar si el nodo no está eliminado
                    current_node.value = None  # Desenlazar el nodo actual
                    new_node.value = player  # Enlazar el nodo nuevo con el jugador
                    return True

        return False


    def remove_cell(self, row, col, player):
        # Obtener el nodo en la posición a eliminar
        node_to_remove = self.get_node(row, col)

        if node_to_remove:
            # Verificar si el nodo no tiene una pared y no está ocupado por un jugador
            if not node_to_remove.is_removed and not node_to_remove.value:
                # Simulamos la eliminación para verificar si aún es posible ganar
                node_to_remove.is_removed = True
                can_reach_victory = self.can_reach_victory(player)
                node_to_remove.is_removed = False  # Restauramos el estado del nodo

                if can_reach_victory:
                    node_to_remove.is_removed = True  # Eliminar la referencia del nodo
                    return True

        return False

    
    def has_won(self, player):
        # Verificar si el jugador ha ganado
        if player == 'X':
            for col in range(self.n):
                node = self.get_node(self.n - 1, col)
                if node and node.value == 'X':
                    return True  # El jugador X llegó a la fila n-1
        elif player == 'Y':
            for col in range(self.n):
                node = self.get_node(0, col)
                if node and node.value == 'Y':
                    return True  # El jugador Y llegó a la fila 0
        return False
    
    def find_player_position(self, player):
        for row in range(self.n):
            for col in range(self.n):
                node = self.get_node(row, col)
                if node and not node.value is None and node.value == player:
                    return row, col
        return None
    
    def is_valid_position(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n
    
    def get_node_position(self, node):
        current = self.head
        row, col = 0, 0

        while current:
            if current == node:
                return row, col

            col += 1
            current = current.next

            if col == self.n:
                col = 0
                row += 1
                current = current.down

        return -1, -1  # Si el nodo no se encuentra en la matriz


    def can_reach_victory(self, player):
        def dfs(row, col):
            visited[row][col] = True

            if (player == 'X' and row == self.n - 1) or (player == 'Y' and row == 0):
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < self.n and 0 <= new_col < self.n
                        and not visited[new_row][new_col]
                        and not self.get_node(new_row, new_col).is_removed
                        and not self.get_node(new_row, new_col).value):
                    if dfs(new_row, new_col):
                        return True

            return False

        visited = [[False for _ in range(self.n)] for _ in range(self.n)]
        start_row, start_col = self.find_player_position(player)

        return dfs(start_row, start_col)
    
def play_game():
    n = 5  # Tamaño del tablero
    board = MatrixLinkedList(n)  # Crear un tablero de 5x5

    # Inicializar jugadores en posiciones aleatorias
    board.initialize_players()

    while True:
        player = 'X'
        board.print_matrix()
        action = input(f"Jugador {player}, ¿qué acción deseas realizar? (m para mover, e para eliminar): ")

        if action == 'm':
            while True:
                direction = input("Dirección de movimiento (left, right, up, down): ")
                if direction in ['left', 'right', 'up', 'down']:
                    break
                else:
                    print("Dirección no válida. Intenta de nuevo.")

            if not board.move_player(player, direction):
                print("Movimiento inválido o la casilla está eliminada. Repite tu turno.")
                continue

            if board.has_won(player):
                board.print_matrix()
                print(f"¡El jugador {player} ha ganado!")
                break
        elif action == 'e':
            while True:
                row = int(input("Fila de la casilla a eliminar: "))
                col = int(input("Columna de la casilla a eliminar: "))
                if 0 <= row < n and 0 <= col < n:
                    break
                else:
                    print("Casilla seleccionada fuera de rango. Intenta de nuevo.")

            if not board.remove_cell(row, col, player):
                print("La casilla seleccionada no puede ser eliminada. Repite tu turno.")
                continue

        player = 'Y'
        board.print_matrix()
        action = input(f"Jugador {player}, ¿qué acción deseas realizar? (m para mover, e para eliminar): ")

        if action == 'm':
            while True:
                direction = input("Dirección de movimiento (left, right, up, down): ")
                if direction in ['left', 'right', 'up', 'down']:
                    break
                else:
                    print("Dirección no válida. Intenta de nuevo.")

            if not board.move_player(player, direction):
                print("Movimiento inválido o la casilla está eliminada. Repite tu turno.")
                continue

            if board.has_won(player):
                board.print_matrix()
                print(f"¡El jugador {player} ha ganado!")
                break
        elif action == 'e':
            while True:
                row = int(input("Fila de la casilla a eliminar: "))
                col = int(input("Columna de la casilla a eliminar: "))
                if 0 <= row < n and 0 <= col < n:
                    break
                else:
                    print("Casilla seleccionada fuera de rango. Intenta de nuevo.")

            if not board.remove_cell(row, col, player):
                print("La casilla seleccionada no puede ser eliminada. Repite tu turno.")

if __name__ == "__main__":
    play_game()
