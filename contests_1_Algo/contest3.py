def zad3_1():
    '''
    Вычислите XOR от двух чисел.

    Входные данные

    Два целых шестнадцатеричных числа меньших FF.

    Выходные данные

    Побитовый XOR этих чисел в шестнадцетиричном виде
    '''
    z=input()
    x=z[:z.find(' ')]
    y=z[z.find(' ')+1:]
    x=bin(int('0x'+x,16))
    y=bin(int('0x'+y,16))

    print(hex(int(x,2)^int(y,2))[2:])
    
def zad3_2():
    '''
    Сколько 1 в бинарной записи числа
    Найти, сколько единиц содержит бинарная запись числа.

    Входные данные

    Целое неотрицательное число K.

    Выходные данные

    Сколько единиц содержит бинарная запись числа.
    '''
    cnt=0
    x=bin(int(input()))
    for y in x:
        if y == '1':
            cnt+=1
    print(cnt)
    
def zad3_3():
    '''
    Сколько рыцарей?
    Ограничение по времени работы программы: 1 секундa.
    Ограничение по памяти: 32 мегабайта.
    Ввод из стандартного потока ввода (с клавиатуры).
    Вывод в стандартный поток вывода (на экран).

    На острове Буяне жили N человек, каждый из которых был либо рыцарем либо лжецом, встали в круг. Рыцари говорят только правду, лжецы всегда только лгут. Каждому человеку в кругу задали вопрос: «Кто ты и кто твой сосед слева: рыцарь или лжец?» При этом каждый человек сказал, что он – рыцарь. А ответы всех людей о левом соседе были записаны в следующем формате: 1 – рыцарь 0 – лжец. Все ответы записаны в строку через пробел. Последний спрошенный человек отвечал на вопрос о первом.

    Написать программу, которая по ответам жителей определяет, какое количество рыцарей заведомо присутствует в круге.

    Входные данные

    Первое число ( 1 < N ≤ 255 ) - количество жителей. Следующие N чисел (0 или 1), разделенных пробелами - ответы жителей.
    '''
    #x='0101'
    flag=True
    b=input()
    x=input()
    f=x.split()
    x=''
    for z in f:
        x+=z

    def riz(x,flag=False):
        a=''
        for z in x:

            if z =='0' and flag: #рыцарь указывает на лжеца
                flag=False
                a+='0'
            elif z=='0' and not flag : #лжец указывает на лжеца(рыцаря)
                flag=True
                a+='1'
            elif z=='1' and not flag: #лжец указывает на рыцаря(лжеца)
                flag=False
                a+='0'
            else:
                flag=True
                a+='1' #рыцарь указывает на рыцаря
                
        return a
    a=riz(x)
    print(a.count('1'))

def zad3_4():
    '''
    Студент покупает рис каждый день.
    В первую неделю рис стоит price монет.
    Каждый день (перед началом рабочего дня) цена риса увеличивается на delta монет (price = price + delta).
    Неделя - 7 дней.
    Студент покупал рис m недель.

    Написать программу (с циклом while), которая вычисляет сколько денег потратил студент.

    Нужны переменные:

    day - чтобы считать дни.
    Сначала day = 1.
    Если day == 8, то это первый день новой недели day = 1
    week - чтобы считать недели. Сначала week = 1.
    Если day == 8, то началась новая неделя week = week + 1
    Входные данные

    price - цена риса

    delta - на сколько увеличивается цена

    m - количество недель

    Выходные данные

    Число money - сколько денег потратил студент.
    '''
    data=input()
    l=data.split()
    price,delta,m=int(l[0]),int(l[1]),int(l[2])
    week=0
    day=1
    money=0
    while True:
        if day > 7:
            day=1
            week+=1
        if week == m:
            break
            
        
        money+=price
        price+=delta
        day+=1

        
    print(money)
    
