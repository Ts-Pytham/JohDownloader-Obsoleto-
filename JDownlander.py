#Con la librería TKiter
from tkinter import *
from tkinter import ttk
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
    enlacecorrecto = False
    if enlaceu.get()=="":
        return messagebox.showwarning("Error","¡No ha ingresado nada!")
    for i in enlaceu.get():
        if (i == "."):
            enlacecorrecto = True
    if enlacecorrecto == False:
        messagebox.showwarning("Error", "El enlace es inválido")
    else:
        try:
            #URL = Label(raiz,text="Probando URL "+ enlaceu.get())
            #URL.place(x=30,y=100)
            #--------------Creamos el título del vídeo---------------
            global video
            video = pafy.new(enlaceu.get())
            global titulov
            titulov2 = Frame(raiz)
            titulov2.place(x=290, y=190)
            titulov2.config(bg="white",width=440,height=32,bd=2,relief="solid")
            titulov = Label(titulov2,text=video.title,font=("Century"),bg="white")
            titulov.pack()
            #------------Descripcion del video-----------------------
            # creamos la barra de scroll
            barra = Scrollbar(raiz)
            global c
            #Creamos el cavas (Dibujo para que podamos usar el label)
            c = Canvas(raiz, bg="white", relief="solid", bd=2, yscrollcommand=barra.set,height=300,width=340)
            barra.config(command=c.yview)
            barra.place(x=660, y=230, height=306)
            #El frame nos servirá para unir el canvas y comm2
            global elframe
            elframe = Frame(c)
            c.place(x=290, y=230)
            c.create_window(0,0, window=elframe)
            global comm2
            comm2 = Label(elframe, wraplength=330,justify="left", font=("Century"),text=video.description,bg="white")
            comm2.pack()
            raiz.update()
            c.config(scrollregion=c.bbox("all"))
            #-----------Likes y Dislikes del video-------------------
            likem = Frame(raiz)
            likem.place(x=0,y=506)
            likem.config(bg="white",width=30,height=30,bd=2,relief="solid")
            global like
            like = Label(likem, bg="white", text=f"Likes: {video.likes}", font=("Century"))
            like.grid(row=0, column=1)
            dislike = Frame(raiz)
            dislike.place(x=120, y=506)
            dislike.config(bg="white", width=30, height=30, bd=2, relief="solid")
            global dislikee
            dislikee = Label(dislike, bg="white", text=f"Dislikes: {video.dislikes}", font=("Century"))
            dislikee.grid(row=0, column=2)
            #----------------Botón de descarga----------------------
            download = Button(raiz,text="Descargar",font=("Century"),bg="#1DB30A",fg="black",relief="solid",bd=1,height=2,width=10,command=dialogdescarga)
            download.place(x=0,y=560)
        except ValueError:
            messagebox.showwarning("Error", "¡No se encontró la URL!, intente de nuevo")
        except:#Si manda error por el título
            messagebox.showwarning("Error", "¡Hubo un error en el título!")
            video = pafy.new(enlaceu.get())
            titulov2 = Frame(raiz)
            titulov2.place(x=290, y=190)
            titulov2.config(bg="white", width=440, height=32, bd=2, relief="solid")
            titulov = Label(titulov2, text="Hubo un error en el título.", font=("Century"), bg="white")
            titulov.pack()
            barra = Scrollbar(raiz)
            c = Canvas(raiz, bg="white", relief="solid", bd=2, yscrollcommand=barra.set, height=300, width=340)
            barra.config(command=c.yview)
            barra.place(x=660, y=230, height=306)
            elframe = Frame(c)
            c.place(x=290, y=230)
            c.create_window(0, 0, window=elframe, anchor='nw')
            comm2 = Label(elframe, wraplength=330, justify="left", font=("Century"), text=video.description, bg="white")
            comm2.pack()
            raiz.update()
            c.config(scrollregion=c.bbox("all"))
            likem = Frame(raiz)
            likem.place(x=0, y=400)
            likem.config(bg="white", width=30, height=30, bd=2, relief="solid")
            like = Label(likem, bg="white", text=f"Likes: {video.likes}", font=("Century"))
            like.grid(row=0, column=1)
            dislike = Frame(raiz)
            dislike.place(x=120, y=400)
            dislike.config(bg="white", width=30, height=30, bd=2, relief="solid")
            dislikee = Label(dislike, bg="white", text=f"Dislikes: {video.dislikes}", font=("Century"))
            dislikee.grid(row=0, column=2)

