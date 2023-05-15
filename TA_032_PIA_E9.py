import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MaquinaTuring import turing_machine

def check_input():
    input_string = input_entry.get()
    if turing_machine(input_string):
        messagebox.showinfo("Resultado", "La cadena es válida según las reglas de la máquina de Turing.")
    else:
        messagebox.showerror("Resultado", "La cadena no es válida según las reglas de la máquina de Turing.")

def close_window():
    sys.exit()

def clear_text():
    input_entry.delete(0, 'end')

# Crear la ventana principal
root = tk.Tk()
root.iconbitmap('D:/PIA Teoria de automatas/icono/pochita.ico')
root.title("Máquina de Turing")
root.geometry("600x300")

# Cambiar el color de fondo y el contorno de la ventana
root.configure(bg="#F0F0F0", bd=5, relief="solid")

# Estilos
label_style = {"font": ("Arial", 12), "bg": "#F0F0F0"}

# Crear los widgets
text_label1 = tk.Label(root, text="Producto Integrado de Aprendizaje Teoria de Automatas", **label_style)
text_label2 = tk.Label(root, text="Pablo Tadeo Capistran Fernandez Matricula 1971973", **label_style)
input_label = tk.Label(root, text="Ingresa una cadena para verificar:", **label_style)
input_entry = ttk.Entry(root, width=40)
check_button = ttk.Button(root, text="Verificar", command=check_input)
clear_button = ttk.Button(root, text="Limpiar", command=clear_text)
close_button = ttk.Button(root, text="Cerrar", command=close_window)

# Aumentar el tamaño de los botones
check_button.configure(width=20)
clear_button.configure(width=20)
close_button.configure(width=20)

# Posicionar los widgets en la ventana usando grid
text_label1.grid(row=0, column=0, columnspan=2, pady=10)
text_label2.grid(row=1, column=0, columnspan=2)
input_label.grid(row=2, column=0, pady=10, sticky=tk.E)
input_entry.grid(row=2, column=1, pady=10, sticky=tk.W)
check_button.grid(row=3, column=0, pady=10)
clear_button.grid(row=3, column=1, pady=10)
close_button.grid(row=4, column=0, columnspan=2, pady=5)

# Ajustar el tamaño de las columnas
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Iniciar el bucle de eventos
root.mainloop()