def zad3_5():
    '''
    Скобочки
    Ограничение по времени работы программы: 1 секунда.

    Ограничение по памяти: 32 мегабайта.

    Ввод из стандартного потока ввода (с клавиатуры).

    Вывод в стандартный поток вывода (на экран).

    Некоторые скобочные структуры правильные, другие — неправильные. Ваша задача — определить правильная ли скобочная структура.

    Входные данные

    Слово в алфавите из двух круглых скобочек ( и ). Длина слова меньше 4001

    Выходные данные

    Либо NO, либо YES

    Примеры
    '''
    def funct():
        cord=list(input())
        word=cord[:]
        flag=False
        tryes=0
        x=0
        if len(word)%2==0 and cord[0] !=')':
            while cord and tryes < len(word)/2:
                if x >= len(cord):
                    print('NO')
                    return
                    break
                if cord[x]=='(' and not flag:
                    flag=True
                    memo=x
                    x+=1
                if cord[x] == ')' and flag:
                    cord.pop(x)
                    cord.pop(memo)
                    tryes+=1
                    x=0
                    flag=False
                else:
                    x+=1
                
        else:
            print('NO')
            return
        if not cord:
            print('YES')
            return
        else:
            print('NO')
            return
    funct()
    
def zad3_6():
    '''
    Заданная цифра в числе
    Сколько раз цифра d входит в десятичную запись числа n?

    Входные данные

    Число 0≤d≤9. Пробел. Целое положительное число n в десятичной системе (0 ≤ n ≤ 3·10 6) .

    Выходные данные

    Сколько раз цифра d входит в запись числа n.
    '''

    inp=input()
    digit=inp[0]
    posled=inp[2:]

    def counter(digit,posled):
        cnt=0
        for number in posled:
            if number == digit:
                cnt+=1
        else:
            return cnt
    print(counter(digit,posled))

    def newcnt(digit,posled):
        
        posled=list(posled)
        posled.sort()
        left=-1
        right=len(posled)+1
        midle=len(posled)//2
        while right-left>1:
            if int(posled[left])< int(digit):
                left=midle
            else:
                right=midle
            midle=len(posled[left:midle])//2
        cnt=0
        for number in posled[left:]:
            
            if number == digit:
                cnt+=1
        else:
            return cnt
            
    newcnt(digit,posled)
def zad3_7():
    '''
    Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.

    Входные данные

    Строка, заканчивающаяся точкой, длиной не более 1000 символов. Точку сортировать не нужно. Все, что находится после первой точки - игнорировать.

    Выходные данные

    Отсортированная строка с точкой на конце.
    '''
    mass=list(input())
    cnt=0
    for z in mass:
        if z!='.':
            cnt+=1
        else:
            break
    mass=mass[:cnt]
    
    def sorting_for_ASCII(massive):
        if len(massive)<=1:
            return
        barrier=massive[0]
        left=[]
        right=[]
        midle=[]
        for element in massive:
            if ord(element)<ord(barrier):
                left.append(element)
            elif ord(element) == ord(barrier):
                midle.append(element)
            else:
                right.append(element)
        sorting_for_ASCII(left)
        sorting_for_ASCII(right)
        k=0
        for element in left+midle+right:
            massive[k]=element
            k+=1
    sorting_for_ASCII(mass)
    last_sorted_word=''
    for x in mass:
        last_sorted_word+=x
        
    print(last_sorted_word+'.')   
def zad3_8():
    '''
    Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.

    Входные данные

    Строка, заканчивающаяся точкой, длиной не более 1000 символов. Точку сортировать не нужно. Все, что находится после первой точки - игнорировать.

    Выходные данные

    Отсортированная строка с точкой на конце.
    '''
    N=int(input())
    massive=input()
    def sort_numbers(massive):
        local_massive=[]
        f=''
        for z in massive:
            if z!=' ':
                f+=z
            else:
                local_massive.append(f)
                f=''
        else:
            local_massive.append(f)

        return local_massive
    mass=sort_numbers(massive)


    def choise_sort(massive):
        
        fix=0
        for z in massive:
            if len(z)> fix:
                fix=len(z)
                
        for z in range(len(massive)): 
            while len(massive[z])<fix:
                massive[z]='0'+massive[z]
    
        x=-1
        N=len(massive)
        
        for bypass in range(1,N):
            for k in range(0,N-bypass): 
                while len(massive[k])>=-x and int(massive[k][x]) == int(massive[k+1][x]):#решить проблему с переполняющимся x в цикле    
                    if len(massive[k])==-x:
                        x=-1
                        break
                    else:
                        x-=1    
                if int(massive[k][x]) > int(massive[k+1][x]):
                    massive[k],massive[k+1] = massive[k+1],massive[k]
                    x=-1#сброс  
                else:
                    x=-1#сброс
                    
    choise_sort(mass)


    read=''
    xx=0
    zz=0
    for lit in mass:
        while mass[xx].startswith('0'):
            zz+=1
            mass[xx]=lit[zz:]
        xx+=1
        zz=0
        if xx==range(len(mass)):
            break
    for lit in mass:
        print(lit,end=' ')
        
