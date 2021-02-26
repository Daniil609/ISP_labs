def bubble_max_row(matrix, row):
    """Replace m[row] row with the one of the underlying rows with the modulo greatest first element.
    :param m: matrix (list of lists)
    :param col: index of the column/row from which underlying search will be launched
    :return: None. Function changes the matrix structure.
    """
    max_element = matrix[row][row]
    max_row = row
    for i in range(row + 1, len(matrix)):
        if abs(matrix[i][row]) > abs(max_element):
            max_element = matrix[i][row]
            max_row = i
    if max_row != row:
        matrix[row], matrix[max_row] = matrix[max_row], matrix[row]

def solve_gauss(matrix):
    """Solve linear equations system with gaussian method.
    :param m: matrix (list of lists)
    :return: None
    """
    n = len(matrix)
    # forward trace
    for k in range(n - 1):
        bubble_max_row(matrix, k)
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]
            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]

    # check modified system for nonsingularity
    if is_singular(matrix):
        print('The system has infinite number of answers...')
        return

    # backward trace
    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]

    # Display results
    for i in range(len(x)):
        a = str(toFixed(x[i],4))
        print("x{} = {}".format(i+1,a))

def is_singular(matrix):
    """Check matrix for nonsingularity.
    :param m: matrix (list of lists)
    :return: True if system is nonsingular
    """
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return True
    return False

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

c = [[0.2,0,0.2,0,0],
    [0,0.2,0,0.2,0],
    [0.2,0,0.2,0,0.2],
    [0,0.2,0,0.2,0],
    [0,0,0.2,0,0.2]
    ]

d = [[2.33,0.81,0.67,0.92,-0.53],
    [-0.53,2.33,0.81,0.67,0.92],
    [0.92,-0.53,2.33,0.81,0.67],
    [0.67,0.92,-0.53,2.33,0.81],
    [0.81,0.67,0.92,-0.53,2.33]
    ]

b = [4.2,4.2,4.2,4.2,4.2]

variant = 15.0

for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j] = variant * c[i][j] + d[i][j]

for i in range(len(c)):
    for j in range(len(c[i])):
        if j == (len(c[i])-1):
            c[i].append(b[i])

for i in range(len(c)):
    for j in range(len(c[i])):
        if j == len(c[i])-2:
            print("{} X{} = {} ".format(c[i][j],j+1,c[i][j+1]),end="")
            break
        print("{} X{} * ".format(c[i][j],j+1),end="")
    print("")

solve_gauss(c)
