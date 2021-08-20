def zad1_1():
    '''
    На вход программы поступает число n ( 1 <= n <= 100) – количество вершин в графе, а затем
    n строк по n чисел, каждое из которых равно 0 или 1, – его матрица смежности.
    '''
    cnt=0
    N=int(input())
    G=[input().split() for y in range(N)]
    for i in range(N):
        for j in range(i,N):
            if int(G[i][j]):
                cnt+=1
    print(cnt)
    
def zad1_2():
    '''
    На вход программы поступает число n ( 1 <= n <= 100) – размер матрицы, а затем n строк по n
    чисел, каждое из которых равно 0 или 1, – сама матрица.
    '''
    flag = False
    N=int(input())
    G=[input().split() for y in range(N)]
    for i in range(N):
        for j in range(N):
            if G[i][j] != G[j][i]:
                flag = True
                break
            elif i == j and G[i][j] =='1':
                flag = True
                break
        if flag:
            print('NO')
            break
    else:
         print('YES')
         
def zad1_3():
    '''
    В Банановой республике очень много холмов, соединенных мостами. На химическом заводе
    произошла авария, в результате чего испарилось экспериментальное удобрение "зован". На
    следующий день выпал цветной дождь, причем он прошел только над холмами. В некоторых
    местах падали красные капли, в некоторых – синие, а в остальных – зеленые, в результате чего
    холмы стали соответствующего цвета. Президенту Банановой республики это понравилось, но
    ему захотелось покрасить мосты между вершинами холмов так, чтобы мосты были покрашены
    в цвет холмов, которые они соединяют. К сожалению, если холмы разного цвета, то покрасить
    мост таким образом не удастся. Посчитайте количество таких "плохих" мостов.
    '''
    N = int(input())
    G = [input().split() for y in range(N)]
    input()
    colors = input().split()
    cnt=0
    for i in range(N):
        for j in range(N):
            if int(G[i][j]) and colors[i] != colors[j]:
                cnt+=1
    print(cnt//2)
    
def zad1_4():
    '''
    Ориентированный граф называется полуполным, если между любой парой его различных вершин
    есть хотя бы одно ребро. Для заданного списком ребер графа проверьте, является ли он полуполным.
    '''
    N,M = [int (x) for x in input().split()]
    G = []
    for x in range(M):
        a,b = [int (y) for y in input().split()]
        if {a,b} not in G:
            G.append({a,b})
    for i in range(N):
        cnt=0
        for item in G:
            if i in item:
                cnt += 1
        if cnt < N-1:
            print('NO')
            break
    else:
        print('YES')

def zad1_5():
    '''
    Дан ориентированный граф. Вершины пронумерованы от 0.
    Трeбуется с помощью обхода в глубину проверить является ли граф ацикличным.
    '''
   
    N,M = [int (x) for x in input().split()]
    
    visited = set()
    G = {}
   
    
    
    #сформируем список смежностей именно -  ОРИЕНТИРОВАННОГО ГРАФА
   
    flag= False
    
    for x in range(M):
        a,b = [int (y) for y in input().split()]
        if a not in G:
            G[a]={b}
        else:
            G[a].add(b)
    
    l=[]
    #G = {0: {8, 10, 7}, 7: {10, 2, 4}, 10: {9, 2}, 4: {8, 11}, 3: {4, 5}, 11: {0}, 6: {8, 1, 11, 5}, 8: {11}, 9: {8, 2}}
    #N=12
    
    for i in range(N):
        if i not in G:
            G[i]=set()
            visited.add(i)
        
    G_colors = {x : 0 for x in G}
    
    #print(G_colors)
    
    flag=False
    def dfs(start,G, visited,l):
        
        #СДЕЛАТЬ RETURN ФУНКЦИИ и функцию впихнуть в условие. ложь выкинет из цикла нахой мб?
        if start in G:

            c = 0
            visited.add(start) #добавляем в посещенную вершину
            G_colors[start] = 1
            l.append(start) #запоминаем вложение
            for neighbour in G[start]:  #для всех соседей 
                if neighbour not in visited:#которые не посещены 
                    c = dfs(neighbour, G, visited,l) # выход 3 результата: 
                    #1 - просмотрели всех соседей
                    #2 - соседей у вершины нету
                    #3 - цикл найден
                    if c==3:
                        return 3
               
                elif neighbour in visited and G_colors[neighbour] == 1:
                    
                    return 3
                  

            l.pop()
            G_colors[start] = 2
            return 1
        else:
            l.pop()
            G_colors[start] =2
            return 2
            
    
    for vertex in G:
        if vertex not in visited:
            c=dfs(vertex,G,visited,l)
            if c==3:
                flag = True
                break


    if flag:           
        for x in l:
            print(x, end=' ')
    else:
        print('YES')
  
def zad1_6():
    '''
    Дан ориентированный граф. Вершины пронумерованы от 0. Требуется с помощью топологической
    сортировки линейно упорядочить вершины графа в список так, чтобы для любого ребра графа из
    вершины A в вершину B, вершина A была левее чем B в списке.
    '''
   
    N,M = [int (x) for x in input().split()]
    
    visited = set()
    G = {}
   
    
    
    #сформируем список смежностей именно -  ОРИЕНТИРОВАННОГО ГРАФА
   
    flag= False
    
    for x in range(M):
        a,b = [int (y) for y in input().split()]
        if a not in G:
            G[a]={b}
        else:
            G[a].add(b)
    
    l=[]
    #G = {0: {8, 10, 7}, 7: {10, 2, 4}, 10: {9, 2}, 4: {8, 11}, 3: {4, 5}, 11: {0}, 6: {8, 1, 11, 5}, 8: {11}, 9: {8, 2}}
    #N=12
    
    for i in range(N):
        if i not in G:
            G[i]=set()
    
        
    G_colors = {x : 0 for x in G}
    
    #print(G_colors)
    
    flag=False
    def dfs(start,G, visited,l):
        
        #СДЕЛАТЬ RETURN ФУНКЦИИ и функцию впихнуть в условие. ложь выкинет из цикла нахой мб?
        if start in G:

            c = 0
            visited.add(start) #добавляем в посещенную вершину
            G_colors[start] = 1
             
            for neighbour in G[start]:  #для всех соседей 
                if neighbour not in visited:#которые не посещены 
                    c = dfs(neighbour, G, visited,l) # выход 3 результата: 
                    #1 - просмотрели всех соседей
                    #2 - соседей у вершины нету
                    #3 - цикл найден
                    if c==3:
                        return 3
                elif neighbour in visited and G_colors[neighbour] == 1:
                    
                    return 3
            l.append(start)

            
            G_colors[start] = 2
            return 1
        else:
          
            G_colors[start] =2
            return 2
            
    
    for vertex in G:
        if vertex not in visited:
            c=dfs(vertex,G,visited,l)
            if c==3:
                flag = True
                break
    if not flag:           
        for i in range(N):
            if i not in G:
                print(x, end=' ')
    else:
        print('NO')
def zad1_7():
    '''
    Во время контрольной работы профессор заметил, что некоторые студенты
    обмениваются записками. Сначала он хотел поставить им всем двойки, но в
    тот день профессор был добрым, а потому решил разделить студентов на две
    группы: списывающих и дающих списывать, и поставить двойки только первым.
    У профессора записаны все пары студентов, обменявшихся записками.
    Требуется определить, сможет ли он разделить студентов на две группы так, чтобы
    любой обмен записками осуществлялся от студента одной группы студенту другой группы
    '''
   
    N,M = [int (x) for x in input().split()]
    
    visited = set()
    G = {}
   
    
    
    #сформируем список смежностей именно -  ОРИЕНТИРОВАННОГО ГРАФА
   
    flag= False
    
    for x in range(M):
        a,b = [int (y) for y in input().split()]
        if a not in G:
            G[a]={b}
        else:
            G[a].add(b)
    G_B=G.copy()
    l=[]
    #G = {0: {8, 10, 7}, 7: {10, 2, 4}, 10: {9, 2}, 4: {8, 11}, 3: {4, 5}, 11: {0}, 6: {8, 1, 11, 5}, 8: {11}, 9: {8, 2}}
    #N=12
    
    for i in range(N):
        if i not in G:
            G[i]=set()
    
        
    G_colors = {x : 0 for x in G}
    
    #print(G_colors)
    
    flag=False
    def dfs(start,G, visited,l):
        
        #СДЕЛАТЬ RETURN ФУНКЦИИ и функцию впихнуть в условие. ложь выкинет из цикла нахой мб?
        if start in G:

            c = 0
            visited.add(start) #добавляем в посещенную вершину
            G_colors[start] = 1
             
            for neighbour in G[start]:  #для всех соседей 
                if neighbour not in visited:#которые не посещены 
                    c = dfs(neighbour, G, visited,l) # выход 3 результата: 
                    #1 - просмотрели всех соседей
                    #2 - соседей у вершины нету
                    #3 - цикл найден
                    if c==3:
                        return 3
                elif neighbour in visited and G_colors[neighbour] == 1:
    
                    return 3
            l.append(start)

            
            G_colors[start] = 2
            return 1
        else:
          
            G_colors[start] =2
            return 2
            
    
    for vertex in G:
        if vertex not in visited:
            c=dfs(vertex,G,visited,l)
            if c==3:
                flag = True
                break
    if not flag:           
        for i in range(N):
            if i not in G_B:
                print(i, end=' ')
    else:
        print('NO')


def zad1_8():
    '''
    Дан неориентированный граф содержащий гамильтонов цикл, требуется найти этот цикл.
    
    '''
   #Убрать visited и играться цветами 
    N,M = [int (x) for x in input().split()]
    
    visited = set()
    G = {}
   
    
    
    #сформируем список смежностей именно -  НЕОРИЕНТИРОВАННОГО ГРАФА
   
    flag= False
    
    for x in range(M):
        a,b = [int (y) for y in input().split()]
        for v,u in (a,b),(b,a):
            if v not in G:
                G[v]={u}
            else:
                G[v].add(u)
    
    l=[]
    #G = {0: {8, 10, 7}, 7: {10, 2, 4}, 10: {9, 2}, 4: {8, 11}, 3: {4, 5}, 11: {0}, 6: {8, 1, 11, 5}, 8: {11}, 9: {8, 2}}
    #N=12

        
    G_colors = {x : 0 for x in G}
    
    
    
    flag=False
    def dfs(start, G, G_colors, l):
        nonlocal flag
        
        if start in G:

            c = 0
             #добавляем в посещенную вершину
            G_colors[start] = 1
            l.append(start)
       
                
            for neighbour in G[start]:  #для всех соседей 
                if not G_colors[neighbour]: #которые не посещены 
                    c = dfs(neighbour, G, G_colors, l) # выход 3 результата:
                    #1 - наткнулись на серую и нашли цикл, но он не гамельтонов
                    #2 - просмотрели всех соседей     
                    #3 - гамельтонов цикл найден
                    if c==3:
                        return 3
                   
                elif G_colors[neighbour] == 1 and 0 not in G_colors.values(): 
                    return 3
                    
                elif G_colors[neighbour] == 1 and 0 in G_colors.values():
                    
                    continue
                    #возвращаем значение в 0 что бы потом другим путём ее пройти
            G_colors[start] = 0
            l.pop()
            return 2

            
    
    for vertex in G:
        if not G_colors[vertex]: # если вершина 0 - тоесть не посещена
            c = dfs(vertex, G, G_colors, l)
            if c==3:
                flag = True
                break
   
    if flag:
       
        for x in l:
            print(x, end=' ')
    
    


