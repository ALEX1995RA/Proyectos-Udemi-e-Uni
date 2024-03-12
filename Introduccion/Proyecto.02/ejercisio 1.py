alto = int(input('indica el alto del rectangulo: '))
ancho = int(input('indica el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('El area es:', area)
print('El perimetro es:', perimetro)
# ejercicio 2 ALGORITMO
a = int(input('Escribe un valor numerico: '))
if a % 2 == 0:
    print(f'El valor de a {a} es numero par')
else:
    print(f'el valor de a {a} es inpar')

edadAdulto = 18
edadPersona = int(input('proporciona tu edad: '))
if edadPersona >= edadAdulto:
    print(f'la persona con edad {edadPersona} es un adulto')
else:
    print(f'la persona con edad {edadPersona} es menor de edad:')
# ejercisio operador logico
valor = int(input('escribe el valor: '))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} esta dentro de rango ')
else:
    print(f'El valor {valor} esta fuera de rango')
vacaciones = True
diaDescanso = False
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene compromisos no va a ir')
if not (vacaciones or diaDescanso):
    print('Tiene compromisos no va a ir')
else:
    print('Puede asistir al juego')
edad = int(input('Introduce tu edad: '))
veintes = edad >= 20 and edad < 30
print(veintes)
treintas = 30 <= edad < 40
print(treintas)
if veintes or treintas:
    print('Dentro de rango (20\'s) o (30\'s')
    if veintes:
        print('Dentro de los 20\´s')
    elif treintas:
        print('Dentro de los 30\´s')
    else:
        print('fuera de rango')
else:
    print('No esta dentro del rango (20´s ni 30´s')
# if ( edad >= 20 and edad < 30) or (edad >= 30 and edad < 40)
# print('Dentro de rango (20\'s) o (30\'s')
# if (20 <= edad <30) or (30 <= edad < 40):

numero1 = int(input('Proporciona el numero 1: '))
numero2 = int(input('Proporciona el numero 2: '))
if numero1 > numero2:
    print('Si el numero 1 es mayor ')
else:
    print('Si el numero 2 es mayor' )
# Creacion de libros
print('proporcione los datos del libro:')
nombre = input('Proporciona el nombre:')
id = int(input('Prporciona el Id del del libro:'))
precio = float(input('proporciona el valor del libro:'))
envioGratuito = input('Indica si el envio es gratuito (true / false): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = ('Valor in coorecto debe escribir True /False: ')
print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio {precio}
    Envio Gratuito? {envioGratuito}''')