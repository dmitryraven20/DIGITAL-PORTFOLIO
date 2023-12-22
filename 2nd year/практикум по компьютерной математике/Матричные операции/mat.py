def mat_null_tr(m,n):
    matr = [[0 for i in range(m)] for j in range(n)]
    return matr

def mat_null(m,n):
    matr = [[0 for j in range(n)] for i in range(m)]
    return matr

#Сложение матриц
def mat_add(M,M1):
    row_M = len(M)
    col_M = len(M[0])

    MB = mat_null(row_M,col_M)

    for i in range (row_M):
        for j in range (col_M):
            MB[i][j] = M[i][j] + M1[i][j]

    MA = MB
    return MA

#Вычитание матриц
def mat_subtr(M,M1):
    row_M = len(M)
    col_M = len(M[0])
    
    MB = mat_null(row_M,col_M)

    for i in range (row_M):
        for j in range (col_M):
            MB[i][j] = M[i][j] - M1[i][j]

    MA = MB
    return MA

#Транспонирование
def mat_transp(M):
    row_M = len(M)
    col_M = len(M[0])
    
    matr = mat_null_tr(row_M,col_M)

    for i in range (row_M):
        for j in range (col_M):
            matr[j][i] = M[i][j]
    
    M1 = matr
    return M1

#Умножение матриц
def mat_multiply(M,M1):
    row_M = len(M)
    col_M = len(M[0])

    row_M1 = len(M1)
    col_M1 = len(M1[0])

    MA = mat_null(row_M,col_M)

    if col_M <= row_M1:
        for i in range (row_M):
            for j in range (col_M):
                MA[i][j] = sum(M[i][col_M1] + M1[col_M1][j] for (col_M1) in range(row_M1))
        
        return MA
    else:
        raise ValueError

#Умножение матрицы на скаляр
def mat_scal(M,scal):
    row_M = len(M)
    col_M = len(M[0])

    matr = mat_null(row_M,col_M)

    for i in range (row_M):
        for j in range (col_M):
            matr[i][j] = M[i][j] * scal
    
    M1 = matr
    return M1

#Получение строки по индексу
def mat_str_index(M,scal):
    try:
        m = M[scal]
    except:
        raise ValueError
    return m

#Получение столбца по индексу
def mat_col_index(M,scal):
    row_M = len(M)
    col_M = len(M[0])
    
    matr = mat_null_tr(row_M,col_M)

    for i in range (row_M):
        for j in range (col_M):
            matr[j][i] = M[i][j]
    try:
        m = matr[scal]
    except:
        raise ValueError
    return m

#Перестановка строк матрицы местами
def str_swap(M,st1,st2):
    M1 = M
    M1[st1],M1[st2] = M[st2],M[st1]
    return M1

#Умножение одной строки матрицы на скаляр
def ind_str_multiply(M,st1,scal):
    row_M = len(M)
    
    M1 = M
    for j in range(row_M):
        M1[st1][j] = M[st1][j] * scal

    return M1

#Сложение строк, умноженных на число
def mat_add_num(M,st1,st2,n):
    row_M = len(M[0])

    M1 = M
    for j in range(row_M):
        M1[st2][j] = M[st2][j] + (M[st1][j] * n)

    return M1
