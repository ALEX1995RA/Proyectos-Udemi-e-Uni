def app():
    archivo = open('archivo.txt', 'w')  
    for i in range(0,20):
       archivo.write('Esta es la Linea ' + str (i) + "\r\n" )
    archivo.close()
       

app()