def zad3_9():
    '''
    Задача I: Матпомощь
    Студентов надо построить в шеренгу от самого легкого до самого тяжелого. Кто мало весит - тем выдать матпомощь..
    При одинаковом весе сначала идет студент с большим ростом (тощий).

    Формат входных данных
    Целое число N, 0 < N < 100, - количество студентов. Затем N пар чисел (float) через пробел - рост в метрах и вес в килограммах одного студента.

    Формат результата
    Рост и вес (печатать рост с точностью до сантиметров, а вес - до граммов) по одному студенту на строку от первого студента в шеренге к последнему
    '''
    N=int(input())
    mass=[input() for i in range(N)]

    z=0

    for lit in mass:
        x=lit.find(' ')
        mass[z]=[float(lit[:x])]+[float(lit[x+1:])]
        z+=1

    def choise_sort(massive):
        for bypass in range(1,N):
            for k in range(0,N-bypass):
        
                if massive[k][1] > massive[k+1][1]:
                    massive[k],massive[k+1] = massive[k+1],massive[k]
                    
                elif massive[k][1] == massive[k+1][1]:
                    if massive[k][0] < massive[k+1][0]:
                        massive[k],massive[k+1] = massive[k+1],massive[k]
                                  
    choise_sort(mass)

    for x in mass:
        print('%.2f'%x[0],'%.3f'%x[1])
def zad3_10():
    '''
    Задача J: Словарь для блондинки
    Блондинка Даша любит решать кроссворды на латинском языке, пользуясь орфографическим словарем. Часто Даша отгадывает последние буквы слова и долго ищет каким словам подходит такая концовка. Она мечтает о словаре, где бы слова были разбиты на главы по количеству букв в слове и написаны задом наперед. Помогите ей составить такой словарь по заданному орфографическому словарю латинском языка.

    Формат входных данных
    В первой строке содержится единственное целое число N (1≤N≤100) — количество латинских слов в словаре. Далее следует N слов по одному слову на строку. Все слова состоят только из маленьких латинских букв. Общее количество слов на входе не превышает 100. Длина каждого слова не превосходит 15 символов.

    Формат результата
    Длина слов в данном блоке. На следующих строках слова задом наперед и исходное слово через пробел в лексикографическом порядке.
    '''

    N=int(input())
    mass=[input()for i in range(N)]
    x=0
    def hoar(massive):
        if len(massive)<=1:
            return
        barrier=len(massive[0])
        l=[]
        r=[]
        m=[]
        for x in massive:
            if len(x)<barrier:
                l.append(x)
            elif len(x)==barrier:
                m.append(x)
            else:
                r.append(x)
        hoar(l)
        hoar(r)
        k=0
        for x in l+m+r:
            massive[k]=x
            k+=1
            
    hoar(mass)
    f=[]
    mirk=[]
    fg=0
    for i in range(len(mass)):
        if fg!=i:
            continue
        for z in range(i,len(mass)):
            if len(mass[i])==len(mass[z]):
                f.append(''.join(reversed(mass[z])))
            else:
                mirk.append(f)
                f=[]
                fg=z
                break        

    else:
        mirk.append(f)
        

    for massive in mirk:
            x=0
            N=len(massive)
            
            for bypass in range(1,N):
                for k in range(0,N-bypass): 
                    while len(massive[k])>=x and massive[k][x] == massive[k+1][x]:  
                        if len(massive[k])==x:
                            x=0
                            break
                        else:
                            x+=1    
                    if massive[k][x] > massive[k+1][x]:
                        massive[k],massive[k+1] = massive[k+1],massive[k]
                        x=0#сброс  
                    else:
                        x=0#сброс
    x=0

    for lit in mirk:
        for i in lit:
            if len(i)>x:
                x=len(i)
                print(x)
                print(i,''.join(reversed(i)))
            else:
                print(i,''.join(reversed(i)))


