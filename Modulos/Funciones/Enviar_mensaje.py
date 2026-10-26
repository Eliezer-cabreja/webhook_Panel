import requests
from tkinter import messagebox
from Modulos import Configuracion
from playsound3 import playsound

def Enviar_Webhook(webhook,mensaje):


    URL = webhook.get()
    mensaje_enviar = mensaje.get()
    try:
        
        requests.post(URL, json=({"content":mensaje_enviar}), timeout= 5)

        messagebox.showinfo("success", "Mensaje Enviado")
        
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"No se pudo enviar en mensaje: {e}")