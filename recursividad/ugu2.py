def move_to_target(matrix, row, col):
   
    current_value = matrix[row][col]
    print(f"Estás en la posición ({row}, {col}) y el valor es: {current_value}")

    if row == -1 and col == -1:
        return True

    if row + 1 < 3:
        value_down = matrix[row + 1][col]
    else:
        value_down = float('-inf')

    if col + 1 < 3:
        value_right = matrix[row][col + 1]
    else:
        value_right = float('-inf')
    

    if value_down > current_value and value_down >= value_right:
        return move_to_target(matrix, row + 1, col)
    elif value_right > current_value and value_right > value_down:
        return move_to_target(matrix, row, col + 1)
    else:
        if row == 2 and col == 2:
            return True
        else:
            if row + 1 >= 2:
                return move_to_target(matrix, row, col + 1)

            elif col + 1 >= 2:
                return move_to_target(matrix, row+1, col)

matrix_3x3 = [[7,4,3],
         [8,5,2],
         [9,6,1]]

move_to_target(matrix_3x3, 0, 0)
