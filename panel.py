from customtkinter import *

from PIL import Image

import threading

from Modulos import (
    Configuracion,
    Enviar_Webhook,
    Entrar_Discord,

    )



config = Configuracion()

class Panel_Tkinter(CTk):
    def __init__(self):
        super().__init__()

        self.foto = Image.open(config.Ruta_logo)
        self.iconbitmap(config.Icono_app)
        self.title("Panel_Prueba")
        self.geometry(f"{config.Ancho_Panel}x{config.Largo_Panel}+{config.X_Panel}+{config.Y_Panel}")

        if not config.resizable:
            self.resizable(False,False)

        if config.resizable:
            self.resizable(True,True)

        self.pack_propagate(False)


        self.imagen_foto = CTkImage(light_image= self.foto, dark_image= self.foto, size = (50,50))
        self.Fondo = CTkLabel(self,image=self.imagen_foto, text = "")
        self.Fondo.pack()

        self.Text_Webhook = CTkLabel(self, text = config.Texto_Webhook_Label )
        self.Text_Webhook.place(x = 30, y = 100)

        self.webhook = CTkEntry(self, placeholder_text= config.Texto_Placeholde_webhook, width= 170)
        self.webhook.place(x = 95, y = 100)

        self.Label_Entry_Mensaje = CTkLabel(self, text = config.Label_Entry_Mensaje)
        self.Label_Entry_Mensaje.place(x  = 30, y = 150)

        self.Entry_mensaje = CTkEntry(self, placeholder_text= config.Entry_mensaje_placeholde, width= 170)
        self.Entry_mensaje.place(x = 95, y = 150)

        dc_icon = Image.open(config.logo_discord)
        dc_icon = CTkImage(light_image= dc_icon, dark_image= dc_icon, size = (70,70))

        self.Discord = CTkButton(self, image= dc_icon, text = "", command = lambda: threading.Thread(target=Entrar_Discord,daemon= True).start(), fg_color= "transparent",hover_color=self.cget("fg_color"), width=10, height= 10)
        self.Discord.place(x = 2, y = 230)

        self.Image_Boton = Image.open(config.ruta_imagen_boton)

        self.Imagen_Boton = CTkImage(light_image= self.Image_Boton, dark_image= self.Image_Boton, size=(30,30))

        self.Boton_enviar = CTkButton(self, image = self.Imagen_Boton, text = config.Text_Boton_Enviar, command= lambda: threading.Thread(target=Enviar_Webhook, args =(self.webhook,self.Entry_mensaje,),daemon=True, ).start(), width= 170 )

        self.Boton_enviar.place(x = 90, y = 200)





if __name__ == "__main__":

    ventana = Panel_Tkinter()
    ventana.mainloop()