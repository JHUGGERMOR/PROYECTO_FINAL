from tkinter import *
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
import pygame



def seleccionar_opcion(opcion):
    if opcion == "INVITADO":
        abrir_ventana1()
    elif opcion == "ACCEDER":
        abrir_ventana2()

def abrir_ventana1():
    global ventana_invitado
    ventana_invitado = Toplevel(root)
    ventana_invitado.geometry("500x500")
    ventana_invitado.title("MODO INVITADO")
    Button(ventana_invitado, text="Volver al Inicio", width=20, command=lambda: volver_inicio(ventana_invitado)).place(x=10, y=20)
    root.iconify()

def abrir_ventana2():
    ventana_acceso = Toplevel(root)
    ventana_acceso.geometry("500x500")
    ventana_acceso.title("MODO LOGIN")
    Button(ventana_acceso, text="Volver al Inicio", width=20, command=lambda: volver_inicio(ventana_acceso)).place(x=10, y=20)
    root.iconify()

def volver_inicio(ventana):
    root.deiconify()
    ventana.destroy()
    

    
    

def toggle_reproducir_pausar():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def ajustar_fondo(event):
    # Redimensionar la imagen de fondo cuando la ventana se redimensiona
    nueva_dimension = (root.winfo_width(), root.winfo_height())
    imagen_redimensionada = imagen_pil.resize(nueva_dimension, Image.LANCZOS)
    nueva_imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    fondo_label.configure(image=nueva_imagen_tk)
    fondo_label.image = nueva_imagen_tk  # Actualizar la referencia para evitar que la imagen sea eliminada por el recolector de basura


# Inicializar pygame mixer para la reproducción de música
pygame.mixer.init()

# Cargar la canción (reemplaza con la ruta correcta de tu archivo de música)
pygame.mixer.music.load("PROYECTO FINAL/RECURSOS/sonidosincopy.mp3")
pygame.mixer.music.play(loops=-1)  # '-1' para reproducir infinitamente

root = Tk()
root.title("PROYECTO EMULADOR V1.0")

root.geometry("850x600")
root.resizable(0, 0)

# Abrir la imagen y redimensionarla para que se ajuste a las dimensiones de la ventana
imagen_pil = Image.open("PROYECTO FINAL/RECURSOS/FONDO.jpg")
imagen_redimensionada = imagen_pil.resize((850, 600), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un widget de etiqueta para mostrar la imagen de fondo
fondo_label = Label(root, image=imagen_tk)
fondo_label.place(relwidth=1, relheight=1)

# Configurar el evento de redimensionamiento de la ventana
root.bind("<Configure>", ajustar_fondo)

# Crear las opciones de botones
btn_invitado = Button(root, text="INVITADO", bg="#A80000", fg="#11A5D9", font=("Bauhaus 93", 30), command=lambda: seleccionar_opcion("INVITADO"), relief="solid")
btn_invitado.place(x=120, y=420)

btn_acceder = Button(root, text="ACCEDER", bg="#000770", fg="#11A5D9", font=("Bauhaus 93", 30), command=lambda: seleccionar_opcion("ACCEDER"), relief="solid")
btn_acceder.place(x=530, y=420)

# Cargar la imagen y redimensionarla
imagen_reproducir_pausar = PhotoImage(file="PROYECTO FINAL/RECURSOS/mute.png")
imagen_reproducir_pausar = imagen_reproducir_pausar.subsample(30, 30)  # Ajusta los valores de subsample según sea necesario

# Reemplazar el texto con la imagen en el botón
btn_reproducir_pausar = Button(root, image=imagen_reproducir_pausar, command=toggle_reproducir_pausar)
btn_reproducir_pausar.place(x=818, y=0)


# ETIQUETAS Y TEXTO
label1 = Label(root, text="Julian Rodrigo Perdomo Olaya", bg="black", fg="#11A5D9", font=("Arial", 10), relief="solid")
label1.place(x=20, y=20)

label2 = Label(root, text="PROYECTO FINAL PROGRAMACION 2-USCO", bg="black", fg="#11A5D9", font=("Arial", 10), relief="solid")
label2.place(x=20, y=570)

root.mainloop()
