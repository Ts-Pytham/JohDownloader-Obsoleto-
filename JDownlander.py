#Con la librería TKiter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pafy import *
raiz=Tk()#Creamos la raíz
raiz.title("JohDownloader")
raiz.resizable(0,0)
try:
    raiz.iconbitmap('img\Iconov1.ico')
except:
    messagebox.showerror("Error Fatal", "No se pudo cargar el ícono,Revise si tiene la carpeta 'img' y tenga el icono.")
    raiz.destroy()
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
            refresh.set(refresh.get() + 1)
            if (refresh.get() == 2):
                messagebox.showwarning("¡Error!", "¡Primero tiene que refrescar la pagina!")
                refresh.set(1)
            else:
                #--------------Creamos el título del vídeo---------------
                try:
                    global video
                    video = pafy.new(enlaceu.get())
                    global titulov
                    global titulov2
                    titulov2 = Frame(raiz)
                    titulov2.place(x=290, y=190)
                    titulov2.config(bg="white",width=440,height=32,bd=2,relief="solid")
                    titulov = Label(titulov2,text=video.title,font=("Century"),bg="white")
                    titulov.pack()
                except:
                 messagebox.showwarning("Error","El texto contiene caracteres desconocidos.")
                #------------Descripcion del video-----------------------
                # creamos la barra de scroll
                global barra
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
                global likem
                likem = Frame(raiz)
                likem.place(x=0,y=506)
                likem.config(bg="white",width=30,height=30,bd=2,relief="solid")
                global like
                like = Label(likem, bg="white", text=f"Likes: {video.likes}", font=("Century"))
                like.grid(row=0, column=1)
                global dislike
                dislike = Frame(raiz)
                dislike.place(x=120, y=506)
                dislike.config(bg="white", width=30, height=30, bd=2, relief="solid")
                global dislikee
                dislikee = Label(dislike, bg="white", text=f"Dislikes: {video.dislikes}", font=("Century"))
                dislikee.grid(row=0, column=2)
                #----------------Botón de descarga----------------------
                global download
                download = Button(raiz,text="Descargar",font=("Century"),bg="#1DB30A",fg="black",relief="solid",bd=1,height=2,width=10,command=dialogdescarga)
                download.place(x=0,y=560)
                botonrefresh = Button(raiz, bg="white",cursor="hand2", relief="solid", bd=2,width=2,command=refrescar)
                botonrefresh.place(x=690, y=45)
                if(code.get() == "#000000"):
                    comm2.config(bg="white")
                    c.config(bg="white")
                    elframe.config(bg="white")
                    like.config(bg="white")
                    dislikee.config("white")
                    titulov.config(bg="white")
                else:
                    titulov.config(bg=code.get())
                    comm2.config(bg=code.get())
                    c.config(bg=code.get())
                    elframe.config(bg=code.get())
                    like.config(bg=code.get())
                    dislikee.config(bg=code.get())
        except ValueError:
            messagebox.showwarning("Error", "¡No se encontró la URL!, intente de nuevo")
#-------------Refrescar el puto Widget Raiz--------------------------
def refrescar():
    titulov.destroy()
    titulov2.destroy()
    barra.destroy()
    c.destroy()
    elframe.destroy()
    comm2.destroy()
    like.destroy()
    likem.destroy()
    dislikee.destroy()
    dislike.destroy()
    download.destroy()
    refresh.set(0)
    print("Entró a esta mierda")
#-------------Funcion para crear la segunda pantalla-----------------
def segundapantalla():
    ventana = Toplevel()
    ventana.resizable(0, 0)
    ventana.title("Colores de fondo")
    ventana.geometry("300x200")
    ventana.iconbitmap('img\Iconov1.ico')
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
    code.set("#2DFF00")
    cambiarbg()
def ColorRojo():
    code.set("#FF0000")
    cambiarbg()
def ColorAmarillo():
    code.set("#FFFF00")
    cambiarbg()
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
            info.config("white")
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
            info.config(bg=code.get())
            print(f"el bg es: {code.get()}")
    except:
        return messagebox.showwarning("Error","¡El code no existe o no funciona, pruebe otro!")

 # ----------------Salir de la api-descarga-------------
def salir():
    ventanad.destroy()
#----------------------Descargar-------------------
def descargar():
    if calidad.get() == "" or formato.get() == "":
        messagebox.showwarning("Error","¡No has elegido una opción!")
        ventanad.destroy()
    elif destino.get() == "":
         messagebox.showwarning("Error","¡No has puesto nada en el destino!")
         ventanad.destroy()
    else:
        archivo = video.streams[0]
        archivo.download()
#-------------------Ventana de descarga-----------------
def dialogdescarga():
    global ventanad
    ventanad = Toplevel()
    ventanad.resizable(0,0)
    ventanad.title("Descarga")
    ventanad.geometry("600x400")
    ventanad.config(bg="white")
    ventanad.iconbitmap('img\Iconov1.ico')
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
    calidad["values"] = ["Máxima calidad [1280x720]"]
    calidad.place(x=70,y=100)
    # --------Creamos el label y el combobox de destino-----
    Label(ventanad,text="Destino:",font=("Comic Sans MS",9),bg="white").place(x=0,y=160)
    global destino
    destino = ttk.Combobox(ventanad,width=40,state="readonly")
    destino["values"] = ["JohDownloader\Videos"]
    destino.place(x=70,y=160)
    # --------Creamos los botones de aceptar y rechazar-----
    aceptar = Button(ventanad,text="Aceptar",bg="white",font=("Comic Sans MS",9),width=10,command=descargar)
    aceptar.place(x=0,y=220)
    rech = Button(ventanad,text="Rechazar",bg="white",font=("Comic Sans MS",9),width=10,command=salir)
    rech.place(x=120,y=220)
#------------------Ventana de información sobre mi-----
def informacion():
    infov = Toplevel()
    infov.resizable(0,0)
    infov.title("Información")
    infov.geometry("420x200")
    infov.config(bg="white")
    infov.iconbitmap('img\Iconov1.ico')
    global nombre,nombre2,nombre3
    nombre = Label(infov,bg="white",justify="center",font=("Comic Sans MS",10),text="\t        JohDownloader V1.0")
    nombre.place(x=0,y=0)
    nombre2 = Label(infov,bg="white",font=("Comic Sans MS",10),text="Creador: Johan Sánchez")
    nombre2.place(x=0,y=30)
    nombre3 = Label(infov,bg="white",justify="left",font=("Comic Sans MS",10),text="El programa no está a la venta y es de código libre,\nsi alguien lo está vendiendo, por favor contactame.")
    nombre3.place(x=0,y=60)
    nombre.config(bg=code.get())
    nombre2.config(bg=code.get())
    nombre3.config(bg=code.get())
    infov.config(bg=code.get())
#-------------------Navegación-------------------------
code = StringVar()
code.set("#FFFFFF")
enlaceu = StringVar()
refresh = IntVar(0)
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
#---------------------BOTON DE COLOR (Para backgrounds)-------------------------------
cblanco = Button(raiz,bg="white",width="3",cursor="hand2",command=segundapantalla,relief="solid",bd=2)
cblanco.place(x=768,y=0)
#--------------------Informacion del creador osea yo :3-------------------------------
info = Button(raiz,bg="white",bitmap="info",width=30,height=30,command=informacion,cursor="hand2",relief="solid",bd=2)
info.place(x=768,y=615)
raiz.mainloop()