from dis import show_code
from functools import update_wrapper
from msilib.schema import ComboBox, Font
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from turtle import bgcolor, width
from pip import main
from urllib.request import urlcleanup, urlopen
import json
import requests

#DEFINIR VARIABLES
color="#646FD4"
rojo = "#FF0000"
colorboton = "#9BA3EB"


#CONSUMIR APIa
url = "http://localhost:3000/get_by_almacen/1"
response = urlopen(url)
data_json = json.loads(response.read())

def show_frame(frame):
    frame.tkraise()
    

def fill_table():
    contador=0
    for data in data_json:    
    
        nombre=data_json[contador]["nombre"]
        id=data_json[contador]["id_instrumento"]
        stock = data_json[contador]["stock"]
        tv.insert("", END, text=id, values=(nombre, stock))
        
        contador=contador+1


root = tkinter.Tk()
root.geometry("960x800")
root.title("MUSICPRO")
# root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


verInstrumentos = tkinter.Frame(root, bg=color)
agregarInstrumentos = tkinter.Frame(root, bg=color)
editarInstrumentos = tkinter.Frame(root, bg=color)
mainFrame = tkinter.Frame(root, bg=color)
santiagoFrame = tkinter.Frame(root, bg=color)
valparaisoFrame = tkinter.Frame(root, bg=color)
bodegaFrame = tkinter.Frame(root, bg=color)
ventaFrame = tkinter.Frame(root, bg=color)
for frame in (verInstrumentos, agregarInstrumentos, editarInstrumentos, mainFrame, santiagoFrame, ventaFrame, bodegaFrame, valparaisoFrame):
    frame.grid(row=0, column=0, sticky="nsew")
    
    
####################################################################################################################################################################################
####################################################################### VER INSTRUMENTOS (FRAME 1)##################################################################################
####################################################################################################################################################################################

def fn_refresh():
    for i in tv.get_children():
        tv.delete(i)
        
    response = urlopen(url)
    data_json = json.loads(response.read())    
    
    for i in data_json:    
        nombre=i["nombre"]
        id=i["id_instrumento"]
        precio=i["precio"]
        stock=i["stock"]
        tv.insert("", END, text=id, values=(nombre, precio, stock))
        
    verInstrumentos.update()


    
frame1_title = tkinter.Label(verInstrumentos, text="Mostrar Instrumentos", bg=color, font="COMIC_SANS 40", anchor="center")
frame1_title.place(x=150, y=0)

refreshBtn = tkinter.Button(verInstrumentos, text="Refrescar Tabla",bg=colorboton , command=lambda:fn_refresh())
refreshBtn.place(x = 220, y = 550, height=50,width=190)

frame1_btn = tkinter.Button(verInstrumentos, text="Agregar Instrumento",bg=colorboton , command=lambda:show_frame(agregarInstrumentos),width=20, height=2)
frame1_btn.place(x = 720, y = 100, height=50,width=190)

frame1_btn2 = tkinter.Button(verInstrumentos, text="Editar Instrumento",bg=colorboton , command=lambda:show_frame(editarInstrumentos),width=20, height=2)
frame1_btn2.place(x = 720, y = 180, height=50,width=190)

frame1_btn3 = tkinter.Button(verInstrumentos, text="Realizar Venta",bg=colorboton , command=lambda:show_frame(ventaFrame), width=20, height=2)
frame1_btn3.place(x = 720, y = 260, height=50,width=190)

frame1_btn3 = tkinter.Button(verInstrumentos, text="Volver Inicio",bg=colorboton , command=lambda:show_frame(mainFrame), width=20, height=2)
frame1_btn3.place(x = 720, y = 340, height=50,width=190)

frame1_btn3 = tkinter.Button(verInstrumentos, text="Salir",bg=colorboton , command=root.destroy, width=20, height=2)
frame1_btn3.place(x = 720, y = 420, height=50,width=190)
    
#CREAR TABLA
tv = ttk.Treeview(verInstrumentos, columns=("nombre","precio","stock"))
style = ttk.Style()

style.configure('Treeview', rowheight = 40)

tv.column("#0",stretch=True, width=50,anchor=CENTER)
tv.column("nombre",stretch=True, width=150,anchor=CENTER)
tv.column("stock",stretch=True, width=100,anchor=CENTER)
tv.column("precio",stretch=True, width=150,anchor=CENTER)


tv.heading("#0", text="Id", anchor="center")
tv.heading("nombre", text="Nombre", anchor="center")
tv.heading("precio", text="Precio", anchor="center")
tv.heading("stock", text="Stock", anchor="center")

tv.column("#0", anchor="center")

