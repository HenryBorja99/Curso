# ================================
# 1. PARA COMENTAR UNA LÍNEA SE USA EL SÍMBOLO DE NUMERAL
# ================================

'''
para comentar varias lineas se usa tres comillas dobles al inicio y al final
python permite el tipado dinámico, es decir, no es necesario declarar el tipo de variable
El tipado dinámico es una característica de los lenguajes de programación 
en la que no es necesario declarar el tipo de variable que se va a utilizar.
'''
# ================================
# 2. DECLARACIÓN DE LAS VARIABLES
# ================================
edad = 25
nombre = "Henry"
booleano = True
flotante = 4.5
print(edad)
print(nombre)
print(booleano)
print(flotante) 


# ================================
# 3. OPERADORES ARITMÉTICOS
# ================================
a =5
b = 10
resta = a - b
print("la resta es: " + str(resta))
suma = a + b
print ("la suma es: "+ str(suma))
division = a / b
print ("La división es: "+str(division))
multiplicacion = a * b
print ("La multiplicación es: "+str(multiplicacion))
modulo = a % b
print ("El módulo es: "+str(modulo))
exponente = a ** b
print ("El exponente es: "+str(exponente))


# ================================
# 4. OPERADORES DE COMPARACIÓN Y RELACIONALES
# los operadores de comparación y relacionales se utilizan para comparar dos valores
#primero se ejecutan los aritméticos y luego los de comparación
# ================================
#no olvides las reglas de precedencia 
#1. ()
#2. **
#3. *, /, % 
#4. +, -
#5. =
# Ejemplo utilizando las reglas de precedencia
resultado = (a + b) * (a - b) ** 2 / b % a
print("El resultado del cálculo con las reglas de precedencia es: " + str(resultado))

#6. ==, !=, <, >, <=, >=
#7 =, +=, -=, *=, /=, %=, **=
relacional = a == b
print("El resultado de la comparación es: "+str(relacional))


# ================================
# 5. OPERADORES LÓGICOS
# ================================
# not, and, or
#permite contrastar dos o más expresiones booleanas
# Ejemplo de operadores lógicos
# and: devuelve True si ambas expresiones son verdaderas
# or: devuelve True si al menos una de las expresiones es verdadera
# not: devuelve True si la expresión es falsa, y False si la expresión es verdadera
# Ejemplo de operadores lógicos
a = True
b = False
c=  True
resultado_and = a and b # False
resultado_or = a or b # True   
resultado_not = not a # False
print("El resultado de la operación AND es: " + str(resultado_and))
print("El resultado de la operación OR es: " + str(resultado_or))
print("El resultado de la operación NOT es: " + str(resultado_not))

# ================================
# 6. SALIDAS Y ENTRADA DE DATOS
# ================================
print("Hola mundo")
print(f"Hola {nombre}, tienes {edad} años")
nombre = input("Digite su nombre: ")
edad = input("Digite su edad: ")
# Convertir la edad a entero
edad = int(edad)
print(f"Hola {nombre}, tienes {edad} años")

# ================================
# 7. FUNCIONES INTEGRADAS
# ================================
# abs(), round(), len(), type(), str(), int(), float(), bool(), list(), dict(), set(), tuple(), sum(), min(), max(),bin(), oct(), hex(), chr(), ord(), enumerate(), zip(), map(), filter(), reduce()
n = hex(10)
print(f"El numero hexadecinal es: ",{n}) 
s=len("Borja")
print(s)

# ================================
# 8. ELEMENTOS BASICOS DE PYTHON
# ================================
# 8.1 Ecribir la siguiente expresion en forma de expresion algoritmica
# a^3*(b^2-2ac )/2b
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el valor de c: "))
resultado = (a ** 3) * ((b ** 2) - (2 * a * c)) / (2 * b)
print(f"El resultado es: {resultado}")

#8.2 Determinar la solucion logica de la siguiente expresion: 
#((3+5*8)<3and ((-6)/3*4)+2<2))or(a>b)
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
resultado = ((3 + 5 * 8) < 3 and ((-6) / 3 * 4) + 2 < 2) or (a > b)
print(f"El resultado es: {resultado}")  
#8.3 Hacer un programa para intercambiar el valor de dos variables
a = input("Digite el valor de a: ")
b = input("Digite el valor de b: ")
a, b = b, a
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
#8.4 Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia
# area = pi * r^2
# longitud = 2 * pi * r
import math
radio = float(input("Digite el radio del circulo: "))

area = math.pi * radio ** 2
longitud =2*math.pi* radio 
print(f"El area del circulo es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")
#8.5
''''Una tienda ofrece un descuento del 15% sobre el total de la compra 
y un cliente desea saber cuántod deberá pagar finalmente por su compra.
'''
print("Bienvenido a la tienda")
total_compra = float(input("Digite el total de la compra: "))
descuento = total_compra * 0.15
total_final = total_compra - descuento
print(f"El total final a pagar es: {total_final:.2f}")


# ================================     
# 9. ESTRUCTURAS DE CONTROL (condicionales)
# ================================
# if, elif, else

print("Ejercicio de condicionales")
numero = int(input("Digite un numero: "))
if numero >0:
    print("El numero es positivo")
elif numero == 0: #Caso contrario si: 
    print("El numero es cero")
else: #Caso contrario
    print("El numero es negativo")

#9.1 Hacer un programa que pida dos numeros y se de cuenta cual es par o si ambos lo son:

