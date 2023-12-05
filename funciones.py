from tkinter import *
from tkinter.messagebox import *
import orm
from tablas.Estudiantes import Estudiantes
#creamos nuestra base de datos
db = orm.SQLiteORM("Estudiantes")
db.crear_tabla(Estudiantes)
#funcion limpiar

def limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellido_texto.delete(0,END)
    ventana.dni_texto.delete(0,END)
    ventana.f_nacimiento_texto.delete(0,END)
    ventana.programa_texto.delete(0,END)
    ventana.correo_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)
    ventana.nombre_texto.focus()

def nuevo(ventana):
    name = ventana.nombre_texto.get()
    apellido = ventana.apellido_texto.get()
    dni = ventana.dni_texto.get()
    f_nacimiento = ventana.f_nacimiento_texto.get()
    programa = ventana.programa_texto.get()
    correo = ventana.correo_texto.get()
    celular = ventana.celular_texto.get()
    name = ventana.nombre_texto.focus()
    date = {
        "Nombre":name,
        "Apellido":apellido,
        'DNI':dni,
        'Fecha_de_nacimiento':f_nacimiento,
        'Programa_de_estudio':programa,
        'Correo_Electronico':correo,
        'celular':celular

    }
    db.insertarUno('Estudiantes',date)
    showinfo(title='save', message='nuevo registro agregado')
    #nuevo
    id = db.mostrar('Estudiantes', where=f'celular={celular}')[0][0]
    ventana.tabla_datos.insert('',END, text=id, values=(name,apellido,dni,f_nacimiento,programa,correo,celular))
    limpiar(ventana)
    
#eliminar 
def eliminar(ventana):
    elemento_eliminar = ventana.tabla_datos.selection()
    dato = ventana.tabla_datos.item(elemento_eliminar)['text'] #sirve para mostrar el registro seleccionado
    ventana.tabla_datos.delete(elemento_eliminar)
    db.eliminar('Estudiantes.db',where=f'id= "{dato}"')
    #db.eliminar('Usuarios',where='Nombre="ggh"')
    showwarning(title='Delete', message='registro eliminado')

def actualizar(ventana):
    if ventana.nombre_texto.get()=='':
        showerror(title='error', message='que va actualizar si noy nada')
    else:
        nombre = ventana.nombre_texto.get()
        apellidos = ventana.apellido_texto.get()
        dni = ventana.dni_texto.get()
        f_nacimiento = ventana.f_nacimiento_texto.get()
        programa = ventana.programa_texto.get()
        correo = ventana.correo_texto.get()
        celular = ventana.celular_texto.get()
        elemento_actualizar = ventana.tabla_datos.selection()
        date = ventana.tabla_datos.item(elemento_actualizar)['text']
        mensaje = askyesno(title='actualizar', message='estas seguro que deseas actulizar esta hvda')
        if mensaje == True:
            limpiar(ventana)
            update = {
                'Nombre':nombre,
                'Apellido':apellidos,
                'DNI':dni,
                'Fecha_de_nacimiento':f_nacimiento,
                'Programa_de_estudio':programa,
                'correo':correo,
                'Celular':celular
                }
            ventana.tabla_datos.selection_remove(elemento_actualizar)
            db.actualizar('Estudiantes',update,where=f'id={date}')
            return ventana.tabla_datos.item(elemento_actualizar,text=date, values=(nombre,apellidos,dni,f_nacimiento,programa,correo,celular))
        else:
            showinfo(title='no actualizo', message='no esta seleccionado')
            ventana.tabla_datos.selection_remove(elemento_actualizar)

        
def doble_clic(ventana,event):
    elemento_actualizar=ventana.tabla_datos.selection()
    captura_datos = ventana.tabla_datos.item(elemento_actualizar)
    mensaje = askyesno(title='actualizar', message='desde el registro')
    if mensaje == True:
        nombre = captura_datos['values'][0]
        apellidos = captura_datos['values'][1]
        dni = captura_datos['values'][2]
        f_nacimiento = captura_datos['values'][3]
        programa = captura_datos['values'][4]
        correo = captura_datos['values'][5]
        celular = captura_datos['values'][6]

        ventana.nombre_texto.insert(0,nombre)
        ventana.apellido_texto.insert(0,apellidos)
        ventana.celular_texto.insert(0,dni)
        ventana.celular_texto.insert(0,f_nacimiento)
        ventana.celular_texto.insert(0,programa)
        ventana.celular_texto.insert(0,correo)
        ventana.celular_texto.insert(0,celular)
    else:
        showinfo(title='actualizar',message='ningún registro seleccionado para actualizar')
        ventana.tabla_datos.selection_remove(elemento_actualizar)