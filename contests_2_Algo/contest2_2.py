def zad2_1():
    from collections import deque
    '''
    Дан невзвешенный связный граф. Вершины пронумерованы от 0. Трeбуется с помощью 
    обхода в ширину найти расстояние от одной указанной вершины до другой.
    '''
    # создаем орграф
    N, M, x, y = map(int, input().split())
    graph = {i : set() for i in range(N)}

    for i in range(M):
        V1 ,V2 = map(int, input().split())
        graph[V1].add(V2)
        graph[V2].add(V1)

    parents = [None] * N # родители пока неизвестны
    distances = [None] * N #расстояния пока неизвестны
    start_vertex = x #начальная вершина
    end_vertex = y # конечная
    distances[start_vertex] = 0 #расстояние до самой себя = 0
    queue = deque([start_vertex]) # создаем очередь

    while queue: # пока эта очередь не пустая
        current_vetrex = queue.popleft() #вызвываем из очереди вершину для  просмотра соседей
        for neighbour in graph[current_vetrex]: #просмотрим всех соседей
            if distances[neighbour] is None: #если дистанция пока неизвестна
                parents[neighbour] = current_vetrex
                distances[neighbour] = distances[current_vetrex] + 1 # дистанция от текущей вершины +1
                queue.append(neighbour)# пихаем соседа в очередь для дальнейшей обработки

    path = [end_vertex]
    parent = parents[end_vertex]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]
    print(len(path)-1)

def zad2_2():
    '''
    Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0.
    Трeбуется с помощью обхода в ширину найти расстояния от 0-й до всех остальных вершин.
    '''
    from collections import deque
    # создаем неорграф
    N, M = map(int, input().split())
    graph = {i : set() for i in range(N)}

    for i in range(M):
        V1 ,V2 = map(int, input().split())
        graph[V1].add(V2)
        graph[V2].add(V1)
    start_vertex = 0
    parents = [None] * N # родители пока неизвестны
    distances = [None] * N #расстояния пока неизвестны
    for end_vertex in graph:
        distances[start_vertex] = 0 #расстояние до самой себя = 0
        queue = deque([start_vertex]) # создаем очередь

        while queue: # пока эта очередь не пустая
            current_vetrex = queue.popleft() #вызвываем из очереди вершину для  просмотра соседей
            for neighbour in graph[current_vetrex]: #просмотрим всех соседей
                if distances[neighbour] is None: #если дистанция пока неизвестна
                    parents[neighbour] = current_vetrex
                    distances[neighbour] = distances[current_vetrex] + 1 # дистанция от текущей вершины +1
                    queue.append(neighbour)# пихаем соседа в очередь для дальнейшей обработки

        path = [end_vertex]
        parent = parents[end_vertex]
        while not parent is None:
            path.append(parent)
            parent = parents[parent]
        print(len(path)-1)

def zad2_3():
    '''
    Дано прямоугольное поле размера n строк на m столбцов. Некоторые ячейки поля
    непроходимы. Требуется найти расстояние между двумя заданными ячейками.
    '''
    from collections import deque

    N, M = map(int, input().split())
    start_vertex = input().split()
    start_vertex = start_vertex[0] +' '+ start_vertex[1]
    end_vertex = input().split()
    end_vertex = end_vertex[0] +' '+ end_vertex[1]

    field = [input() for x in range(N)]


    #составим граф
    graph = { str(i) +' '+ str(k) : set() for i in range(N) for k in range(M)}

    for vertex in graph:
        if field[int(vertex.split()[0])][int(vertex.split()[1])] == ' ': # если клетка на поле проходимая
            if int(vertex.split()[1]) + 1 < M and field[int(vertex.split()[0])][int(vertex.split()[1])+1] == ' ': # проверка границы поля справа
                graph[vertex].add( vertex.split()[0] +' '+ str(int(vertex.split()[1])+1) )
            if int(vertex.split()[0]) + 1 < N and field[int(vertex.split()[0])+1][int(vertex.split()[1])] == ' ' :  # проверка границы поля снизу
                graph[vertex].add(str(int(vertex.split()[0]) + 1) +' '+ vertex.split()[1] )
            if int(vertex.split()[1]) - 1 > -1 and field[int(vertex.split()[0])][int(vertex.split()[1])-1] == ' ': # проверка границы поля слева
                graph[vertex].add( vertex.split()[0] +' '+ str(int(vertex.split()[1])-1) )
            if int(vertex.split()[0]) - 1 > -1 and field[int(vertex.split()[0])-1][int(vertex.split()[1])] == ' ' :  # проверка границы поля сверху
                graph[vertex].add(str(int(vertex.split()[0]) - 1) +' '+ vertex.split()[1] )

    parents = {v : None for v in graph} # родители пока неизвестны
    distances = {v : None for v in graph}  # расстояния пока неизвестны
    distances[start_vertex] = 0
    queue = deque([start_vertex])  # создаем очередь


    while queue:  # пока эта очередь не пустая
        current_vetrex = queue.popleft()  # вызвываем из очереди вершину для  просмотра соседей
        for neighbour in graph[current_vetrex]:  # просмотрим всех соседей
            if distances[neighbour] is None:  # если дистанция пока неизвестна
                distances[neighbour] = distances[current_vetrex] + 1  # дистанция от текущей вершины +1
                parents[neighbour] = current_vetrex
                queue.append(neighbour)  # пихаем соседа в очередь для дальнейшей обработки
    path = [end_vertex]
    parent = parents[end_vertex]

    while not parent is None:
        path.append(parent)
        parent = parents[parent]

    if len(path)-1 > 0:
        print(len(path) -1)
    else:
        print('INF')
