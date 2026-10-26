import webbrowser
from Modulos import Configuracion
from playsound3 import playsound

def Entrar_Discord():
    playsound(Configuracion().sonido_boton)
    
    webbrowser.open(Configuracion().Link_Discord)