contador=0
for data in data_json:    

    nombre=data_json[contador]["nombre"]
    id=data_json[contador]["id_instrumento"]
    stock=data_json[contador]["stock"]
    precio=data_json[contador]["precio"]
    tv.insert("", END, text=id, values=(nombre, precio, stock))
    
    contador=contador+1

        

    
tv.place(x = 100, y = 100)

####################################################################################################################################################################################
####################################################################### AGREGAR INSTURMENTOS (FRAME 2) #############################################################################
####################################################################################################################################################################################



datos = {}

#VARIABLES PARA ALMACENAR DATOS DE LOS INPUTS
nomVariable = tkinter.StringVar()
precioVariable = tkinter.IntVar()
stockVariable = tkinter.StringVar()

#FUNCION BOTON POST
def fn_post():
    datos = {'nombre':nomVariable.get(), 'precio': precioVariable.get(), 'stock': stockVariable.get(), 'id_almacen': 2}
    requests.post("http://localhost:3000/instrumento", json=datos)


#CREAR LOS INPUTS
nombreEntry = ttk.Entry(agregarInstrumentos, textvariable =nomVariable)
precioEntry = ttk.Entry(agregarInstrumentos,textvariable = precioVariable)
stockEntry = ttk.Entry(agregarInstrumentos, textvariable=stockVariable)


#BOTON DE POST
postBtn = tkinter.Button(agregarInstrumentos, text="Agregar", bg=colorboton ,command=lambda:fn_post())
postBtn.place(x = 150, y = 210, height=50, width=300)

#CREAR BOTONES DE NAVEGACIÓN
frame2_btn = tkinter.Button(agregarInstrumentos, text="Volver", bg=colorboton , command=lambda:show_frame(verInstrumentos))
frame2_btn3 = tkinter.Button(agregarInstrumentos, text="Salir",bg=colorboton , command=root.destroy)


#CREAR LABELS DE LOS INPUTS
nomLabel = tkinter.Label(agregarInstrumentos, text= "NOMBRE", bg=color, font="COMIC_SANS 12", anchor="center")
precioLabel = tkinter.Label(agregarInstrumentos, text= "PRECIO", bg=color, font="COMIC_SANS 12", anchor="center")
stockLabel = tkinter.Label(agregarInstrumentos, text= "STOCK", bg=color, font="COMIC_SANS 12", anchor="center")
frame2_title = tkinter.Label(agregarInstrumentos, text="Agregar Instrumentos", bg=color, font="COMIC_SANS 40", anchor="center")


#POSICIONAR LABELS
frame2_title.place(x = 80, y = 0)
nomLabel.place(x = 50, y = 90)
precioLabel.place(x = 50, y = 130)
stockLabel.place(x = 50, y = 170)

#POSICIONAR INPUTS
nombreEntry.place(x = 150, y =  90, width=300)
precioEntry.place(x = 150, y =  130, width=300)
stockEntry.place(x = 150, y = 170, width=300)


#POSICIONAR BOTONES DE NAVEGACIÓN
frame2_btn.place(x = 710, y = 100, height=50,width=190)
frame2_btn3.place(x = 710, y = 180, height=50,width=190)



####################################################################################################################################################################################
####################################################################### EDITAR INSTRUMENTOS (FRAME 3) ###############################################################################
####################################################################################################################################################################################

ids=['Seleccione...']    
for i in data_json:
    ids.append(i["id_instrumento"])
    
def frame3_llenar_comboboxId():    
    response = urlopen(url)
    data_json = json.loads(response.read())   
    
    contador = 0
    ids.clear()
    ids.append('Seleccione...')
    frame3_idCombobox.set('')
    for i in data_json:
        ids.append(i["id_instrumento"])        
        contador = contador+1
    frame3_idCombobox['values']=ids
    frame3_idCombobox.current(0)

frame3_nomVariable = tkinter.StringVar()
frame3_precioVariable = tkinter.StringVar()
frame3_stockVariable = tkinter.StringVar()

frame3_title = tkinter.Label(editarInstrumentos, text="Editar Instrumentos", bg=color, font="COMIC_SANS 40", anchor="center")
frame3_title.place(x = 80, y = 0)

#CREAR LOS INPUTS
frame3_idCombobox = ttk.Combobox(editarInstrumentos, state ="readonly", values = ids)
frame3_idCombobox.current(0)
frame3_nombreEntry = ttk.Entry(editarInstrumentos, textvariable = frame3_nomVariable)
frame3_precioEntry = ttk.Entry(editarInstrumentos,textvariable = frame3_precioVariable)
frame3_stockEntry = ttk.Entry(editarInstrumentos, textvariable=frame3_stockVariable)


