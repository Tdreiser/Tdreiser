def zad4_1():
    '''
    Вам даны 2 координаты 2 клеток на шахматном поле. Нужно ответить на вопрос,
    можно ли попасть из одной клетки в другую за не более чем 2 хода конем.
    В случае, если попасть возможно, надо вывести количество ходов,
    за которое это можно сделать. Если попасть невозможно, следует вернуть -1.
    '''
    zz=int(input())
    ii=int(input())
    qq=int(input())
    yy=int(input())

    def horse_chess(i,z,q,y):
        deck= [[' ' for i in range(8)] for z in range(8)]
        deck[z][i]='-'
        deck[q][y]='+'
        rez=[-1]


        def check_bourder(i,z):
            '''
            Определяем границы хода
            '''
            if i>=0 and i<8 and z>=0 and z<8:

                return True
            
            else:

                return False
                
        def hod(i,z,n=1):
            '''
            Ходим
            '''
            if deck[z][i]=='+':
                 if n==1:
                     
                     rez.append('0')
                 elif n==0:
                     
                     rez.append('1')
                 elif n==-1:
                     
                     rez.append('2')

            
            if n<=-1:


                return

            
            if check_bourder(i-1,z-2) and deck[z-2][i-1]!='h':
               
                deck[z-2][i-1]= 'h' if deck[z-2][i-1]!='+' else '+' 
                hod(i-1,z-2,n-1)                                       # I ЧЕТВЕРТЬ
                
            if check_bourder(i-2,z-1)and deck[z-1][i-2]!='h':
                deck[z-1][i-2]='h' if deck[z-1][i-2]!='+' else '+'
                hod(i-2,z-1,n-1)
                
            if check_bourder(i+2,z-1)and deck[z-1][i+2]!='h':           # II ЧЕТВЕРТЬ
                deck[z-1][i+2]='h' if deck[z-1][i+2]!='+' else '+'
                hod(i+2,z-1,n-1)
                
            if check_bourder(i+1,z-2)and deck[z-2][i+1]!='h':
                deck[z-2][i+1]='h' if deck[z-2][i+1]!='+' else '+'
                hod(i+1,z-2,n-1)

            if check_bourder(i+1,z+2)and deck[z+2][i+1]!='h':          # III ЧЕТВЕРТЬ
                deck[z+2][i+1]='h' if deck[z+2][i+1]!='+' else '+' 
                hod(i+1,z+2,n-1)
                
            if check_bourder(i+2,z+1)and deck[z+1][i+2]!='h':
                deck[z+1][i+2]='h' if deck[z+1][i+2]!='+' else '+'
                hod(i+2,z+1,n-1)

            if check_bourder(i-1,z+2)and deck[z+2][i-1]!='h':          # IV ЧЕТВЕРТЬ
                deck[z+2][i-1]='h' if deck[z+2][i-1]!='+' else '+'
                hod(i-1,z+2,n-1)

            if check_bourder(i-2,z+1)and deck[z+1][i-2]!='h':
                deck[z+1][i-2]='h' if deck[z+1][i-2]!='+' else '+'
                hod(i-2,z+1,n-1)
                
            
               



            return 
            
        hod(i,z)
        '''
        print(rez)    
        for cell in deck:   
            print(cell)
        '''
        
        if len(rez)>1:
            print(rez[1])
        else:
            print(rez[0])
    horse_chess(ii-1,zz-1,qq-1,yy-1)
    
def zad4_2():
    q=int(input())

    platf=[int(input()) for i in range(q)]

    def cost_energy(n,pltf:list):
        f=0
        jmp=0
        
        if abs(pltf[1]-pltf[0])+abs(pltf[2]-pltf[1]) < abs((pltf[0]-pltf[2])*3):
            f+=1
        else:
            f+=2

        if f+1<n-1:
            for i in range(1,n-1):
                if f+1==n-1:
                    
                    cost[i]=cost[i-1]+abs(pltf[f]-pltf[f+1])
                    print('f1=',f)
                    jmp+=1
                    break
                
                elif f+2==n-1 and abs(pltf[f]-pltf[f+1])+abs(pltf[f+1]-pltf[f+2]) >= abs((pltf[f]-pltf[f+2])*3):
                    cost[i]=cost[i-1]+abs((pltf[f]-pltf[f+2])*3)
                    print('f2=',f)
                    jmp+=1
                    break
                
                elif f+2==n-1 and abs(pltf[f]-pltf[f+1])+abs(pltf[f+1]-pltf[f+2])< abs((pltf[f]-pltf[f+2])*3):
                    cost[i]=cost[i-1]+abs(pltf[f]-pltf[f+1])
                    cost[i+1]=cost[i]+abs(pltf[f+1]-pltf[f+2])
                    print('f3=',f,'i',i)
                    jmp+=2
                    break
                
                if abs(pltf[f]-pltf[f+1])+abs(pltf[f+1]-pltf[f+2])< abs((pltf[f]-pltf[f+2])*3):
                    cost[i]=cost[i-1]+abs(pltf[f]-pltf[f+1])
                    f+=1
                    jmp+=1
                    
                else:
                    cost[i]=cost[i-1]+abs((pltf[f]-pltf[f+2])*3)
                    f+=2
                    jmp+=1
                

        elif f==2:
            cost[1]=cost[0]
            jmp+=1

        else:
            cost[1]=cost[0]+abs(platf[f]-platf[f+1])
            jmp+=1

        print(cost[jmp])
        
    if q<2:
        print(0)
    elif 1==q-1:        
        cost=[abs(platf[0]-platf[1])]
        print(cost[0])
        
    else:
        cost=[min(abs(platf[0]-platf[1]),abs((platf[0]-platf[2])*3))]+[0]*(q-1)
        cost_energy(q,platf)

