import pywhatkit as kit

def importMensaje():
    mensaje = input('Ingrese el mensaje a enviar: ')
    return mensaje

def EnviarConFoto(data,mensaje,rutaImagen):
    for i in range(len(data)):
        nombre = data['NOMBRES'][i]
        celular = data['CELULAR'][i]
        """ try:
            kit.sendwhats_image("+57"+str(celular),rutaImagen,f'Cordial saludo estimado {nombre}, {mensaje}',16,True,4)
            print(f'envio exitoso a {nombre}')
        except:
            print(f'Se presento un erro al enviar a {nombre}') """
        kit.sendwhats_image("+57"+str(celular),rutaImagen,f'Cordial saludo estimado {nombre}, {mensaje}',16,True,4)    


def sendWhatsappSimple (data,mensaje):
    
    for i in range(len(data)):
        nombre = data['NOMBRES'][i]
        
        celular = data['CELULAR'][i]
        
        try:
            kit.sendwhatmsg_instantly("+57"+str(celular),f'Cordial saludo estimado {nombre}, {mensaje}',15,4)
            

            print(f'envio exitoso a {nombre}')
        except:
            print(f'Se presento un erro al enviar a {nombre}')
    
 
 


