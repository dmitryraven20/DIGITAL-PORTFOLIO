landscape = [int(x) for x in (2,4,1,1,4,7,3,5)]
levels = len(landscape)
flood = 0

print('У острова такой ландшафт: ', landscape)

left = [0]*levels #размер самого большого столбца слева
right = [0]*levels #размер самого большого столбца справа

left[0] = landscape[0] #заполнение массива
for i in range(1,levels):
    left[i] = max(left[i-1],landscape[i])
    right[levels-1] = landscape[levels-1]
for i in range(levels-2,-1,-1):
    right[i] = max(right[i+1], landscape[i])

for i in range(0, levels):
    flood += min(left[i],right[i]) - landscape[i]

print('Заполненность водой: ', flood)