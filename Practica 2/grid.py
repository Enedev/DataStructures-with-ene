import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value) + " "
            current = current.next
        return result

class Grid:
    def __init__(self, rows, columns, fill_value=None):
        self.rows = rows
        self.columns = columns
        self.data = [[LinkedList() for _ in range(columns)] for _ in range(rows)]
        for row in range(rows):
            for col in range(columns):
                self.data[row][col].append(fill_value)

    def get_height(self):
        return self.rows

    def get_width(self):
        return self.columns

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                cell_data = self.data[row][col]
                if cell_data is None or cell_data.__str__() == "":
                    result += "# "  # Representa las casillas eliminadas con un "#" en lugar de None
                else:
                    result += cell_data.__str__() + " "
            result += "\n"
        return result

def move_player(grid, player, direction, visited_cells, opponent_visited_cells):
    current_row, current_col = player["position"]
    new_row, new_col = current_row, current_col

    if direction == "up":
        new_row -= 1
    elif direction == "down":
        new_row += 1
    elif direction == "left":
        new_col -= 1
    elif direction == "right":
        new_col += 1

    if (
        0 <= new_row < grid.get_height()
        and 0 <= new_col < grid.get_width()
        and (new_row, new_col) not in visited_cells
        and (new_row, new_col) not in opponent_visited_cells
    ):
        grid[current_row][current_col].head = None  # Limpia la celda actual
        player["position"] = (new_row, new_col)
        grid[new_row][new_col] = LinkedList()  # Crea una nueva lista en la celda
        grid[new_row][new_col].append(player["symbol"])  # Agrega el símbolo del jugador
        visited_cells.add((new_row, new_col))
        return True
    else:
        print("¡No puedes pasar por esta casilla o ya la has visitado! Elige otro movimiento.")
        return False

def find_paths(grid, player, visited_cells, target_row):
    current_row, current_col = player["position"]

    if current_row == target_row:
        return [[]]

    directions = ["up", "down", "left", "right"]
    paths = []

    for direction in directions:
        new_row, new_col = current_row, current_col

        if direction == "up":
            new_row -= 1
        elif direction == "down":
            new_row += 1
        elif direction == "left":
            new_col -= 1
        elif direction == "right":
            new_col += 1

        if (0 <= new_row < grid.get_height() and 0 <= new_col < grid.get_width()
            and grid[new_row][new_col].__str__() != "#" and (new_row, new_col) not in visited_cells):
            visited_cells.add((new_row, new_col))
            player["position"] = (new_row, new_col)
            sub_paths = find_paths(grid, player, visited_cells, target_row)
            for sub_path in sub_paths:
                paths.append([(new_row, new_col)] + sub_path)
            visited_cells.remove((new_row, new_col))
            player["position"] = (current_row, current_col)

    return paths

def can_move(matrix, player, direction, visited_cells, opponent_visited_cells):
    current_row, current_col = player["position"]
    new_row, new_col = current_row, current_col

    if direction == "up":
        new_row -= 1
    elif direction == "down":
        new_row += 1
    elif direction == "left":
        new_col -= 1
    elif direction == "right":
        new_col += 1

    # Realiza una copia de las casillas visitadas para no modificar las originales
    temp_visited_cells = visited_cells.copy()
    temp_opponent_visited_cells = opponent_visited_cells.copy()

    if (
        0 <= new_row < matrix.get_height()
        and 0 <= new_col < matrix.get_width()
        and (new_row, new_col) not in temp_visited_cells
        and (new_row, new_col) not in temp_opponent_visited_cells
    ):
        temp_visited_cells.remove(player["position"])  # Quita la posición actual de las casillas visitadas
        temp_visited_cells.add((new_row, new_col))  # Agrega la nueva posición a las casillas visitadas

        # Verifica si bloquea una ruta de victoria
        if not find_paths(matrix, player, temp_visited_cells, player["position"][0]):
            return False

    return True

def check_win(player, target_row):
    return player["position"][0] == target_row

# ... (código anterior)
def print_board(matrix):
    print(matrix)

def main():
    matrix = Grid(5, 5)

    initial_col_x = random.randint(0, 4)
    initial_col_y = random.randint(0, 4)
    matrix[0][initial_col_x] = LinkedList()
    matrix[matrix.get_height() - 1][initial_col_y] = LinkedList()
    matrix[0][initial_col_x].append('X')
    matrix[matrix.get_height() - 1][initial_col_y].append('Y')

    player_x = {"symbol": "X", "position": (0, initial_col_x)}
    player_y = {"symbol": "Y", "position": (matrix.get_height() - 1, initial_col_y)}

    visited_cells_x = {(0, initial_col_x)}
    visited_cells_y = {(matrix.get_height() - 1, initial_col_y)}
    print_board(matrix)
    # Listas para almacenar rutas de victoria
    paths_x = []
    paths_y = []

    while True:
        paths_x = find_paths(matrix, player_x, visited_cells_x, matrix.get_height() - 1)     

        valid_move_x = False
        while not valid_move_x:
            move = input("Turno de Jugador X (selecciona una dirección - up/down/left/right): ")
            if move in ["up", "down", "left", "right"] and can_move(matrix, player_x, move, visited_cells_x, visited_cells_y):
                valid_move_x = move_player(matrix, player_x, move, visited_cells_x, visited_cells_y)
                paths_x = find_paths(matrix, player_x, visited_cells_x, matrix.get_height() - 1)  # Actualiza rutas
                if valid_move_x:
                    print_board(matrix) # Imprime el tablero después del movimiento

        if check_win(player_x, matrix.get_height() - 1):
            print("¡Jugador X ha ganado!")
            break

        paths_y = find_paths(matrix, player_y, visited_cells_y, 0)

        valid_move_y = False
        while not valid_move_y:
            move = input("Turno de Jugador Y (selecciona una dirección - up/down/left/right): ")
            if move in ["up", "down", "left", "right"] and can_move(matrix, player_y, move, visited_cells_y, visited_cells_x):
                valid_move_y = move_player(matrix, player_y, move, visited_cells_y, visited_cells_x)
                paths_y = find_paths(matrix, player_y, visited_cells_y, 0)  # Actualiza rutas
                if valid_move_y:
                    print_board(matrix)  # Imprime el tablero después del movimiento

        if check_win(player_y, 0):
            print("¡Jugador Y ha ganado!")
            break

        if not paths_x or not paths_y:
            print("¡Empate! Uno de los jugadores no tiene rutas de victoria disponibles.")
            break

if __name__ == "__main__":
    main()