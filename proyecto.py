import json
from multiprocessing.sharedctypes import Value
from pickle import TRUE
import tkinter
from tkinter import *
from tkinter import NORMAL, W, Label, Toplevel, Variable, messagebox
from tkinter.font import BOLD


class formulario:
    def __init__(self):
        self.preguntas_num=0
        self.ventana_titulo()
        self.ventana_pregunta()
        self.opcion_seleccionada=IntVar()
        self.opts=self.radio_botones()
        self.ventana_opciones()
        self.botones()
        self.total_preguntas=len(pregunta)
        self.correctas=0

    def ventana_resultado(self):
        contador_incorrectas=self.total_preguntas-self.correctas
        correctas=f"correctas:{self.correctas}"
        incorrectas=f"incorrectas:{contador_incorrectas}"
        puntaje=int(self.correctas/self.total_preguntas*100)
        resultado=f"puntaje:{puntaje}%"
        messagebox.showinfo("Resultado",f"{resultado}\n{correctas}\n{incorrectas}")

    def verificar_respuesta(self,preguntas_num):
        if self.opcion_seleccionada.get()==respuesta[preguntas_num]:
            return True

    def siguiente_boton(self):
        if self.verificar_respuesta(self.preguntas_num):
            self.correctas+=1
        self.preguntas_num+=1
        if self.preguntas_num==self.total_preguntas:
            self.ventana_resultado()
            ventana_menu.destroy()
        else:
            self.ventana_pregunta()
            self.ventana_opciones()

    def botones(self):
        siguiente_btn=tkinter.Button(ventana_pregunta,text=("Siguiente"),command=self.siguiente_boton,width=10,bg="#000000",fg="white",font=("arial",14,"bold"))
        siguiente_btn.place(x=500,y=380)
        salir_btn=tkinter.Button(ventana_pregunta,text=("Salir"),command=ventana_menu.destroy,width=5,bg="red",fg="black",font=("arial",14,"bold"))
        salir_btn.place(x=950,y=50)
    
    def ventana_opciones(self):
        val=0
        self.opcion_seleccionada.set(0)
        for x in opciones[self.preguntas_num]:
            self.opts[val]['text']=x
            val+=1
            
    def ventana_pregunta(self):
        preguntas_no=Label(ventana_pregunta,text=pregunta[self.preguntas_num],width=100,font=("Comic sans MS",12,"bold"),bg="#ffffff",fg="#620096",justify="center")
        preguntas_no.place(x=20,y=100)

    def ventana_titulo(self):
        title=Label(ventana_pregunta,text=("Formulario sobre Ciberseguridad"),width=63,bg="#620096",fg="#ffffff",font=("arial",20,"bold"),justify="center")
        title.place(x=0,y=2)

    def radio_botones(self):
        pregunta_lista=[]
        y_pos=150
        while len(pregunta_lista)<2:
            radio_btn=tkinter.Radiobutton(ventana_pregunta,text="",variable=self.opcion_seleccionada,value=len(pregunta_lista)+1,fg="#000000",bg="#ffffff",font=("arial",14,"bold"))
            pregunta_lista.append(radio_btn)
            radio_btn.place(x=100,y=y_pos)
            y_pos+=40
        return pregunta_lista


def nuevaVentana():
    ventana_menu.withdraw()
    ventana_pregunta.deiconify()

    ##comenzarFormulario()


ventana_menu=tkinter.Tk()
ventana_menu.title("Formulario Ciberseguridad")
ventana_menu.geometry("700x500")
ventana_menu.resizable(0,0)
ventana_menu.config(background="#ffffff")

imagen_inicio=tkinter.PhotoImage(file="candado.png")

etiqueta_imagen=tkinter.Label(ventana_menu,image=imagen_inicio,text="Fondo",background="#ffffff")
etiqueta_imagen.pack(pady=(20,0))

texto1=tkinter.Label(ventana_menu,text="Bienvenido al Formulario de Ciberseguridad",font=("Comic sans MS",20,"bold"),background="#ffffff",fg="#620096")
texto1.pack(pady=(0,40))

imagen_boton=tkinter.PhotoImage(file="boton.png")

boton_inicio=tkinter.Button(ventana_menu,image=imagen_boton,relief=tkinter.FLAT,border=0,command=nuevaVentana)
boton_inicio.pack()

etiqueta_instrucciones=tkinter.Label(
    ventana_menu,
    text="Leer las regas y \n Dar click una vez cuando se este listo",
    background="#ffffff",
    font=("Consolas",13),
    justify="center",

)

etiqueta_instrucciones.pack(pady=(10,105))

etiqueta_reglas=tkinter.Label(
    ventana_menu,
    text="Este formulario contiene preguntas sobre la informacion con respecto a la ciberseguridad de la empresa\nAl finalizar el formulario contara con una grafica mostrando el nivel que posee la empresa\nAdemas recibira asesorias para mejorar los aspectos que esta mal\nTomese todo el tiempo que sea necesario para realizar el formulario",
    width=100,
    font=("Time",10),
    background="#000000",
    foreground="#FACA2F",
    justify="center"
)
etiqueta_reglas.pack()

with open('data.json','r',encoding='utf-8',errors="ignore") as f:
    data=json.load(f)
pregunta=data["pregunta"]
respuesta=data["respuesta"]
opciones=data["opciones"]


ventana_pregunta=tkinter.Toplevel(width=1050,height=500)
ventana_pregunta.config(bg="#ffffff")
ventana_pregunta.resizable(0,0)
ventana_pregunta.withdraw()
formulario=formulario()

ventana_menu.mainloop()