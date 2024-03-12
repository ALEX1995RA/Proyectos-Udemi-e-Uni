class Restaurant:

    def Agregar_restaurant(self, Nombre):
        self.Nombre = Nombre
    def mostrar_informacion(self):
        print(f'Nombre:{self.Nombre}')

        print('Agregando...')
restaurant = Restaurant()
restaurant.Agregar_restaurant('pizzeria Mexico')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.Agregar_restaurant('Hamburgusas Python')
restaurant2.mostrar_informacion()

print(f'Nombre Restaurant:{restaurant.Nombre}')
print(f'Nombre Restaurant:{restaurant2.Nombre}')