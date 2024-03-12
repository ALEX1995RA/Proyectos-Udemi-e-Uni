# operadores aritmeticos  suma
oprandoA = 6
operandoB = 5
suma = operandoB + oprandoA
print('El resultado es', suma)
print(f'el resultado es:{suma}')
# Resta
oprandoA = 6
operandoB = 5
resta = operandoB - oprandoA
print('El resultado es', resta)
print(f'el resultado es:{resta}')
# multiplicacion
oprandoA = 6
operandoB = 5
multiplicar = operandoB * oprandoA
print('El resultado es', multiplicar)
print(f'el resultado es:{multiplicar}')
# division
oprandoA = 6
operandoB = 5
division = operandoB / oprandoA
print('El resultado es', division)
print(f'el resultado es:{division}')
# con doble //
division2 = operandoB // oprandoA
print(f'resultado es (int):{division2}')
# modulo o residuo
modulo = operandoB % oprandoA
print(f'resultado es (modulo):{modulo}')
# exponeciales
exponente = operandoB ** oprandoA
print(f'resultado es: {exponente}')
# operadores de asignacion
mivariable = 10
mivariable = mivariable + 2
print(mivariable)
# Incremoento o reasignacion con el signo = y cualquier valor aritmetico
mivariable -= 2
print(mivariable)
mivariable *= 5
print(mivariable)
mivariable /= 2
print(mivariable)
mivariable //= 2
print(mivariable)
mivariable %= 2
print(mivariable)
# operadores de comparacion
a = 5
b = 8
resultado = a == b
print(f'resultado ==: {resultado}')
resultado = a != b
print(f'resultado de ! : {resultado}')
resultado = a >= b
print(f'revicion de mayor que: {resultado}')
# operadores logiocos and / or / not
a = True
b = True
resultado = a and b
print(resultado)
a = True
b = False
resultado = a and b
print(resultado)
a = True
b = False
resultado = a or b
print(resultado)
a = True
b = True
resultado = not a
print(resultado)