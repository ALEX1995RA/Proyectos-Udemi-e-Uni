class Restaurant:

    def __init__(self, Nombre, Categoria, Precio):
        self.Nombre = Nombre
        self.Categoria = Categoria
        self.__Precio = Precio
    def mostrar_informacion(self):
        print(f'Nombre: {self.Nombre}, Categoria: {self.Categoria}, Precio: {self.__Precio}')

    def get_Precio(self):
        return self.__Precio
        print(self.__Precio)

    def set_precio(self, Precio):
        self.__Precio = Precio
         
restaurant = Restaurant('pizzeria Mexico', 'Comida Italiana', '50')
# print(restaurant._Precio)
# Restaurant.__Precio = 80
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_Precio()
print(precio)

restaurant2 = Restaurant('Hamburgusas Python', 'Comida Casual', '20')
# print(restaurant2._Precio)
# restaurant2.__Precio = 50
restaurant2.mostrar_informacion()
restaurant2.set_precio(850)
precio = restaurant2.get_Precio()