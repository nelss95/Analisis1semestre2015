__author__ = 'nelson'
def insertionSort(lista):
   for i in range(1, len(lista)):

     ValorActual = lista[i]
     position = i

     while position >0 and lista[position-1] > ValorActual:
         lista[position] = lista[position-1]
         position = position-1

     lista[position] = ValorActual

lista = [54,26,93,17,77,31,44,55,20]
insertionSort(lista)
print(lista)