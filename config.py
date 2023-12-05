import datetime
#constantes para el tema oscuro
COLOR_FONDO_PRIMARIO = '#5E0819'
COLOR_FONDO_SECUNDARIRIO = '#8A349C'
TITULO_APP = 'APP DE Nadine'
date = datetime.datetime.now()
HORA_ACTUAL = f"{date.day}-{date.month}-{date.year} Hora: {date.hour}:{date.minute}"
COLOR_BOTON = '#EC8ECD'
#FUNCION QUE NOS PERMITE CENTRAR NUESTRA PANTALLA
def centrar_ventana(objeto, ancho_ventana, largo_ventana):
    pantalla_ancho = objeto.winfo_screenwidth()
    pantalla_largo = objeto.winfo_screenheight()
    x = int((pantalla_ancho/2)-(ancho_ventana/2))
    y = int((pantalla_largo/2)-(largo_ventana/2))
    return objeto.geometry(f'{ancho_ventana}x{largo_ventana}+{x}+{y}')
    