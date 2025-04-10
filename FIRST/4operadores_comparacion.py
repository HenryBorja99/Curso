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
a= 3
b = 5
resultado = (a + b) * (a - b) ** 2 / b % a
print("El resultado del cálculo con las reglas de precedencia es: " + str(resultado))

#6. ==, !=, <, >, <=, >=
#7 =, +=, -=, *=, /=, %=, **=
relacional = a == b
print("El resultado de la comparación es: "+str(relacional))

