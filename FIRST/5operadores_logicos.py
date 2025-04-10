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