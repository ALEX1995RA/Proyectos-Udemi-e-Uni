#operadores And y Or
usuario_logueado = True
usuario_admi = False
if usuario_logueado and usuario_admi:
    print('Administrador')
elif usuario_logueado:
    print('Acseso al sistema')
else:
    print('debes iniciar sesión')