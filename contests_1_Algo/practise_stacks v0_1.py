"""

>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
>>> zad_1([1,2,3,4,5,6,7])
'7 6 5 4 3 2 1 '
>>> skobki('(())()')
'correct'
>>> skobki('()))')
'incorrect'
>>> skobki('({)}')
'incorrect'
>>> skobki('({()}())')
'correct'
>>> skobki('')
'correct'
>>> skobki('(')
'incorrect'
>>> skobki('}')
'incorrect'
>>> skobki('(')
'incorrect'
"""
_stack=[]
def push(a):
    _stack.append(a)
def top():
    return _stack[-1]
def is_empty():
    return len(_stack) == 0
def clear():
    _stack.clear()
def pop():
    return _stack.pop()

def zad_1(massive):
    z=''
    for x in massive:
        push(x)
    while not is_empty():
        z+=str(pop())+' '
    return z

def skobki(word):
    '''
    проверяет корректность записи скобок
    '''
    clear()
    for c in word:
        if c  in '{(':
            push(c)
            continue
        if not is_empty():
            x=pop()
            if (c,x) ==(')','('):
                continue
            elif (c,x)== ('}','{'):
                continue
            else:
                return 'incorrect'
        else:
            return 'incorrect'
    if is_empty():
        return 'correct'
    else:
        return 'incorrect'
        
def stack_calc(l):
    '''
    стековый калькулятор
    принимает массив с постфиксной записью и возвращает результат вычислений
    либо возвращает error
    >>> stack_calc(['2','3','-','12','10','-','*','4','2','//','+'])
    '0'
    '''
    clear()

    for c in l:
        if  c.isdigit():
            push(c)   
        else:
            if not is_empty():
                x=pop()
            else:
                return 'error'
            if not is_empty():
                y=pop()
            else:
                return 'error'
            exec('push(str('+y+c+x+'))')
    x=pop()
    if is_empty():
        return x
    else:
        return 'error'

def sort_station(t):
    '''
    Функция которая преобразует инфиксную запись арифметического выражения
    в постфиксную. Выражение должно быть записано в массиве каждый операнд или
    оператор в отдельной ячейке.
    '''
    clear()
    
    priority=['-','+','/','*'] # приоритеты операторов с самого низшего к высшему
    endlist=[]
    for x in t: #для всех токенов
        if x.isdigit(): #если токен цифра то на вывод его
            endlist.append(x)
        elif is_empty(): #иначе если стек пустой то пушим туда токен
            push(x)   
        elif x in priority : #если на входе оператор то смотрим на приоритет
            while not is_empty() and top() !='(' and priority.index(x)< priority.index(top())   : 
                endlist.append(pop()) # и достаем токены из стека пока  приоритет не станет ниже
            push(x) # в остальных случаях пушим в стек токен
        elif x =='(' :
            push(x)
        elif x==')':
            while not is_empty() and top() != '(':
                endlist.append(pop())
            if not is_empty() and top()=='(':
                pop()        
    while not is_empty(): #всё что осталось в стеке достаём на вывод к оставшимся токенам
        endlist.append(pop())
        
    return endlist
trn=['3','+','4','*','(','2','-','1',')']
print(sort_station(trn))
                

                
        
    
'''
if __name__ == '__main__' :
    import doctest
    doctest.testmod()
'''

   

