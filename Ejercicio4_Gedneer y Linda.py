import tkinter as tk
from tkinter import messagebox

datos = []

def agregar_elemento():
    elemento = int(caja_texto.get())
    if elemento == 0:
        ordenar_arreglo()
        ventana.quit()
    else:
        datos.append(elemento)
        caja_texto.delete(0, tk.END)
        actualizar_tamano_arreglo()
        actualizar_elemento_mayor()
        actualizar_elemento_menor()

def ordenar_arreglo():
    n = len(datos)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if datos[j] > datos[j+1]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
    mostrar_arreglo_ordenado()

def mostrar_arreglo_ordenado():
    messagebox.showinfo("Arreglo Ordenado", f"El arreglo ordenado de menor a mayor es:\n{datos}")

def actualizar_tamano_arreglo():
    tamano = len(datos)
    etiqueta_tamano.config(text=f"Tamaño del arreglo: {tamano}")

def actualizar_elemento_mayor():
    elemento_mayor = max(datos) if datos else None
    etiqueta_elemento_mayor.config(text=f"Elemento de mayor valor: {elemento_mayor}")

def actualizar_elemento_menor():
    elemento_menor = min(datos) if datos else None
    etiqueta_elemento_menor.config(text=f"Elemento de menor valor: {elemento_menor}")

ventana = tk.Tk()
ventana.title("Programa de Ordenamiento")

etiqueta_instruccion = tk.Label(ventana, text="Ingrese un elemento entero (0 para terminar):")
etiqueta_instruccion.pack()

caja_texto = tk.Entry(ventana)
caja_texto.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack()

etiqueta_tamano = tk.Label(ventana, text="")
etiqueta_tamano.pack()

etiqueta_elemento_mayor = tk.Label(ventana, text="")
etiqueta_elemento_mayor.pack()

etiqueta_elemento_menor = tk.Label(ventana, text="")
etiqueta_elemento_menor.pack()

ventana.geometry("300x200")  # Establecer el tamaño de la ventana
label_nombre = tk.Label(ventana, text="Realizado por: Gedneer Vasquez y Linda Inestroza")
label_nombre.pack()


ventana.mainloop()
