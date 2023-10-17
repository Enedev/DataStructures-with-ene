board = [[7,4,3],
         [8,5,2],
         [9,6,1]]

print(board)

def moveAround(matrix, row, col):

    current_value = matrix[row][col]
    print(f"Estás en la posición ({row}, {col}) y el valor es: {current_value}")

    if row == -1 and col == -1:
        return True

    directions = [(1, 0), (0, 1)]

    found_movement = False

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            next_value = matrix[new_row][new_col]

            if next_value > current_value:
                if moveAround(matrix, new_row, new_col):
                    return True
                found_movement = True

    if not found_movement:
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                if moveAround(matrix, new_row, new_col):
                    return True

    return False

moveAround(board, 0, 0)
