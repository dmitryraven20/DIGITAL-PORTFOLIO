def get_nearest_node(weights, visited): #функция, которая возвращает минимальную непосещенную вершину
    nearest_node = '-1' #начальное значение / если вершин не осталось, то будет как индикатор их отсутствия
    weight = 99999999
    for node in weights: #пробегаемся по всем весам вершин - если вершина не была посещена и ее вес меньше чем nearest, то переопределяем ее
        if not visited[node]:
            if weight > weights[node]:
                weight = weights[node]
                nearest_node = node
    return nearest_node

def algo_Dijkstra(start, adj_matrix): 
    visited = {} #словарь посещенных вершин, по дефолту не посещенных
    for nodes in adj_matrix:
        visited[nodes] = False

    weights = {} #словарь весов для каждой вершины
    for nodes in adj_matrix:
        weights[nodes] = 99999999

    weights[start] = 0  #текущая вершина
    while start != '-1':#проходимся по всем вершинам, выбирая минимальный вес непосещенной в качестве аргумента
        for neighbour in adj_matrix[start]: #проходимся по всем соседям текущей вершины / если она не посещена, путь до нее = 0, то сравниваем текущее значение ее веса с весом пути от нашей текущей вершины и ее пути до соседа
            if not visited[neighbour] and adj_matrix[start][neighbour] != 0:
                current_road = weights[start] + adj_matrix[start][neighbour]
                if weights[neighbour] > current_road:
                    weights[neighbour] = current_road

        visited[start] = True #помечаем вершину как посещенную
        start = get_nearest_node(weights, visited) #ищем ближайшую непосещенную точку

    return weights #возвращаем массив весов от начальной вершины до всех остальных


path = ('graphic.txt') #чтение матрицы смежности из файла

start_city = input("Введите пункт А: ").strip().upper()
end_city = input("Введите пункт Б: ").strip().upper()
is_valid_input = True

with open(path, 'r') as f: #читаем заголовок с названиями пунктов (ключи в словаре)
    matrix = dict()
    head  = f.readline()[1:].split()
    
    for line in f: #записываем их в промежуточный словарь roads вес дороги и в качестве ключа используем название конечного пункта
        line = line.split()
        dest_a = line[0]
        roads = {}

        for road, dest_b in zip(line[1:], head): #помещаем словарь roads в словарь matrix с ключом пункта, откуда мы направляемся в пункты из словаря roads
            roads[dest_b] = int(road)
        matrix[dest_a] = roads

if len(start_city) != 1 or head[0] > start_city or head[-1] < start_city:
    print("Неверный ввод")
    is_valid_input = False

if len(end_city) != 1 or head[0] > end_city or head[-1] < end_city:
    print("Неверный ввод")
    is_valid_input = False

if is_valid_input:
    print("Ввод правильный, строю путь от", start_city, "до", end_city)
    mas_of_weights = algo_Dijkstra(start_city, matrix)
    print("Минмальный путь равен ", mas_of_weights[end_city])
