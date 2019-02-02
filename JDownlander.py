#Con la librería TKiter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from pafy import *
raiz=Tk()#Creamos la raíz
raiz.title("JohDownloader")
raiz.resizable(0,0)
raiz.iconbitmap(r'D:\archivos de Johan\programa para descargar videos\img\Iconov1.ico')
raiz.geometry("800x650")
raiz.config(bg="white")
URL = ""
#-----------Función para seguir el evento--------------
def Enlace():
    if enlaceu.get()=="":
        print("No hay nada")
        messagebox.showwarning("Error","No ha ingresado nada")
    #elif enlaceu.get() != "https://www.youtube.com":
        #messagebox.showwarning("Error", "El enlace es inválido")
    else:
        URL = Label(raiz,text="Probando URL "+ enlaceu.get())
        URL.place(x=30,y=100)
        #--------------Creamos el título del vídeo---------------
        titulov2 = Frame(raiz)
        titulov2.place(x=290, y=190)
        titulov2.config(bg="white",width=440,height=32,bd=2,relief="solid")
        video = pafy.new(enlaceu.get())
        titulov = Label(titulov2,text=video.title,font=("Century"),bg="white")
        titulov.pack()
        #------------Descripcion del video-----------------------
        comm = Frame(raiz)
        comm.place(x=290, y=230)
        comm.config(bg="white",width=440,height=230,bd=2,relief="solid")
        comm2 = Label(comm,text=video.description,font=("Century"),bg="white")
        comm2.pack(side="left",anchor="n")
        #-----------Likes y Dislikes del video-------------------
        #likem = Frame(raiz)
        #likem.place(x=100,y=50)
        #like = Label.(bg=white)
#-------------Funcion para cambiar el background-----------------
def cambiarbg():
    ventana = tk.Toplevel()
    ventana.title("Colores de fondo")
    ventana.geometry("300x200")
    cverde = Button(ventana,bg="green")
    cverde.grid(row= 0,column=0,padx=2,pady=2,width="3")
    crojo = Button(ventana, bg="red")
    crojo.grid(row=0, column=1,padx=2,pady=2)
#-------------------Navegación-------------------------
enlaceu = StringVar()
browse=Entry(raiz,bg="white",width="50",bd=2,font=("Century"),textvariable=enlaceu)#Creo la variable browse, le asigno un Frame.
browse.place(x=188,y=50)
browse.config(relief="solid")
Label(raiz,text="¡Descarga tús vídeos de youtube con seguridad!",
                   font=("Comic Sans MS",10),bg="white",fg="blue",justify="center").place(x="200",y="10")
Label(raiz,text="URL:",font=("Comic Sans MS",10),bg="white").place(x=140,y=50)
#Creamos el botón para enviar a la descarga
botonprincipal = Button(raiz,text="OK",bg="white",cursor="hand2",command=Enlace)
botonprincipal.place(x=650,y=45)
botonprincipal.config(relief="solid",bd=2)
#----------------------BOTON DE COLOR (Para backgrounds)-------------------------------
cblanco = Button(raiz,bg="white",width="3",cursor="hand2",command=cambiarbg,relief="solid",bd=1)
cblanco.place(x=768,y=0)



raiz.mainloop()
