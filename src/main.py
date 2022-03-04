import scripts.contro_cvc as a
import scripts.send_whatsapp as t

#definir ruta para cada equipo
ruta = "../doc/contacto.xlsx"

def run():
    print('enviar whatsapp de forma masiva')

    #ingresar la ruta del archivo
    print( "1- mesaje simple\n2-mensaje con imagen \n 3-Salir")
    valor = int(input('Ingrese valor :'))
    data = a.dataFrame(ruta)
    if (valor ==1):
        mensaje =t.importMensaje()
        t.sendWhatsappSimple(data,mensaje)
    elif(valor ==2):
        mensaje = t.importMensaje()
        imagen = input('Ingrese ruta de imagen:')
        t.EnviarConFoto(data,mensaje,imagen)
    else:
        print('Terminar')

if __name__=='__main__': 
    
    run()