#-------------Funcion para crear la segunda pantalla-----------------
def segundapantalla():
    ventana = Toplevel()
    ventana.resizable(0, 0)
    ventana.title("Colores de fondo")
    ventana.geometry("300x200")
    Label(ventana,text="Hex: ",font=("Comic Sans MS",10)).place(x=60,y=0)
    chex = Entry(ventana,font=("Comic Sans MS",10),bd=2,width=10,textvariable=code)
    chex.place(x=100,y=0)
    botonsec = Button(ventana, text="OK", cursor="hand2", command=cambiarbg)
    botonsec.place(x=210,y=0)
    global colorselec
    colorselec = Label(ventana,bg="white",width=3,relief="solid",bd=2)
    colorselec.place(x=270,y=1)
    #Creamos los botones
    cverde = Button(ventana,bg="green",width=1,command=ColorVerde)
    cverde.place(x=0,y=40)
    crojo = Button(ventana, bg="red",width=1,command=ColorRojo)
    crojo.place(x=20,y=40)
    cyellow = Button(ventana,bg="yellow",width=1,command=ColorAmarillo)
    cyellow.place(x=40,y=40)
def ColorVerde():
    raiz.config(bg="green")
    msg.config(bg="green")
    msg1.config(bg="green")
    cblanco.config(bg="green")
    botonprincipal.config(bg="green")
    browse.config(bg="green")
    colorselec.config(bg="green")
    titulov.config(bg="green")
    comm2.config(bg="green")
    c.config(bg="green")
    elframe.config(bg="green")
    like.config(bg="green")
    dislikee.config(bg="green")
def ColorRojo():
    raiz.config(bg="red")
    msg.config(bg="red")
    msg1.config(bg="red")
    cblanco.config(bg="red")
    botonprincipal.config(bg="red")
    browse.config(bg="red")
    colorselec.config(bg="red")
    titulov.config(bg="red")
    comm2.config(bg="red")
    c.config(bg="red")
    elframe.config(bg="red")
    like.config(bg="red")
    dislikee.config(bg="red")

def ColorAmarillo():
    raiz.config(bg="yellow")
    msg.config(bg="yellow")
    msg1.config(bg="yellow")
    cblanco.config(bg="yellow")
    botonprincipal.config(bg="yellow")
    browse.config(bg="yellow")
    colorselec.config(bg="yellow")
    titulov.config(bg="yellow")
    comm2.config(bg="yellow")
    c.config(bg="yellow")
    elframe.config(bg="yellow")
    like.config(bg="yellow")
    dislikee.config(bg="yellow")
#------------------Cambiamos el background mediante código hex---------------
def cambiarbg():
    try:
        if code.get() == "#000000":
            raiz.config(bg="black")
            msg.config(bg="black")
            msg1.config(bg="black",fg="white")
            cblanco.config(bg="#373737")
            botonprincipal.config(bg="white")
            browse.config(bg="white")
            colorselec.config(bg=code.get())
            titulov.config(bg="white")
            comm2.config(bg="white")
            c.config(bg="white")
            elframe.config(bg="white")
            like.config(bg="white")
            dislikee.config("white")
            print("entró al if")
        elif code.get() == "":
            messagebox.showwarning("Error","¡No hay nada!")
        else:
            raiz.config(bg=code.get())
            msg.config(bg=code.get())
            msg1.config(bg=code.get())
            cblanco.config(bg=code.get())
            botonprincipal.config(bg=code.get())
            browse.config(bg=code.get())
            colorselec.config(bg=code.get())
            titulov.config(bg=code.get())
            comm2.config(bg=code.get())
            c.config(bg=code.get())
            elframe.config(bg=code.get())
            like.config(bg=code.get())
            dislikee.config(bg=code.get())
            print(f"el bg es: {code.get()}")
    except:
        print(code.get())
        return messagebox.showwarning("Error","¡El code no existe o no funciona, pruebe otro!")

 # ----------------Salir de la api-descarga-------------
