amount_island = 0
island_coords = dict()

def dfs(x, y, fill, matrix):
    global amount_island
    global island_coords
    if x >= len(matrix) or y >= len(matrix[x]):
        return

    if fill == 0 and matrix[x][y] > 0:
        amount_island += 1
        fill = matrix[x][y]

    if matrix[x][y] == fill and matrix[x][y] > 0:
        if amount_island in island_coords:
            island_coords[amount_island].append((x,y))
        else:
            island_coords[amount_island] = [(x,y)]
        matrix[x][y] *= -1
        dfs(x+1, y, fill, matrix)
        dfs(x-1, y, fill, matrix)
        dfs(x, y+1, fill, matrix)
        dfs(x, y-1, fill, matrix)

matrix = []

f = open('matrix.txt','r')
for line in f:
    line = list(map(int, line.split()))
    matrix.append(line)
f.close()
for line in matrix:
    for el in line:
        print(el, end=' ')
    print()

print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        dfs(i, j, 0, matrix)

print('Островки:')
for key in island_coords:
    min_x = min(island_coords[key], key=lambda x: x[0])[0]
    min_y = min(island_coords[key], key=lambda x: x[1])[1]
    max_x = max(island_coords[key], key=lambda x: x[0])[0]
    max_y = max(island_coords[key], key=lambda x: x[1])[1]

    for i in range(min_x, max_x+1):
        for j in range(min_y,max_y+1):
            if (i,j) in island_coords[key]:
                print(-matrix[i][j], end=' ')
            else:
                print(" ", end=' ')
        print()
    print()
print()
print("Количество островков: ",amount_island)
print("Координаты: ", island_coords)