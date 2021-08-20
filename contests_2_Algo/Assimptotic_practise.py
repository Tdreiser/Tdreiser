import matplotlib.pyplot as plt
import time
import string
def first_ex():
    def get_pop_time(size, repeat_count, pop_postion=None):
        '''
        size - размер списка из нулей на котором будем тестировать скорость операции pop
        repeat_count - количество повторений для усреднения
        pop_position - позиция с которой делаем pop
        '''
        l = [0] * size
        start_time = time.time()
        if pop_postion == None:
            l.pop()
        else:
            l.pop(pop_postion)
        end_time = time.time()
        return (end_time - start_time) / repeat_count

    repeat_count = 1000

    values1 = [get_pop_time(size,1000) for size in range(10, 10000)]
    values2 = [get_pop_time(size,1000,0) for size in range(10, 10000)]
    values3 = [get_pop_time(size,1000,-1) for size in range(10, 10000)]

    plt.plot(values1, label='Pop no args')
    plt.plot(values2, label='Pop start list')
    plt.plot(values3, label='Pop end list')
    plt.ylabel('pop time')
    ax = plt.subplot(111)
    ax.legend()
    plt.show()
    
def secnd_ex():
    '''
    Вывести на экран все элементы множества A, которых нет в множестве B.
    '''
    A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
    B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
    for x in A:
        if x not in B:
            print(x,end=' ')
    print()
    print(A-B)
    print(A.difference(B))
    
def thrd_ex():
    A = set('0123456789')
    B = set('02468')
    C = set('12345')
    D = set('56789')
    print(((A-B)&(C-D))|((D-A)&(B-C)))

def forth_ex():
    '''
    Дан текст на некотором языке. Требуется подсчитать сколько раз каждое слово входит в
    этот текст и вывести десять самых часто употребяемых слов в этом тексте и количество их
    употреблений.
    В качестве примера возьмите файл с текстом лицензионного соглашения Python
    /usr/share/licenses/python/LICENSE.
    '''
    
    file = open('C:\PY38\LICENSE.txt','r').read()
    for c in string.punctuation:
        if c in file:
            file=file.replace(c,' ')
            
    file=file.lower()
    d={}
    for f in file.split():
        if f in d.keys():
            d[f]+=1
        else:
            d[f]=1
            
    for i in range(10):        
        for key in list(d.keys()):
            flag=True
            for dk in list(d.keys()):
                if d[key]<d[dk]:
                    flag=False
            if flag:
                print(key,d.pop(key, None))
                
def fifth_ex():
    '''
    Дан словарь task4/en-ru.txt с однозначным соответствием английских и русских слов в
    таком формате:

    cat - кошка

    dog - собака

    mouse - мышь

    house - дом

    eats - ест

    in - в

    too - тоже

    Здесь английское и русское слово разделены двумя табуляциями и минусом: '\t-\t'.

    В файле task4/input.txt дан текст для перевода, например:

    Mouse in house. Cat in house.
    Cat eats mouse in dog house.
    Dog eats mouse too.
    Требуется сделать подстрочный перевод с помощью имеющегося словаря и вывести
    результат в output.txt. Незнакомые словарю слова нужно оставлять в исходном виде.
        
    '''
    d={}
    for line in open('C:\code\datafile.txt'):
        d[line.split()[0]]=line.split()[2]
    
    output = open('C:\code\output.txt','w')
    
    for line in open('C:\code\exampe.txt'):
        x=line
        for c in string.punctuation:
            if c in line:
                    liner=line.replace(c,' ')
        for word in liner.split():

            if word.lower() in d.keys():
                x=x.replace(word,d[word.lower()])
        output.write(line)
        output.write(x)
    output.close()
    
def sixth_ex():
    '''
    Дан список стран и языков на которых говорят в этой стране в формате
    <Название Страны> : <язык1> <язык2> <язык3> ... в файле task5/input.txt. На ввод
    задается N - длина списка и список языков. Для каждого языка укажите, в каких
    странах на нем говорят.
    '''
    d={}
    for line in open('C:\code\ex_6.txt'):
        for lang in line.split(':')[1].split():
            if lang in d.keys():
                d[lang]+=[line.split(':')[0]]
            else:
                d[lang]=[line.split(':')[0]]
    x=' '
    while True:
        x = input('input lang: ')
        if x:
            for country in d[x]:
                print(country, end=' ')
            print('')
        else:
            break
        
def seventh_ex():
    '''
    В файле ex_7.txt находятся строки англо-русского словаря в таком формате:

    cat - кошка
    dog - собака
    home - домашняя папка, дом
    mouse - мышь, манипулятор мышь
    to do - делать, изготавливать
    to make - изготавливать
    Здесь английское слово (выражение) и список русских слов (выражений) разделены
    двумя табуляциями и минусом: '\t-\t'.

    Требуется создать русско-английский словарь и вывести его в файл ex_7_output в таком
    формате:

    делать - to do
    дом - home
    домашняя папка - home
    изготавливать - to do, to make
    кошка - cat
    манипулятор мышь - mouse
    мышь - mouse
    собака - dog
    Порядок строк в выходном файле должен быть словарным с человеческой точки зрения
    (так называемый лексикографический порядок слов). То есть выходные строки нужно
    отсортировать.
    '''
    d={}
    for line in open('C:\code\ex_7.txt'):
        for word in  line.split('-')[1].split(','):
            if word in d.keys():
                d[word]+=[line.split('-')[0]]
            else:
                d[word]=[line.split('-')[0]]
    output=open('C:\code\ex_7_output.txt','w')
    prep=list(d.keys())
    prep.sort()
    
    x=''
    for ru in prep:
        for eng in d[ru]:
            x+=' '+eng
        end=ru.strip()+'\t-\t '+x.strip()
        output.write(end+'\n')
        x=''
    