def zad4_3():
    def king_VS_horse(z,i):
        
        
        def horse_chess(z,i):
            deck= [[' ' for z in range(8)] for i in range(8)] # моделируем доску
            deck[z][i]='h' # horse point


            def check_bourder(z,i):
                '''
                Определяем границы хода
                '''
                if i>=0 and i<8 and z>=0 and z<8:

                    return True
                
                else:

                    return False
            def hod(z,i,n=0):
                '''
                Ходим
                '''

                if n<=-1:
                    return
                
                if check_bourder(i-1,z-2) and deck[z-2][i-1]!='h':
                   
                    deck[z-2][i-1]= 'h' if deck[z-2][i-1]!='+' else '+' 
                    hod(i-1,z-2,n-1)                                       # I ЧЕТВЕРТЬ
                    
                if check_bourder(i-2,z-1)and deck[z-1][i-2]!='h':
                    deck[z-1][i-2]='h' if deck[z-1][i-2]!='+' else '+'
                    hod(i-2,z-1,n-1)
                    
                if check_bourder(i+2,z-1)and deck[z-1][i+2]!='h':           # II ЧЕТВЕРТЬ
                    deck[z-1][i+2]='h' if deck[z-1][i+2]!='+' else '+'
                    hod(i+2,z-1,n-1)
                    
                if check_bourder(i+1,z-2)and deck[z-2][i+1]!='h':
                    deck[z-2][i+1]='h' if deck[z-2][i+1]!='+' else '+'
                    hod(i+1,z-2,n-1)

                if check_bourder(i+1,z+2)and deck[z+2][i+1]!='h':          # III ЧЕТВЕРТЬ
                    deck[z+2][i+1]='h' if deck[z+2][i+1]!='+' else '+' 
                    hod(i+1,z+2,n-1)
                    
                if check_bourder(i+2,z+1)and deck[z+1][i+2]!='h':
                    deck[z+1][i+2]='h' if deck[z+1][i+2]!='+' else '+'
                    hod(i+2,z+1,n-1)

                if check_bourder(i-1,z+2)and deck[z+2][i-1]!='h':          # IV ЧЕТВЕРТЬ
                    deck[z+2][i-1]='h' if deck[z+2][i-1]!='+' else '+'
                    hod(i-1,z+2,n-1)

                if check_bourder(i-2,z+1)and deck[z+1][i-2]!='h':
                    deck[z+1][i-2]='h' if deck[z+1][i-2]!='+' else '+'
                    hod(i-2,z+1,n-1)

                return 
                
            hod(z,i)
            '''
            for cell in deck:
                print(cell)
            '''
            def king_moving():
                desk= [[0 for z in range(9)] for i in range(9)]
                desk[1][1]=1
          
                
                for i in range(1,9):
                    for z in range(1,9):
                        if (z!=1 or i!=1) and deck[z-1][i-1]!='h':
                            desk[z][i]=desk[z-1][i-1]+desk[z-1][i]+desk[z][i-1]
                '''
                for cell in desk:   
                   print(cell)
                '''
                print (desk[8][8])
            king_moving()
            
                
                
            
                
        horse_chess(z,i)
        
    find=input()   
    coord_list_vert= '12345678'
    coord_list_gor = 'abcdefgh'

    for vert in coord_list_vert:
        for gor in coord_list_gor:
            if gor+vert == find:
                zz=coord_list_vert.find(vert)
                ii=coord_list_gor.find(gor)


                    

    king_VS_horse(zz,ii)



def zad4_4():
    '''
    Написать функцию make_exchange(money, coins),
    которая принимает сумму денег (целое число) и
    массив номиналов разменных монет (целых чисел)
    (возможно пустой) и возвращает количество способов
    произвести размен.Считаем, что разменных монет бесконечное
    множество.
    '''
    moned=20 #можно инпутами ввести
    coinz=[1,2,5]
    def make_exchange(money,coins):
        coins=[0]+coins # добавляем нулевую монету, ПАТАМУШИТА ТАК НАДО
        #генерируем список всех результатов пока они нулевые
        test_list=[[0 for x in range(money+1)] for z in range(len(coins))]
        
        for x in range(len(coins)):
            test_list[x][0]=1 
        #зная точно что при любом колличестве монет сумму 0 можно разменять
        #ровно одним способом
        for x in range(1,money+1):
            if x%coins[1]==0:
                test_list[1][x]=1
        #не берем в расчёт то что уже посчитали, это крайние случаи        
        zz=2
        for t in range(2,len(coins)):
            zz+=1
            for k in range(1,money+1):
                zero=0
                for x in coins[1:zz]:
                    if k-x>=0:#рекурсивная формула будет проходить по известным результатам
                        zero+=test_list[coinz.index(x)][k-x]# ЕСЛИ k-x то увеличиваем промежуточный результат, иначе он будет нулевым 
                                           
                test_list[t][k]=zero
                
                
               
        return test_list


    print(make_exchange(moned,coinz))
zad4_4()