#CREAR BOTONES
frame3_enviarBtn = tkinter.Button(editarInstrumentos, text="Enviar Datos", bg=colorboton, command=lambda:fn_update())
frame3_cargarBtn = tkinter.Button(editarInstrumentos, text="Cargar Datos", bg=colorboton, command=lambda:put_placeholders())
frame3_btn = tkinter.Button(editarInstrumentos, text="Volver", bg=colorboton , command=lambda:show_frame(verInstrumentos))
frame3_btn3 = tkinter.Button(editarInstrumentos, text="Salir",bg=colorboton , command=root.destroy)
frame3_recargarCombobox =tkinter.Button(editarInstrumentos, text="Refresh Combobox",bg=colorboton , command=lambda:frame3_llenar_comboboxId())


#CREAR LABELS DE LOS INPUTS
frame3_nomLabel = tkinter.Label(editarInstrumentos, text= "NOMBRE", bg=color, font="COMIC_SANS 12", anchor="center")
frame3_idLabel = tkinter.Label(editarInstrumentos, text="ID", bg=color,font="COMIC_SANS 12", anchor="center")
frame3_precioLabel = tkinter.Label(editarInstrumentos, text= "PRECIO", bg=color, font="COMIC_SANS 12", anchor="center")
frame3_stockLabel = tkinter.Label(editarInstrumentos, text= "STOCK", bg=color, font="COMIC_SANS 12", anchor="center")
frame3_title = tkinter.Label(editarInstrumentos, text="Editar Instrumentos", bg=color, font="COMIC_SANS 40", anchor="center")


#POSICIONAR LABELS
frame3_title.place(x = 80, y = 0)
frame3_idLabel.place(x = 50, y = 90)
frame3_nomLabel.place(x = 50, y = 130)
frame3_precioLabel.place(x = 50, y = 170)
frame3_stockLabel.place(x = 50, y = 210)

#POSICIONAR INPUTS
frame3_idCombobox.place(x=150, y=90, width= 300)
frame3_nombreEntry.place(x = 150, y =  130, width=300)
frame3_precioEntry.place(x = 150, y =  170, width=300)
frame3_stockEntry.place(x = 150, y = 210, width=300)


#POSICIONAR BOTONES 
frame3_enviarBtn.place(x = 300, y = 250)
frame3_cargarBtn.place(x = 100, y = 250)
frame3_btn.place(x = 710, y = 100, height=50,width=190)
frame3_btn3.place(x = 710, y = 180, height=50,width=190)
frame3_recargarCombobox.place(x=550, y=90)

def fn_update():    
    id = frame3_idCombobox.get()
    url = "http://localhost:3000/instrumento/%s" % (int(id))
    datos = {'nombre':frame3_nomVariable.get(), 'stock': frame3_stockVariable.get(), 'precio': frame3_precioVariable.get() }
    requests.put(url, json=datos)
    frame3_idCombobox.current(0)
    frame3_nombreEntry.delete(0, END)
    frame3_precioEntry.delete(0, END)
    frame3_stockEntry.delete(0, END)
    
def put_placeholders():
    id = frame3_idCombobox.get()
    if id != ids[0]:
        response = urlopen(url)
        data_json = json.loads(response.read())   
        for i in data_json:
            idInstrumento = i["id_instrumento"]                                
            if int(id) == idInstrumento:  
                frame3_nombreEntry.delete(0, END)  
                frame3_stockEntry.delete(0, END)
                frame3_precioEntry.delete(0, END)       
                ph_nombre = i["nombre"]
                ph_stock = i["stock"]
                ph_precio = i["precio"]
                frame3_nombreEntry.insert(0, ph_nombre)
                frame3_stockEntry.insert(0, ph_stock)
                frame3_precioEntry.insert(0, ph_precio)

####################################################################################################################################################################################
####################################################################### MAIN FRAME #################################################################################################
####################################################################################################################################################################################


#CREAR WIDGETS
titulo = tkinter.Label(mainFrame, text="🎸 SUCURSALES 🎸", bg=color, font="COMIC_SANS 40")
santiagoBtn=tkinter.Button(mainFrame,text="Sucursal Santiago",bg=colorboton , command=lambda:show_frame(verInstrumentos))
valparaisoBtn=tkinter.Button(mainFrame,text="Sucursal Valparaiso",bg=colorboton , command=lambda:show_frame(verInstrumentos))
bodegaBtn=tkinter.Button(mainFrame,text="Bodega",bg=colorboton , command=lambda:show_frame(verInstrumentos))
closeBtn=tkinter.Button(mainFrame,text="Salir",bg=colorboton ,command=root.destroy)


