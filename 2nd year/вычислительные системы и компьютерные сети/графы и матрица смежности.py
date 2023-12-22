N_s = input('Р’РІРµРґРёС‚Рµ С‡РёСЃР»Рѕ: ')
n = int(N_s)

matrix = [[0]*n for _ in range(n)]
array = [[x+1,x+2] for x in range(n-1)]
print(matrix)
print(array)

for i in array:
    matrix[i[0]-1][i[1]-1]=1
    matrix[i[1]-1][i[0]-1]=1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
        j=j+1
    i=i+1
    print()