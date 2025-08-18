import tkinter as tk
def Verificar():
    texto = entrada.get()
    longitud = len(texto)
    texto_mayus = texto.upper()

    label_longitud.config(text=f"Longitud: {longitud}")
    label_mayusculas.config(text=texto_mayus)

#1.Ventana Principal:
programa = tk.Tk()
programa.title("Contador y Manipulador de Texto")
programa.geometry("500x175")

#2.Widgets:
#Label para indicar al usuario que ingrese texto (ej., "Introduce tu texto aquí:").
label_instruccion = tk.Label(programa, text="Introduce el texto:")
label_instruccion.pack(pady=4)
#Entry donde el usuario pueda escribir su texto.
entrada = tk.Entry(programa, width=45)
entrada.pack(pady=4)
#Button con el texto "Procesar Texto"/#3.Funcionalidad:
boton = tk.Button(programa, text="Procesar Texto", command=Verificar)
boton.pack(pady=10)
#Label para mostrar la longitud del texto (inicialmente vacío o con "Longitud:0")
label_longitud = tk.Label(programa, text="Longitud: 0")
label_longitud.pack(pady=5)
#Label para mostrar el texto en mayúsculas (inicialmente vacío).
label_mayusculas = tk.Label(programa, text="", font=("Helvetica", 12, "bold"))
label_mayusculas.pack(pady=5)

programa.mainloop()