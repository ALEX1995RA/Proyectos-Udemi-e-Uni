lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']
print(lenguajes)
#los Arrays o list enpienzan en Cero
print(lenguajes[0])

lenguajes.sort()
print(lenguajes)

aprendiendo = f'Estoy aprendiendo { lenguajes[3] }'
print(aprendiendo)

#modificando valores de un Array o list
lenguajes[2] ='PHP'
print(lenguajes)

#Agregar elementos a un Arreglo
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar un producto de un array o list
del lenguajes[1]
print(lenguajes)

#eliminar un Array o list
lenguajes.pop()  #elima el ultimo elemento
print(lenguajes)

# eliminar con pop
lenguajes.pop(0)
print(lenguajes)
#eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)