def salir():
    ventanad.destroy()
#----------------------Descargar-------------------
def descargar():
    if calidad.get() == "" and formato.get() == "":
        return messagebox.showwarning("Error","¡No has elegido una opción!")
    elif destino.get() == "":
        return messagebox.showwarning("Error","¡No has puesto nada en el destino!")
    else:
        archivo = video.getbest()
        archivo.download()
#-------------------Ventana de descarga-----------------
def dialogdescarga():
    global ventanad
    ventanad = Toplevel()
    ventanad.resizable(0,0)
    ventanad.title("Descarga")
    ventanad.geometry("600x400")
    ventanad.config(bg="white")
    #--------Creamos el label y el combobox de formato------
    Label(ventanad,text="Formato:",font=("Comic Sans MS",9),bg="white").place(x=0,y=40)
    global formato
    formato = ttk.Combobox(ventanad,state="readonly",width=40)
    formato["values"] = ["MP4"]
    formato.place(x=70,y=40)
    # --------Creamos el label y el combobox de calidad-----
    Label(ventanad,text="Calidad:",font=("Comic Sans MS",9),bg="white").place(x=0,y=100)
    global calidad
    calidad = ttk.Combobox(ventanad,state="readonly",width=40)
    calidad["values"] = ["HD (1280x720)"]
    calidad.place(x=70,y=100)
    # --------Creamos el label y el combobox de destino-----
    Label(ventanad,text="Destino:",font=("Comic Sans MS",9),bg="white").place(x=0,y=160)
    global destino
    destino = ttk.Combobox(ventanad,width=40)
    destino["values"] = ["JohDownloader\Videos"]
    filepath="programa para descargar videos\Videos"
    destino.place(x=70,y=160)
    # --------Creamos los botones de aceptar y rechazar-----
    aceptar = Button(ventanad,text="Aceptar",bg="white",font=("Comic Sans MS",9),width=10,command=descargar)
    aceptar.place(x=0,y=220)
    rech = Button(ventanad,text="Rechazar",bg="white",font=("Comic Sans MS",9),width=10,command=salir)
    rech.place(x=120,y=220)
#-------------------Navegación-------------------------
code = StringVar()
enlaceu = StringVar()
browse=Entry(raiz,bg="white",width=50,bd=2,font=("Century"),textvariable=enlaceu)#Creo la variable browse, le asigno un Frame.
browse.place(x=188,y=50)
browse.config(relief="solid")
msg = Label(raiz,text="¡Descarga tús vídeos de youtube con seguridad!",
                   font=("Comic Sans MS",10),bg="white",fg="blue",justify="center")
msg.place(x="200",y="10")
msg1 = Label(raiz,text="URL:",font=("Comic Sans MS",10),bg="white")
msg1.place(x=140,y=50)
#Creamos el botón para enviar a la descarga
botonprincipal = Button(raiz,text="OK",bg="white",cursor="hand2",command=Enlace)
botonprincipal.place(x=650,y=45)
botonprincipal.config(relief="solid",bd=2)
#----------------------BOTON DE COLOR (Para backgrounds)-------------------------------
cblanco = Button(raiz,bg="white",width="3",cursor="hand2",command=segundapantalla,relief="solid",bd=2)
cblanco.place(x=768,y=0)
raiz.mainloop()
