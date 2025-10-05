import tkinter as tk
import os
import subprocess
import sys

def opcion1():
    ruta = os.path.join(os.path.dirname(__file__), "dados.py")
    subprocess.Popen([sys.executable, ruta])

def opcion3():
    ruta = os.path.join(os.path.dirname(__file__), "huevos.py")
    subprocess.Popen([sys.executable, ruta])

def opcion4():
    ruta = os.path.join(os.path.dirname(__file__), "azucar.py")
    subprocess.Popen([sys.executable, ruta])

def on_enter(e):
    e.widget['background'] = "#1abc9c"   
    e.widget['foreground'] = "white"

def on_leave(e):
    e.widget['background'] = "#ecf0f1"  
    e.widget['foreground'] = "black"

ventana = tk.Tk()
ventana.title("SIMULACIÓN DE EVENTOS DISCRETOS")
ventana.geometry("400x350")
ventana.config(bg="#2c3e50")  

titulo = tk.Label(
    ventana,
    text="SIMULACIÓN DE EVENTOS DISCRETOS",
    font=("Arial Black", 14, "bold"),
    fg="white",
    bg="#2c3e50"
)
titulo.pack(pady=20)
botones_textos = [("Dados", opcion1), ("Huevos", opcion3), ("Azúcar", opcion4)]

for texto, comando in botones_textos:
    btn = tk.Button(
        ventana,
        text=texto,
        width=20,
        height=2,
        bg="#ecf0f1",
        fg="black",
        font=("Arial", 12, "bold"),
        relief="flat",
        command=comando
    )
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
ventana.mainloop()