print("9.1 Hacer un programa que pida dos numeros y se de cuenta cual es par o si ambos lo son:")
numero1 = int(input("Digite el primer numero: "))  
numero2 = int(input("Digite el segundo numero: "))
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos numeros son pares")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print("El primer numero es par y el segundo es impar")
elif numero1 %2 != 0 and numero2 % 2 == 0:
    print("El primer numero es impar y el segundo es par")
else:
    print("Ambos numeros son impares")
    
#9.2 hacer un programa que pida 3 nuemros y determine cual es el mayor de los tres:
print("9.2 hacer un programa que pida 3 nuemros y determine cual es el mayor de los tres:")
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))
numero3 = int(input("Digite el tercer numero: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"El numero mayor es: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero mayor es: {numero2}")
elif numero3 > numero1 and numero3 > numero2:
    print(f"El numero mayor es: {numero3}")
else:
    print("Los numeros son iguales")

#9.3 Haz un programa que pida un caracter e indique si es una vocal o no
print("9.3 Haz un programa que pida un caracter e indique si es una vocal o no")

letra = input("digite una letra: ").lower()# Tranforma a minuscula, python es sensitive jeje (uper()a mayuscula)
if letra == "a" or letra == "e" or letra =="i" or letra == "o" or letra == "u":
    print("Es una vocal")
else:
    print("no es una vocal")

#9.4 
'''COnstruir un programa que simule el funcionamiento de uan calculadora que se puede realiazar las 4 opreraciones aritmeticas basicas.'
'El usuario dee especificar la opreacion con el primer caracter de la operacion
S, s = suma
R, r = resta 
P, p, M, m =  multiplicacion
D, d = division '''
print("9.4 COnstruir un programa que simule el funcionamiento de uan calculadora que se puede realiazar las 4 opreraciones")
numero1 = float(input( " Ingrese el primer digito: "))
numero2 = float(input( " Ingrese el segundo  digito: "))
Operacion = input("Escoja una letra para la operacion: ").upper()

if Operacion =="S":
    suma = numero1+numero2
    print(f"\nLa suma es {suma}")
elif Operacion == "R":
    resta = numero1+numero2
    print(f"\nLa resta es {resta}")
elif Operacion == "P" or Operacion== "M":
    multiplicacion = numero1*numero2
    print(f"\nLa mltiplicacion es: {multiplicacion}")
elif Operacion == "D":
    division = numero1/numero2
    print(f"\nLa division es {division:.2f}")
else:
    print(f"\nNo es una operación que esta definida")
#9.5 
'''Hacer un programa que simule un cajero automatico sinb un saldo incial de $1000 y tendra 
el siguiente menu de opciones:
1. Ingresar dinero a la cuenta 
2. Retirar dinero de la cuenta
3. Mostrar disponible
4. Salir
'''
print(f"Ejercicio 9.5 cajero")
saldo =1000
print("\t.:Menú:.") #\t= tabulación
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar disponible")
print("4. Salir")
opcion = int(input("Digite una opción del menú: "))

print()

if  opcion==1:
    extra = float(input("cuanto dinero desea ingresar a la cuenta: "))
    saldo += extra
    print(f"EL monto en su cuenta es {saldo}")
elif opcion==2:
    retirar = float(input("cuanto dinero desea retirar a la cuenta: "))
    if retirar>saldo:
        print("No tiene monto suficiente para retirar")
    else:
        saldo-= retirar
        print(f"El monto en su suenta es {saldo}")
elif opcion ==3:
    print(f"El monto en su suenta es {saldo}")
elif opcion == 4:
    print("Gracias por utilizar el cajero automatico ")
else:
    print("Se equivocó de menú")


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


# ================================
# 12. DICCIONARIOS
# ================================
# diccionario = {"nombre": "Henry", "edad": 25, "ciudad": "Lima"}



# ================================
# 13. FUNCIONES
# ================================
# def nombre_funcion(parametros):
#     return valor
# ================================






# ================================
# 14. CICLOS
# ================================
# while, for










# ================================
# 16. IMPORTAR MÓDULOS
# ================================
# import modulo
# ================================
# 17. MANEJO DE EXCEPCIONES
# ================================
# try:
#     print(x)
# except NameError:
#     print("La variable x no está definida")
# except:
#     print("Algo salió mal")
# finally:
#     print("El bloque try...except ha finalizado")
# ================================
# 18. CLASES Y OBJETOS
# ================================
# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#
#     def saludar(self):        
#         print("Hola, mi nombre es " + self.nombre)
# ================================
# 19. HERENCIA
# ================================
# class Estudiante(Persona):   
#     def __init__(self, nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.grado = grado
#
#     def saludar(self):    
#         print("Hola, mi nombre es " + self.nombre + " y soy estudiante de " + self.grado)
# ================================  
# 20. MÓDULOS
# ================================
# import modulo

# ================================
# 21. MANEJO DE ARCHIVOS
# ================================
# archivo = open("archivo.txt", "r")
# print(archivo.read())
# archivo.close()

# ================================
# 22. MANEJO DE CADENAS
# ================================
# cadena = "Hola, soy Henry"
# print(cadena[0])
# print(cadena[0:4])
# print(cadena.upper())
# print(cadena.lower())
# print(cadena.strip())
# print(cadena.replace("H", "J"))
# print(cadena.split(","))
# ================================
# 23. FORMATO DE CADENAS
# ================================
# nombre = "Henry"
# edad = 25
# print("Hola, mi nombre es {} y tengo {} años".format(nombre, edad))
# ================================
# 24. ENTRADA DE DATOS
# ================================
# nombre = input("Por favor, ingresa tu nombre: ")
# print("Hola, " + nombre)
# ================================
