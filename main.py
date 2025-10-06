import tkinter as tk
from tkinter import font as tkfont
import os
import subprocess
import sys

def opcion1():
    ruta = os.path.join(os.path.dirname(__file__), "dados.py")
    subprocess.Popen([sys.executable, ruta])

def opcion2():
    ruta = os.path.join(os.path.dirname(__file__), "tienda.py")
    subprocess.Popen([sys.executable, ruta])

def opcion3():
    ruta = os.path.join(os.path.dirname(__file__), "huevos.py")
    subprocess.Popen([sys.executable, ruta])

def opcion4():
    ruta = os.path.join(os.path.dirname(__file__), "azucar.py")
    subprocess.Popen([sys.executable, ruta])

def on_enter(e):
    e.widget['background'] = "#4A90E2"   
    e.widget['foreground'] = "white"
    e.widget['relief'] = "raised"

def on_leave(e):
    e.widget['background'] = "#F5F7FA"  
    e.widget['foreground'] = "#2C3E50"
    e.widget['relief'] = "flat"
ventana = tk.Tk()
ventana.title("Simulación de Eventos Discretos")
ventana.geometry("500x550")
ventana.config(bg="#1E3A5F")  
ventana.resizable(False, False)

frame_principal = tk.Frame(ventana, bg="#1E3A5F")
frame_principal.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)
titulo = tk.Label(
    frame_principal,
    text="SIMULACIÓN DE\nEVENTOS DISCRETOS",
    font=("Segoe UI", 24, "bold"),
    fg="#FFFFFF",
    bg="#1E3A5F",
    justify=tk.CENTER
)
titulo.pack(pady=(20, 10))
linea = tk.Frame(frame_principal, height=3, bg="#4A90E2", width=250)
linea.pack(pady=10)
subtitulo = tk.Label(
    frame_principal,
    text="Selecciona una simulación para comenzar",
    font=("Segoe UI", 11),
    fg="#A8C5E2",
    bg="#1E3A5F"
)
subtitulo.pack(pady=(5, 35))

frame_botones = tk.Frame(frame_principal, bg="#1E3A5F")
frame_botones.pack(pady=10)

botones_config = [
    ("🎲  Simulación de Dados", opcion1),
    ("🛒  Simulación de Tienda", opcion2),
    ("🥚  Simulación de Huevos", opcion3),
    ("🧂  Simulación de Azúcar", opcion4)
]

for texto, comando in botones_config:
    contenedor_btn = tk.Frame(frame_botones, bg="#2A4A6F", bd=0)
    contenedor_btn.pack(pady=12)
    
    btn = tk.Button(
        contenedor_btn,
        text=texto,
        width=28,
        height=2,
        bg="#F5F7FA",
        fg="#2C3E50",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2",
        command=comando,
        activebackground="#4A90E2",
        activeforeground="white"
    )
    btn.pack(padx=3, pady=3)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

tk.Frame(frame_principal, bg="#1E3A5F", height=20).pack()

info_frame = tk.Frame(frame_principal, bg="#2A4A6F", relief="flat", bd=0)
info_frame.pack(pady=15, padx=20, fill=tk.X)

info_text = tk.Label(
    info_frame,
    text="ℹ️  Cada simulación se ejecutará en una ventana separada",
    font=("Segoe UI", 9),
    fg="#D4E3F0",
    bg="#2A4A6F",
    pady=8
)
info_text.pack()

pie = tk.Label(
    frame_principal,
    text="Desarrollado con Python & Tkinter",
    font=("Segoe UI", 9, "italic"),
    fg="#7B98B8",
    bg="#1E3A5F"
)
pie.pack(side=tk.BOTTOM, pady=(20, 10))

ventana.mainloop()