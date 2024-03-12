# formatos de cadenas
var_hola = 'Hola'
var_mundo = 'Mundo'
print(var_hola, var_mundo)
# concatenacion de cadenas o unificacionde varias cadenas
var_hola_mundo = var_hola + var_mundo
print(var_hola_mundo)
# interpolacion de cadenas
var_hola_mundo = f'Mi cadena: {var_hola} {var_mundo}'
print(var_hola_mundo)
# interpolacion de multilineas
print(f'''Mi cadena:
    {var_hola} 
        {var_mundo}''')