import tkinter as tk

def agregar_elemento():
    elemento = int(entry.get())
    arreglo.append(elemento)
    label2.config(text=str(arreglo))
    entry.delete(0,tk.END)

def buscar_elemento():
    elemento = int(entry1.get())
    for index in range(len(arreglo)):
        if arreglo[index] == elemento:
             return "Elemento encontrado"
    return "Elemento no encontrado"
    
def buscar_elemento_click():   
    label4.config(text=buscar_elemento())


# Crear una ventana en tkinter para mi uso
ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Busqueda lineal en tkinter")

label1 = tk.Label(ventana, text="Ingrese un elemento al arreglo :")
label1.pack()

entry = tk.Entry(ventana)
entry.pack()

boton = tk.Button(ventana, text="Agregar un elemento", command=agregar_elemento)
boton.pack()

label2 = tk.Label(ventana, text="Resultado :")
label2.pack()


label3 = tk.Label(ventana, text="Elemento a buscar :")
label3.pack()
entry1 = tk.Entry(ventana)
entry1.pack()
boton1 = tk.Button(ventana, text="Buscar elemento", command=buscar_elemento_click)
boton1.pack()

label4 = tk.Label(ventana, text="")
label4.pack()

# Declaremos el arreglo
arreglo = []  # arreglo vacio



ventana.mainloop()