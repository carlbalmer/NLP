def printMatrix(matrix):
    for i in range(len(matrix)):
        print("\n", end="")
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
    print("")


def distDamLev(str1, str2):
    matrix = [[0 for i in range(len(str1) + 2)] for i in range(len(str2) + 2)]
    # initialize matrix
    for i in range(len(str1)):
        matrix[0][i + 2] = list(str1)[i]
        matrix[1][i + 2] = i + 1

    for i in range(len(str2)):
        matrix[i + 2][0] = list(str2)[i]
        matrix[i + 2][1] = i + 1

    # do the dynamic programming stuff
    for i in range(2, len(matrix)):
        for j in range(2, len(matrix[0])):
            if matrix[i][0] == matrix[0][j]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
    printMatrix(matrix)
    return matrix[len(matrix) - 1][len(matrix[0]) - 1]


print("Damerau-Levenshtein Distance =", distDamLev("Miller", "Hillier"))
