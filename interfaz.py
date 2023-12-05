from tkinter import *
from tkinter import ttk
from config import *
from funciones import *

class Interfaz_app(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.construir_widget()

    #metodo propio vamos a darle las configuraciones basicas para mostrar nuestra ventana
    def configurar_ventana(self):
        self.title(f"{TITULO_APP} {HORA_ACTUAL}")
        self.configure(bg=COLOR_FONDO_PRIMARIO)
        self.resizable(0,0)
        self.attributes("-alpha",0.96)
        w,h=1500,700
        centrar_ventana(self,w,h)

    def construir_widget(self):
        #CAJITA DE TEXTOS
        self.cajas_textos=LabelFrame(self,text="Cajas de texto",width=150,height=360,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.cajas_textos.grid(row=0,column=0,pady=20,padx=20)
        #caja para capturar el nombre
        self.label_nombre=Label(self.cajas_textos,text="Nombres",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.nombre_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.nombre_texto.pack()
        #caja para capturar el apellido
        self.label_apellido=Label(self.cajas_textos,text="Apellidos",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.apellidos_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.apellidos_texto.pack()
        #caja para capturar el DNI
        self.label_dni=Label(self.cajas_textos,text="DNI",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.dni_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.dni_texto.pack()
        #caja para capturar el nombre
        self.label_dni=Label(self.cajas_textos,text="Fecha de Nacimiento",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.dni_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.dni_texto.pack()
        #caja para capturar el nombre
        self.label_f_naci=Label(self.cajas_textos,text="Programa de estudios",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.f_nacimiento_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.f_nacimiento_texto.pack()
        #caja para capturar el nombre
        self.label_programa=Label(self.cajas_textos,text="Correo Electronico",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.programa_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.programa_texto.pack()
        #caja para celular
        self.label_celular=Label(self.cajas_textos,text="Celular",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.celular_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.celular_texto.pack()
        
        
        #FIN CAJITA DE TEXTOS
        #CAJITA DE BOTONES
        self.cajas_botones=LabelFrame(self,text="Cajas de botones",width=150,height=430,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.cajas_botones.grid(row=0,column=1,pady=20,padx=20)
        #boton nuevo
        self.nuevo=Button(self.cajas_botones,command=lambda:nuevo(self),text="Nuevo",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #boton actualizar
        self.actualizar=Button(self.cajas_botones,command=lambda: actualizar(self),text="Actualizar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #boton eliminar
        self.eliminar=Button(self.cajas_botones,command=lambda:eliminar(self),text="Eliminar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #boton cancelar
        self.cancelar=Button(self.cajas_botones,command=lambda:limpiar(self),text="Cancelar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #FIN CAJITA DE BOTONES
        #TABLA DE DATOS
        self.caja_datos=LabelFrame(self,text="Caja de Datos",width=1000,height=360,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.caja_datos.grid(row=0,column=2,pady=20,padx=20)

        #tabla
        self.tabla_datos=ttk.Treeview(self.caja_datos,columns=("#0","#1","#2","#3","#4","#5","#6"))
        self.tabla_datos.column("#0",width=40)
        self.tabla_datos.column("#1",width=120)
        self.tabla_datos.column("#2",width=40)
        self.tabla_datos.column("#3",width=150)
        self.tabla_datos.column("#4",width=150)
        self.tabla_datos.column("#5",width=140)
        self.tabla_datos.column("#6",width=40)
        
        self.tabla_datos.heading("#0",text="Nombres")
        self.tabla_datos.heading("#1",text="Apellidos")
        self.tabla_datos.heading("#2",text="DNI")
        self.tabla_datos.heading("#3",text="Fecha de Nacimiento")
        self.tabla_datos.heading("#4",text="Programa de Estudios")
        self.tabla_datos.heading("#5",text="Correo Electronico")
        self.tabla_datos.heading("#6",text="Celular")
        
        
        
        alumnitos=db.mostrar('Estudiantes')
        for id,nom,ape,cel in alumnitos:
            self.tabla_datos.insert("",END,text=nom,values=(ape,cel))
        print(alumnitos)
        self.tabla_datos.bind("<Double-1>",lambda event:dobleClick(self,event))
        self.tabla_datos.place(x=0,y=0,width=400,height=600)
        #FIN DE TABLA DE DATOS
        
        