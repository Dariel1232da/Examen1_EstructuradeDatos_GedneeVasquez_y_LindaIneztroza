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
        actualizar_promedio()
        actualizar_suma()

def ordenar_arreglo():
    n = len(datos)
    for i in range(n-1):
        indice_max = i
        for j in range(i+1, n):
            if datos[j] > datos[indice_max]:
                indice_max = j
        datos[i], datos[indice_max] = datos[indice_max], datos[i]
    mostrar_arreglo_ordenado()

def mostrar_arreglo_ordenado():
    messagebox.showinfo("Arreglo Ordenado", f"El arreglo ordenado de mayor a menor es:\n{datos}")

def actualizar_tamano_arreglo():
    tamano = len(datos)
    etiqueta_tamano.config(text=f"Tamaño del arreglo: {tamano}")

def actualizar_promedio():
    if len(datos) > 0:
        promedio = sum(datos) / len(datos)
        etiqueta_promedio.config(text=f"Promedio del arreglo: {promedio:.2f}")

def actualizar_suma():
    suma = sum(datos)
    etiqueta_suma.config(text=f"Suma de los elementos del arreglo: {suma}")

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

etiqueta_promedio = tk.Label(ventana, text="")
etiqueta_promedio.pack()

etiqueta_suma = tk.Label(ventana, text="")
etiqueta_suma.pack()

ventana.geometry("300x200")  # Establecer el tamaño de la ventana

label_nombre = tk.Label(ventana, text="Realizado por: Gedneer Vásquez y Linda Inestroza")
label_nombre.pack()


ventana.mainloop()
