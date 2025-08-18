import tkinter as tk
import math

def click_boton(caracter):
    current_text = display.get()

    if caracter == '=':
        try:
            result = eval(current_text,vars(math))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))

        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, caracter)

root = tk.Tk()
root.title("Calculadora Científica Simple")
root.geometry("320x500")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

display = tk.Entry(root, font=("Arial", 20), bd=5, justify="right")
display.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW, padx=5, pady=5)

botones = [
    'sin(', 'cos(', 'tan(', 'sqrt(',
    'log(', '**', '(', ')',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_num = 1
col_num = 0

for boton_texto in botones:
    if boton_texto:  # Skip empty strings
        button = tk.Button(root, text=boton_texto, font=("Arial", 16),
                           command=lambda b=boton_texto: click_boton(b))
        button.grid(row=row_num, column=col_num, sticky=tk.NSEW, padx=5, pady=5)

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()