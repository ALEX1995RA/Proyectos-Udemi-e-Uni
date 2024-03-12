import os
CARPETA = 'Contactos'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, Nombre, Telefono, Categoria):
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.Categoria = Categoria
def app():
    crear_directorio()
    mostrar_menu()
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            Editar_Contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no Valida, Intente de Nuevo')
def eliminar_contacto():
     nombre = input ('Seleccione el contacto a eliminar: \r\n')
     try:
         os.remove(CARPETA + nombre + EXTENSION)
         print('\r\n Eliminado correctamente')
     except expresion as identifier:
         print('No existe contacto')
     app()     

def buscar_contacto():
    nombre = input ('Seleccione el contacto a buscar: \r\n')
    try:
      with open(CARPETA + nombre + EXTENSION) as contacto:
          print('\r\n Informacion de contacto: \r\n')
          for liena in contacto:
            print(liena.rstrip())
          print('\r\n')  
    except IOError:
        print('El archivo no existe')
        print(IOError)     
    app()      
                
def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')    


def Editar_Contacto():
    print('escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + 'nombre_anterior' + EXTENSION,'w') as archivo:
         nombre_contacto = input('Agrega el nuevo nombre: \r\n') 
         Telefono_contacto = input('Agrega el nuevo telefono: \r\n')
         Categoria_contacto = input ('Agrega la nueva categoria: \r\n')
         contacto = Contacto(nombre_contacto, Telefono_contacto, Categoria_contacto)
         archivo.write('Nombre:' + 'Contacto.Nombre' + '\r\n')
         archivo.write('Telefono:' + 'Contacto.Telefono' + '\r\n')
         archivo.write('Categoria:' + 'Contacto.Categoria' + '\r\n')
         os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION ) 
         print('\r\n Contacto editado Correctamente: \r\n')
    else:
        print('Ese contacto no existe')     
    app()   
        
def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')  
    nombre_contacto = input('Nombre del Contacto: \r\n') 
    existe = existe_contacto('nombre_anterior')
    if not existe:
        with open(CARPETA + 'nombre_contacto' + EXTENSION, 'w') as archivo:
         Telefono_contacto = input('Agrega el Telefono: \r\n')
         Categoria_contacto = input ('Categoria de Contacto: \r\n')
         nombre_contacto = Contacto('nombre_contacto', 'Telefono_contacto', 'Categoria_contacto')
         archivo.write('Nombre:' + 'Contacto.Nombre' + '\r\n')
         archivo.write('Telefono:' + 'Contacto.Telefono' + '\r\n')
         archivo.write('Categoria:' + 'Contacto.Categoria' + '\r\n')
         print('\r\n Contacto creado Correctamente: \r\n')
    else:
        print('Ese contacto ya existe')
    app()
def mostrar_menu():
    print('Selecciona Del Menu lo que desea Hacer')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
       os.makedirs(CARPETA)
def existe_contacto(nombre):
    return os.path.isfile('CARPETA' + 'nombre_contacto' + 'EXTENSION')
 
app()