zad2_3()

def zad2_4():
    '''
    На шахматной доске заданы координатами 2 различных точек. В первой из них находится
    конь, во вторую точку ему надо попасть. Выведите координаты клеток, через которые
    надо прочти коню, чтобы попасть во вторую точку. Путь должен быть кратчайшим, среди
    имеющихся.
    '''
    from collections import deque
    liters = 'abcdefgh'
    numbers = '12345678'
    graph = {x + y : set() for x in liters for y in numbers}

    start_vertex = input()
    end_vertex = input()
    def add_edge(v1,v2):
        graph[v1].add(v2)
        graph[v2].add(v1)

    for i in range(len(liters)):
        for j in range(len(numbers)):
            v1 = liters[i] + numbers[j]
            for mod_i, mod_j in (i+2,j+1),(i-2,j+1),(i+1,j+2),(i-1,j+2):
                if 0 <= mod_i < len(liters) and 0 <= mod_j < len(numbers):
                    v2 = liters[mod_i] + numbers[mod_j]
                    add_edge(v1,v2)

    parents = {v : None for v in graph} # родители пока неизвестны
    distances = {v : None for v in graph}  # расстояния пока неизвестны
    distances[start_vertex] = 0
    queue = deque([start_vertex])  # создаем очередь


    while queue:  # пока эта очередь не пустая
        current_vetrex = queue.popleft()  # вызвываем из очереди вершину для  просмотра соседей
        for neighbour in graph[current_vetrex]:  # просмотрим всех соседей
            if distances[neighbour] is None:  # если дистанция пока неизвестна
                distances[neighbour] = distances[current_vetrex] + 1  # дистанция от текущей вершины +1
                parents[neighbour] = current_vetrex
                queue.append(neighbour)  # пихаем соседа в очередь для дальнейшей обработки
    path = [end_vertex]
    parent = parents[end_vertex]

    while not parent is None:
        path.append(parent)
        parent = parents[parent]
    for x in path[::-1]:
        print(x)


def zad2_5():
    '''
    Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0.
    Трeбуется с помощью обхода в ширину построить остовное дерево.
    '''
    from collections import deque
    n,m = map(int,input().split())
    graph = {}

    # сформируем список смежностей именно -  НЕОРИЕНТИРОВАННОГО ГРАФА

    for x in range(m):
        a, b = [int(y) for y in input().split()]
        for v, u in (a, b), (b, a):
            if v not in graph:
                graph[v] = {u}
            else:
                graph[v].add(u)
    start_vertex = 0
    parents = [None] * n # родители пока неизвестны
    distances = [None] * n #расстояния пока неизвестны
    for end_vertex in graph:
        distances[start_vertex] = 0 #расстояние до самой себя = 0
        queue = deque([start_vertex]) # создаем очередь

        while queue: # пока эта очередь не пустая
            current_vetrex = queue.popleft() #вызвываем из очереди вершину для  просмотра соседей
            for neighbour in graph[current_vetrex]: #просмотрим всех соседей
                if distances[neighbour] is None: #если дистанция пока неизвестна
                    parents[neighbour] = current_vetrex
                    distances[neighbour] = distances[current_vetrex] + 1 # дистанция от текущей вершины +1
                    queue.append(neighbour)# пихаем соседа в очередь для дальнейшей обработки

    for i in range (n): #пройдём по вершинам
        if parents[i] is not None: # из списка предков индекс и будет потомком
            print(parents[i],i) # таким образом мы построим остовное древо избегая циклов

