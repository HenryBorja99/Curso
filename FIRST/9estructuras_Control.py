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
