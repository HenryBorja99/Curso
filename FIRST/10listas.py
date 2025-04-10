
# 10. LISTAS
# ================================
# lista = [1, 2, 3, 4, 5]
'''
listas
'''
# la lista tiene indices desde 0 hasta n-1
#Para mostrar el nuemro del elemento va [n-1]
# al ejecutar [-1] = ultimo elemento que esta lista tiene
# Para delimitar una sublista se utiliza [0:5]=[:5] imprime un elemento antes del numero que lo encierra
# con la funcion len() te permite contar el numero de elementos
# Se pueden "sumar listas"
lista = [ 1,2,4,5,6,7,8,9]
lista.append(8) #insertar elementos al final de la lista
lista.insert(2,3) # determina en donde esta el indice
lista.extend([10,11,12,13]*2) #varios elementos al final de la lista


print(lista)
print(14 in lista) #elemento esta dentro de la lista
print(lista.index(10)) #en que posición se encuentra un elemento
print(lista.count(8)) #Numero de veces que hay un elemento
lista.pop(9) #elimina el ultimo elemento de la lista()
lista.reverse() #Reverso de la lista 
print(lista)

#odenar el orden de la lista

lista.sort() #ordena de mayor a menor
print(lista)
lista.sort(reverse=True)
print(lista)
lista.remove(8) #elimina el elemento que ingresas
lista.clear() # eliminar toda la lista
print(lista)