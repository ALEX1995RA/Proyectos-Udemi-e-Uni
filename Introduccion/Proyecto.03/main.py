# condiciones if / elseif / else / elif
condicion = True
if condicion:
    print('Condicion verdadera')
else:
    print('Condicion falsa')
if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('condicion falsa')
else:
    print('Condicion no reconocida')
# comvertir de numero a texto
numero = int(input('proporciona un valor entre 1 y 3: '))
numeroTexto = ''
if numero == 1:
    numeroTexto = 'Numero Uno'
elif numero == 2:
    numeroTexto = 'Numero Dos'
elif numero == 3:
    numeroTexto = 'Numero Tres'
else:
    numeroTexto = 'Valor fuera de Rango'
print(f"Numero Proporcionado: {numero} - {numeroTexto}")
#simplificacion de sintaxis
Condicion = False
print('condicion verdadera') if condicion else print('condicion falsa')
