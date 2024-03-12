mes = int(input('Proporciona el mes del año (1 - 12) '))
estacion = None
if mes == 12 or mes == 1 or mes == 2:
    estacion = 'invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'para el mes {mes} la estacion es: {estacion} ')
# Ejercisio de edad
edad = int(input('Proporciona tu edad: '))
mensaje: None
if edad >= 0 and edad < 10:
    mensaje = 'la infancia es increible'
elif edad >= 10 and edad< 20:
    mensaje = 'Muchos cambios mucho estudio'
elif edad >= 21 and edad < 30:
    mensaje = 'Amor y comienza el trabajo'
else:
    mensaje = 'Etapa de vida no reconocida'
print(f'tu edad es {edad}, {mensaje}')
# Crear un sistema de calificaciones
calificacion = int(input('Proporciona un valor de 0 a 10: '))
mensaje = None
if calificacion >= 9 and calificacion <= 10:
    mensaje = 'A'
elif calificacion <= 9 and calificacion < 8:
    mensaje = 'B'
elif calificacion <= 8 and calificacion < 7:
    mensaje = 'C'
elif calificacion <= 7 and calificacion < 6:
    mensaje = 'D'
elif calificacion <= 6 and calificacion < 0:
    mensaje = 'F'
else:
    mensaje = 'Valor incorrecto'
print(f' la calificion es {calificacion}, {mensaje}')