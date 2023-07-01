import tkinter as tk
from tkinter import messagebox
from queue import Queue

elementos_encolados = []

def encolar_elemento():
    elemento = int(caja_texto.get())
    if elemento == 0:
        mostrar_elementos_encolados()
        ventana.quit()
    else:
        cola.put(elemento)
        elementos_encolados.append(elemento)
        caja_texto.delete(0, tk.END)
        actualizar_tamano_cola()
        actualizar_valores_cola()

def desencolar_elemento():
    if not cola.empty():
        elemento = cola.get()
        if elemento != 0:
            etiqueta_estado.config(text=f"Elemento desencolado: {elemento}")
    else:
        etiqueta_estado.config(text="La cola está vacía")
    actualizar_tamano_cola()
    actualizar_valores_cola()

def buscar_elemento():
    elemento_buscar = int(caja_texto_buscar.get())
    if elemento_buscar in elementos_encolados:
        messagebox.showinfo("Búsqueda", f"El elemento {elemento_buscar} está encolado.")
    else:
        messagebox.showinfo("Búsqueda", f"El elemento {elemento_buscar} no está encolado.")

def actualizar_tamano_cola():
    tamano = cola.qsize()
    etiqueta_tamano.config(text=f"Tamaño de la cola: {tamano}")

def actualizar_valores_cola():
    valores = list(cola.queue)
    etiqueta_valores.config(text=f"Valores en la cola: {valores}")

def mostrar_elementos_encolados():
    mensaje = "Estos son todos los elementos encolados:\n"
    for elemento in elementos_encolados:
        mensaje += str(elemento) + "\n"
    messagebox.showinfo("Elementos encolados", mensaje)

ventana = tk.Tk()
ventana.title("Programa de Colas")

etiqueta_instruccion = tk.Label(ventana, text="Ingrese un elemento entero (0 para terminar):")
etiqueta_instruccion.pack()

caja_texto = tk.Entry(ventana)
caja_texto.pack()

boton_encolar = tk.Button(ventana, text="Encolar", command=encolar_elemento)
boton_encolar.pack()

boton_desencolar = tk.Button(ventana, text="Desencolar", command=desencolar_elemento)
boton_desencolar.pack()

etiqueta_estado = tk.Label(ventana, text="")
etiqueta_estado.pack()

etiqueta_valores = tk.Label(ventana, text="")
etiqueta_valores.pack()

etiqueta_tamano = tk.Label(ventana, text="")
etiqueta_tamano.pack()

etiqueta_instruccion_buscar = tk.Label(ventana, text="Ingrese el elemento a buscar:")
etiqueta_instruccion_buscar.pack()

caja_texto_buscar = tk.Entry(ventana)
caja_texto_buscar.pack()

boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_elemento)
boton_buscar.pack()

cola = Queue()

actualizar_tamano_cola()  
actualizar_valores_cola()  

ventana.geometry("300x250")  

def on_closing():
    mostrar_elementos_encolados()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", on_closing)

def actualizar_tamano_cola_esquina():
    tamano = cola.qsize()
    ventana.after(100, actualizar_tamano_cola_esquina)  

actualizar_tamano_cola_esquina()  

label_nombre = tk.Label(ventana, text="Realizado por: Gedneer Vásquez y Linda Inestroza")
label_nombre.pack()

ventana.mainloop()



