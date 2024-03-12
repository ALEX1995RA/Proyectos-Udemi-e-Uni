# Geneara el Id Unico
print('*** Sistema de Generador de Email ***')
nombre = input('Cual es tu Nombre?:')
nombre = nombre.lower()
apellido = input('Cual es tu Apellido?:')
apellido = apellido.lower()
# generacion de correo electronico
email_generado = f'{nombre}.{apellido}@cartucho.es'
print(f'''\n Hola {nombre}, Habitnate del cartucho!
    Tu nuevo email generado por mi, el mejor sistema es:
    {email_generado}
    Alegrate y felicitaciones Marihuano!''')