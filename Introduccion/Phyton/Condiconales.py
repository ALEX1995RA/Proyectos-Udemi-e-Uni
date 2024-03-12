 #revisar condicional mayor
balance = 500
if balance >0:
    print('puedes pagar')  
else:
    print('No tiene saldo')

likes = 200
if likes >= 200:
    print('exelente, 200 Likes')
else:
    print('Casi llegas a los 200 ')

    #texto con if
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Exelente desición')

 #evaluar boleano
    
usuario_autenticado = True
if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

# evaluar elemento
lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']
if'PHP' in lenguajes:
    print('PHP Si exisite')
else:
    print('No no esta en la lista')

    # anidados if

usuario_autenticado = True
usuario_admin = True
if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')    
else:
    print('Debes iniciar sesión')