def zad2_6():
    from collections import deque
    n, m = map(int, input().split())
    field = [input().split() for x in range(n)]
    graph = {str(i) +'.'+ str(k): set() for i in range(n) for k in range(m)}
    for vertex in graph:
        if int(vertex.split('.')[1]) + 1 < m :  # проверка границы поля справа
            graph[vertex].add(vertex.split('.')[0] +'.'+ str(int(vertex.split('.')[1]) + 1))
        if int(vertex.split('.')[0]) + 1 < n :  # проверка границы поля снизу
            graph[vertex].add(str(int(vertex.split('.')[0]) + 1) +'.'+ vertex.split('.')[1])
        if int(vertex.split('.')[1]) - 1 > -1 :  # проверка границы поля слева
            graph[vertex].add(vertex.split('.')[0] +'.'+ str(int(vertex.split('.')[1]) - 1))
        if int(vertex.split('.')[0]) - 1 > -1 :  # проверка границы поля сверху
            graph[vertex].add(str(int(vertex.split('.')[0]) - 1) +'.'+ vertex.split('.')[1])



    total_table = [[0 for i in range(m)] for j in range(n)]
    parentss = {v: None for v in graph}  # родители пока неизвестны
    distancess = parentss.copy()# расстояния пока неизвестны
    for i in range(n):
        for j in range(m):
            if field[i][j] == '1':
                total_table[i][j] = 0
                continue
            start_vertex = str(i) +'.'+ str(j) # для перестройки таблицы нужно просмотреть каждую вершину
            parents = parentss.copy() # родители пока неизвестны
            distances = distancess.copy()  # расстояния пока неизвестны
            distances[start_vertex] = 0
            queue = deque([start_vertex])  # создаем очередь

            while queue:  # пока эта очередь не пустая
                current_vetrex = queue.popleft()  # вызвываем из очереди вершину для  просмотра соседей
                for neighbour in graph[current_vetrex]:  # просмотрим всех соседей
                    if field[int(neighbour.split('.')[0])][int(neighbour.split('.')[1])] == '1':  # сосед близжайшая 1
                        queue = False
                        end_vertex = neighbour
                        break
                    if distances[neighbour] is None:  # если дистанция пока неизвестна
                        distances[neighbour] = distances[current_vetrex] + 1  # дистанция от текущей вершины +1
                        parents[neighbour] = current_vetrex
                        queue.append(neighbour)  # пихаем соседа в очередь для дальнейшей обработки


            #считаем по формуле расстрояние |x1-x2|+|y1-y2|
            total_table[i][j] = abs(i - int(end_vertex.split('.')[0])) + abs(j - int(end_vertex.split('.')[1]))

    for line in total_table:
        for liter in line:
            print(liter, end = ' ')
        print()



def zad2_7():
    '''
    Витя хочет придумать новую игру с числами. В этой игре от игроков
    требуется преобразовывать четырехзначные числа не содержащие нулей
    при помощи следующего разрешенного набора действий:

    Можно увеличить первую цифру числа на 1, если она не равна 9.
    Можно уменьшить последнюю цифру на 1, если она не равна 1.
    Можно циклически сдвинуть все цифры на одну вправо.
    Можно циклически сдвинуть все цифры на одну влево.
    Например, применяя эти правила к числу 1234 можно получить числа 2234, 1233, 4123 и
    2341 соответственно. Точные правила игры Витя пока не придумал, но пока его
    интересует вопрос, как получить из одного числа другое за минимальное количество операций.
    '''
    from collections import deque

    start_vertex = input()
    end_vertex = input()
    graph = {}
    def add_edge(graph,vertex):
        pass


    while end_vertex not in graph:
        graph[start_vertex].add
    while queue: # пока эта очередь не пустая
        current_vetrex = queue.popleft() #вызвываем из очереди вершину для  просмотра соседей
        for neighbour in graph[current_vetrex]: #просмотрим всех соседей
            if distances[neighbour] is None: #если дистанция пока неизвестна
                parents[neighbour] = current_vetrex
                distances[neighbour] = distances[current_vetrex] + 1 # дистанция от текущей вершины +1
                queue.append(neighbour)# пихаем соседа в очередь для дальнейшей обработки

    path = [end_vertex]
    parent = parents[end_vertex]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]