#POSICIONAR WIDGETS
titulo.place(x = 200, y = 50)
santiagoBtn.place(x=350,y=150,height=50,width=200)
valparaisoBtn.place(x=350,y=220,height=50,width=200)
bodegaBtn.place(x=350,y=290,height=50,width=200)
closeBtn.place(x=350,y=360,height=50,width=200)


####################################################################################################################################################################################
####################################################################### VENTA PRODUCTOS ############################################################################################
####################################################################################################################################################################################
nomproductoList = ["Seleccione..."]
for i in data_json:
    nomproductoList.append(i["nombre"])
    
def frame4_llenar_comboboxNombre():    
    response = urlopen(url)
    data_json = json.loads(response.read())   
    
    contador = 0
    nomproductoList.clear()
    nomproductoList.append('Seleccione...')
    frame4_productoCombobox.set('')
    for i in data_json:
        nomproductoList.append(i["nombre"])        
        contador = contador+1
    frame4_productoCombobox['values']=nomproductoList
    frame4_productoCombobox.current(0)

def calcular_totalVenta():
    venta=0
    num = frame4_numVariable.get()
    nombreProducto = frame4_productoCombobox.get()
    for i in data_json:
        if nombreProducto == i["nombre"]:
            precio = i["precio"]
            venta = precio*num
            frame4_totalsumVariable.set(f"${venta}")
            
frame4_numVariable = tkinter.IntVar()
frame4_totalsumVariable = tkinter.StringVar()

#CREAR WIDGETS
    #entries
frame4_numEntry = tkinter.Entry(ventaFrame, textvariable=frame4_numVariable)
    #combobox
frame4_productoCombobox = ttk.Combobox(ventaFrame, state ="readonly", values = nomproductoList)
frame4_productoCombobox.current(0)
    #labels
frame4_tituloLabel = tkinter.Label(ventaFrame, text="🎸 VENDER PRODUCTOS 🎸", bg=color, font="COMIC_SANS 40")
frame4_productoLabel = tkinter.Label(ventaFrame, text="PRODUCTO", bg=color, font="COMIC_SANS 12" )
frame4_numproductoLabel = tkinter.Label(ventaFrame, text="NUMERO PRODUCTOS", bg=color, font="COMIC_SANS 12")
frame4_totalLabel = tkinter.Label(ventaFrame, text="TOTAL VENTA", bg=color, font="COMIC_SANS 12" )
frame4_totalsumLabel = tkinter.Label(ventaFrame, text="", bg=color, font="COMIC_SANS 12", textvariable=frame4_totalsumVariable)
    #botones
frame4_btn = tkinter.Button(ventaFrame, text="Volver", bg=colorboton , command=lambda:show_frame(verInstrumentos))
frame4_btn3 = tkinter.Button(ventaFrame, text="Salir",bg=colorboton , command=root.destroy)
frame4_calcularBtn = tkinter.Button(ventaFrame, text="Calcular Precio", bg=colorboton, command=lambda:calcular_totalVenta())
frame4_realizarventaBtn = tkinter.Button(ventaFrame, text="Realizar Venta", bg=colorboton, command=lambda:update_stock())
frame4_refrescarBtn = tkinter.Button(ventaFrame, text="Refrescar Combobox", bg=colorboton,command=lambda:frame4_llenar_comboboxNombre())

#POSICIONAR LABELS
frame4_tituloLabel.place(x = 80, y = 0)
frame4_productoLabel.place(x = 50, y = 90)
frame4_numproductoLabel.place(x=50, y = 130)
frame4_totalLabel.place(x=50, y=170)

#POSICIONAR BOTONES
frame4_btn.place(x = 710, y = 150, height=50,width=190)
frame4_btn3.place(x = 710, y = 230, height=50,width=190)
frame4_calcularBtn.place(x=350, y=240, height=50, width=190)
frame4_realizarventaBtn.place(x=120, y=240, height=50, width=190)
frame4_refrescarBtn.place(x=470, y=90)

#POSICIONAR WIDGETS
frame4_productoCombobox.place(x=250, y=90, width=200)
frame4_numEntry.place(x=250, y=130, width=200)
frame4_totalsumLabel.place(x=200, y=170, width=200)

def update_stock():
    nombre = frame4_productoCombobox.get()
    for i in data_json:
        if nombre == i["nombre"]:
            id = i["id_instrumento"]
            stockActual = i["stock"]
            nombre = i["nombre"]
            precio = i["precio"]
    
    frame4_stockfinalVariable = stockActual-frame4_numVariable.get()
    url = "http://localhost:3000/instrumento/%s" % (int(id))
    datos = {'nombre':nombre, 'precio':precio, 'stock': frame4_stockfinalVariable}
    requests.put(url, json=datos)


show_frame(mainFrame)
root.mainloop()















































