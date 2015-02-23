__author__ = 'nelson'

def selectionSort(lista):
   for i in range(len(lista)-1,0,-1):
       max=0
       for j in range(1,i+1):
           if lista[j]>lista[max]:
               max = j

       temp = lista[i]
       lista[i] = lista[max]
       lista[max] = temp

lista = [54,26,93,17,77,31,44,55,20]
selectionSort(lista)
print(lista)