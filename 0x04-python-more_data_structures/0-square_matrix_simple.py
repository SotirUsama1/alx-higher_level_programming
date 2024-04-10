def square_matrix_simple(matrix=[]):
    squareM = []
    for i in matrix:
        list = []
        for j in i:
            list.append(j * j)
        squareM.append(list)
    return squareM
