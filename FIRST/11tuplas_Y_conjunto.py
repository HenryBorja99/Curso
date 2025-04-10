# ================================
# 11. TUPLAS (listas inmutables) y CONJUNTOS
# ================================
# tupla = (1, 2, 3, 4, 5)

tupla = (1,2,3, "Hola mundo")

print (tupla)
lista1 =list(tupla)
lista1.append(2)
print(lista1)

#Conjuntos
#grupo de elementos desornedados, y no admiten elementos duplicados
Conjunto = set() # se utiliza para crear un conjunto ya que python podría confunfir con diccionarios

Conjunto = {"hola", 1, 2.35,6} 
#agregar más elementos al conjunto
Conjunto.add(5)
Conjunto.add(9)
Conjunto.add(12)
Conjunto.add("a")
print(Conjunto)
#eliminar un elemento del conjunto
Conjunto.discard("a")
# ELemntos dentro de un conjunto 
print(1 in Conjunto)
#vaciar todo el conjunto
Conjunto.clear()
print(f"El conjunto esta vacio ?{Conjunto}")

#operaciones con conjuntos
a = {1,2,3}
b = {3,5,6}
print(f"Son iguales los conjuntos? {a==b}")
#queremos unir dos conjuntos
c = a | b
print(f"LA union de los conjuntos es: {c}")
#queremos saber la interseccion
c = a & b
print(f"La intesceccion de los conjuntos es: {c}")
#la diferencia de los conjuntos
c = a - b
print(f"La diferencia de los conjuntos es: {c}")
# la diferncia simetrica
c = a ^ b
print(f"La diferencia simetrica de los conjuntos es: {c}")
# como determinar si un conjunto es un subconjunto de otro
c = {1,2,3,4,5}
print(f"\nEl conjunto a= {a} es un subconjunto de c= {c} ?\nla respuesta es ={a.issubset(c)}") # \n hace un salto de linea
#como determinar si un conjunto es un superconjunto de otro
# un superconjunto es aquel que contiene todos los elementos de otro conjunto
print(f"\nEl conjunto c= {c} es un superconjunto de a= {a}? \t\nla respuesta es ={c.issuperset(a)}")#\t hace un tabulador
# como determinar si un conjunto es disjunto de otro
# dos conjuntos son disjuntos si no tienen elementos en comun
print(f"\nEl conjunto a= {a} es disjunto de b= {b} \nla respuesta es ={a.isdisjoint(b)}")
#como dterminar conjuntos inmutables
# los conjuntos son mutables, pero si queremos crear un conjunto inmutable se utiliza frozenset
a = frozenset({1,3,5,7})