def eitth_ex():
    '''
    Даны два файла словарей: task8/en-ru.txt и task8/ru-en.txt (в формате, описанном в упражнении
    №6).

    en-ru.txt:

    home - домашняя папка
    mouse - манипулятор мышь
    ru-en.txt:

    дом - home
    мышь - mouse
    Требуется синхронизировать и актуализировать их содержимое.

    en-ru.txt:

    home - домашняя папка, дом
    mouse - манипулятор мышь, мышь
    ru-en.txt:

    дом - home
    домашняя папка - home
    манипулятор мышь - mouse
    мышь - mouse
    '''
    d_eng={}
    d_ru={}
    eng=open('C:\code\ex_8_eng_ru.txt')
    ru=open('C:\code\ex_8_ru_eng.txt')
    
    for line in eng:#переводим англ текст в словарь
        if line.split('\t-\t')[0] in d_eng.keys():
            d_eng[line.split('\t-\t')[0]] += line.split('\t-\t')[1].strip().split(',')
        else:
            d_eng[line.split('\t-\t')[0]] = line.split('\t-\t')[1].strip().split(',')
    for line in ru: #переводим ру текст в словарь
        if line.split('\t-\t')[0] in d_ru.keys():
            d_ru[line.split('\t-\t')[0]] += line.split('\t-\t')[1].strip().split(',')
        else:
            d_ru[line.split('\t-\t')[0]] = line.split('\t-\t')[1].strip().split(',')
    
    for eng_wrd in d_eng.keys():#апдейтим ру словарь
        for ru in d_eng[eng_wrd]:
            try:
                d_ru[ru]
                if eng_wrd not in d_ru[ru]:
                    d_ru[ru]+=[eng_wrd]
            except KeyError:
                d_ru[ru]=[eng_wrd]
    

    for ru_wrd in d_ru.keys(): #апдейтим англ словарь
        for eng in d_ru[ru_wrd]:
            try:
                d_eng[eng]
                if ru_wrd not in d_eng[eng]:
                    d_eng[eng]+=[ru_wrd]
            except KeyError:
                d_eng[eng]=[ru_wrd]
                
    new_eng=open('C:\code\ex_8_eng_ru_new.txt','w')# следом записываем результат в файлы
    for eng in d_eng:
        buf=''
        for i in d_eng[eng]:
            buf+=i+','
        new_eng.write(eng+'\t-\t'+buf[0:-1]+'\n')
    new_ru=open('C:\code\ex_8_ru_eng_new.txt','w')
    for ru in d_ru:
        buf=''
        for i in d_ru[ru]:
            buf+=i+','
        new_ru.write(ru+'\t-\t'+buf[0:-1]+'\n')
    
            
def eith_ex():
    '''
    В одном очень дружном доме, где живет Фёдор, многие жильцы оставляют ключи от
    квартиры соседям по дому, например на случай пожара или потопа, да и просто чтобы
    покормили животных или полили цветы.

    Вернувшись домой после долгих странствий, Фёдор обнаруживает, что потерял свои
    ключи и соседей дома нет. Но вдруг у домофона он находит чужие ключи. Помогите
    Федору найти ключи от своей квартиры в квартирах соседей.

    На ввод подается файл input.txt, в котором в первой строке записано три числа через
    пробел N - номер квартиры Фёдора, M - номер квартиры от которой Федор нашел ключи,
    K - ключ от этой квартиры. Далее i-я строка хранит описание ключей запертых в i-й квартире
    в формате <m_i0 - номер квартиры> <k_i0 - ключ>,<m_i1 - номер квартиры> <k_i1 - ключ>
    ,... , причем реальные номера квартир "зашифрованы" ключем от i-й квартиры(Ki) и находятся
    по формуле m_ij' = m_ij - Ki. Номера квартир начинаются с 0 (кпримеру вторая строка файла
    соответствует 0-й квартире).

    Нужно вывести ключ от квартиры Федора или None если его найти не получилось.
    '''
    found='4 0 1'
    fedr,kv,key = found.split()
    x=['1 1,2 0,3 1,4 0'],['3 0'],['5 1,6 0'],['1 1'],['2 1']
    d={ i : x[i] for i in range(len(x))}
    for room in list(d.keys()):
        for x in room.split(','):
            if (int(x.split()[0]) - int(x.split()[1])) == int(fedr):
                nkv = x.split()[0]
                nkey = x.split()[1]
                point = room
                break
    else:
        print('gg')
    flag = False
    
    
