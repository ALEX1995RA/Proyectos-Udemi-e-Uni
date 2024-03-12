nombre = input('Cual es tu nombre: \r\n')
print(f'Hola {nombre}')

edad = input('Cual es tu edad?: \r\n')
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aun no puedes votar')

numero = input('Agrega un numero y te dire si es par o non: \r\n')
numero = int(numero)
if numero % 2 == 0: 
    print(f'El numero {numero} es Par')
else:
    print(f'El numero {numero} es impar')


    