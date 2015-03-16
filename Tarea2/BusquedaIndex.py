__author__ = 'nelson'
#Esta función es la que se encarga de dividir el array en mitades recursivamente, meter el numero mayor en una lista auxiliar, hasta reducir esa lista auxiliar a 1 o 2 elementos 
def indexMayorAux2(lista,listaAux1,numeroMayor): 
    if (len(lista) == 1) :#si el len de la lista es 1 mete ese numero en la listaAux que sera retornada
        listaAux1.append(lista[0])
    elif (len(lista) == 2):
        if ((lista[0]>lista[1] and lista[0] != numeroMayor)or(lista[0]<lista[1] and lista[1] == numeroMayor)):#si el len 2 revisa cual es el mayor de esos 2 y que no sea repetido con el mayor
            listaAux1.append(lista[0])
        elif ((lista[0]<lista[1] and lista[1] != numeroMayor)or((lista[0]>lista[1] and lista[0] == numeroMayor))) :
            listaAux1.append(lista[1])
    else:#si es más de 2 divide el problema
        indexMayorAux2(lista[0:len(lista)//2],listaAux1,numeroMayor)
        indexMayorAux2(lista[len(lista)//2:len(lista)],listaAux1,numeroMayor)
    return listaAux1
#Esta Función se encarga de revisar los casos base de 1 o 2 elementos para devolver el mayor, lista de retorno es el array donde se devolvera los 2 numero mayores, #numeromayor es (si ya fue encontrado) el numero mayor y no repetirlo
def indexMayorAux1(lista,listaRetorno,numeroMayor):
    print(lista)
    if (len(lista) == 1 or(len(lista)==2 and (lista[0]>lista[1] and lista[0] != numeroMayor ))) : #revisa el primer caso base donde solo hay un numero en el array
        print(lista[0])                                                                           #o el primer numero del array ya esta buscado como el mayor
        listaRetorno.append(lista[0])
    elif(len(lista)==2 and (lista[1]>lista[0] and lista[1] != numeroMayor)):                    #revisa el segundocaso base donde el segundo numero del array es mayor
        listaRetorno.append(lista[1])                                                           #es mayor que el primero
    else:
        listanueva = []
        lista2 = indexMayorAux2(lista, listanueva,numeroMayor) #llama al segundo auxiliar (donde se aplica el divide y conquista) con la lista, una listanueva para  #guardar el array reducido por las diviciones
        indexMayorAux1(lista2,listaRetorno,numeroMayor)#se llama a si misma para ver si el array se reducio lo suficiente como para ser evaluado en un caso base
    return listaRetorno


#Estuscar a Función se encarga de buscar el index de los numeros
def indexMayor(lista):
    listaRetorno = []#array donde se devolvera los 2 numeros mayores
    numeroMayor = 'a' #esta variable sirve como indicador para saber si ya se tiene el numero mayor y no repetirlo, si es 'a' significa que aun no hay numero mayor
    x =(indexMayorAux1(lista,listaRetorno,numeroMayor)) #llamamos a la primera función auxiliar para buscar el numero mayor
    mayor = lista.index(x[0]);
    numeroMayor = x[0]
    y = (indexMayorAux1(lista,listaRetorno,numeroMayor))
    segundo = lista.index(y[1])
    return "El Indice del numero mayo es: " + str(mayor) + ", el Segundo Indice mayor es: " + str(segundo)





listaPrueba=[1, 5, 2, 6, 7, 82, 0, 9, 8, 25, 4,
             1000,86]
numeroPrueba = 0
listap = indexMayor(listaPrueba)
print(listap)

