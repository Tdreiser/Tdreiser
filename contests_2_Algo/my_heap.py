class Heap():
    ''' Класс данных.
        Тип: бинарное древо
        Вид: heap (куча)
        С помощью Heap можно удобно хранить данные и быстро доставать min или
        max в зависимости от разновидности кучи.  В нашем случае min.
    '''
    def __init__(self):
        self.values = []
        #куча хранится в списке где parrent= child - 1//2, (L/R) child= parrent*2(+1 или +2)
        self.size = 0 #размер кучи

    def insert(self, x):
        self.values.append(x)
        self.size+=1
        self.sift_up(self.size - 1)
        
    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            
            #пока мы не у корня и потомок меньше предка
            self.values[i],self.values[(i-1) // 2] = self.values[(i-1) // 2],self.values[i]
            #меняем местами предка и потомка
            i=(i-1)//2
    def extract_min(self):
        if not self.size:
            return None
        tmp = self.values[0]  #временное хранение корня
        self.values[0] = self.values[-1] 
        self.values.pop() # на место корня пихаем последнее значение
        self.size -= 1 #размер уменьшаем 
        self.sift_down(0)
        return tmp
    
    def sift_down(self,i):
        while 2*i+1< self.size: #пока есть хотя бы один потомок
            j=i # запомним позицию предка и через нее высчитаем потомка
            if self.values[2*i+1] < self.values[i]: #если потомок меньше предка
                j=2*i+1 #то запомним новую позицию потомка которого надо свапнуть с предком
            if 2*i+2 <self.size and self.values[2*i+2] < self.values[j]: #если присутствует второй потомок
            #и он меньше предка
                j = 2*i+2 # то уже будем свапать второго потомка с предком
            if i == j: # если оба потомка больше предка, то смысла смотреть дальше нет, выходим.
                break
            self.values[i],self.values[j]= self.values[j],self.values[i] # свап
            i=j #снова запомним позицию предка что бы высчитать второго потомка и свапнуть поновой

def heapyfy(arr):
    heap=Heap()
    for item in arr: #заполним кучу каждым эелементом
        heap.insert(item)
    return heap
def sorted_arr(heap):
    arr = []
    while heap.size: #пока в куче есть что-то
        arr.append(heap.extract_min())# последовательно извлечем минимумы
    return arr
if __name__ == '__main__' :
    x=heapyfy([9,8,7,6,2,3,5,1,4])
    f=sorted_arr(x)
    print(f)
