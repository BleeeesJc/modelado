import tkinter as tk
from tkinter import ttk, messagebox
import random

def simular():
    try:
        n_juegos = int(entry_juegos.get())
        if n_juegos <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido de juegos.")
        return

    tabla_resultados.delete(*tabla_resultados.get_children())

    try:
        costo_juego = float(tabla_info.item(tabla_info.get_children()[0])['values'][1])
        perdida_casa = float(tabla_info.item(tabla_info.get_children()[1])['values'][1])
    except ValueError:
        messagebox.showerror("Error", "Los valores de la tabla deben ser numéricos.")
        return

    ganancia_neta = float(tabla_info.item(tabla_info.get_children()[2])['values'][1])
    gana_casa = 0
    gana_jugador = 0

    for juego in range(1, n_juegos + 1):
        ganancia_neta += costo_juego
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        if suma == 7:
            ganador = "Jugador"
            gana_jugador += 1
            ganancia_neta -= perdida_casa
        else:
            ganador = "Casa"
            gana_casa += 1

        tabla_resultados.insert("", "end", values=(
            juego, dado1, dado2, suma, ganador, f"{ganancia_neta:.2f}"
        ))

    porcentaje_casa = (gana_casa / n_juegos) * 100

    lbl_resultados.config(
        text=(
            f"RESULTADOS FINALES\n\n"
            f"Ganancia neta de la casa: {ganancia_neta:.2f} Bs\n"
            f"Número de juegos ganados por la casa: {gana_casa}\n"
            f"Número de juegos ganados por el jugador: {gana_jugador}\n"
            f"Porcentaje de juegos ganados por la casa: {porcentaje_casa:.2f}%\n"
        )
    )

def limpiar():
    entry_juegos.delete(0, tk.END)
    entry_juegos.insert(0, "10")
    tabla_resultados.delete(*tabla_resultados.get_children())
    lbl_resultados.config(text="Resultados aparecerán aquí.")
    for i, val in enumerate([("Costo del juego (jugador paga)", "2"),
                             ("Pérdida de la casa si gana jugador", "5"),
                             ("Ganancia inicial de la casa", "0")]):
        tabla_info.item(tabla_info.get_children()[i], values=val)

def editar_celda(event):
    item = tabla_info.identify_row(event.y)
    columna = tabla_info.identify_column(event.x)

    if not item or columna == "#0":
        return

    col_index = int(columna.replace("#", "")) - 1
    valor_actual = tabla_info.item(item, "values")[col_index]
    x, y, ancho, alto = tabla_info.bbox(item, columna)

    entry_edit = tk.Entry(tabla_info, justify="center")
    entry_edit.place(x=x, y=y, width=ancho, height=alto)
    entry_edit.insert(0, valor_actual)
    entry_edit.focus()

    def guardar_edicion(event):
        nuevo_valor = entry_edit.get()
        valores = list(tabla_info.item(item, "values"))
        valores[col_index] = nuevo_valor
        tabla_info.item(item, values=valores)
        entry_edit.destroy()

    entry_edit.bind("<Return>", guardar_edicion)
    entry_edit.bind("<FocusOut>", lambda e: entry_edit.destroy())

ventana = tk.Tk()
ventana.title("Simulación de Juego de Dados")
ventana.geometry("900x700")
ventana.config(bg="#1E3A5F")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="🎲 SIMULACIÓN DE EVENTOS DISCRETOS",
    font=("Segoe UI", 20, "bold"),
    bg="#1E3A5F",
    fg="#FFFFFF"
)
titulo.pack(pady=15)

linea = tk.Frame(ventana, height=3, bg="#4A90E2", width=400)
linea.pack()

subtitulo = tk.Label(
    ventana,
    text="Juego de Dados",
    font=("Segoe UI", 12),
    bg="#1E3A5F",
    fg="#A8C5E2"
)
subtitulo.pack(pady=(5, 15))

frame_param = tk.LabelFrame(
    ventana, 
    text="  Parámetros del Juego  ", 
    bg="#2A4A6F",
    font=("Segoe UI", 11, "bold"), 
    fg="#FFFFFF",
    bd=0,
    relief="flat"
)
frame_param.pack(pady=10, padx=20, fill="x")

contenedor_param = tk.Frame(frame_param, bg="#2A4A6F")
contenedor_param.pack(pady=15)

tk.Label(
    contenedor_param, 
    text="Número de Juegos:", 
    bg="#2A4A6F", 
    fg="#D4E3F0",
    font=("Segoe UI", 10)
).grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_juegos = tk.Entry(contenedor_param, width=12, font=("Segoe UI", 10), justify="center")
entry_juegos.grid(row=0, column=1, padx=10, pady=5)
entry_juegos.insert(0, "10")

frame_botones = tk.Frame(ventana, bg="#1E3A5F")
frame_botones.pack(pady=15)

def on_button_enter(e):
    e.widget['background'] = e.widget.hover_color

def on_button_leave(e):
    e.widget['background'] = e.widget.original_color

btn_simular = tk.Button(
    frame_botones, 
    text="▶  SIMULAR", 
    bg="#4A90E2", 
    fg="white", 
    width=16, 
    height=2, 
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    cursor="hand2",
    command=simular
)
btn_simular.original_color = "#4A90E2"
btn_simular.hover_color = "#357ABD"
btn_simular.grid(row=0, column=0, padx=10)
btn_simular.bind("<Enter>", on_button_enter)
btn_simular.bind("<Leave>", on_button_leave)

btn_limpiar = tk.Button(
    frame_botones, 
    text="🔄  LIMPIAR", 
    bg="#6C757D", 
    fg="white", 
    width=16, 
    height=2, 
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    cursor="hand2",
    command=limpiar
)
btn_limpiar.original_color = "#6C757D"
btn_limpiar.hover_color = "#5A6268"
btn_limpiar.grid(row=0, column=1, padx=10)
btn_limpiar.bind("<Enter>", on_button_enter)
btn_limpiar.bind("<Leave>", on_button_leave)

btn_salir = tk.Button(
    frame_botones, 
    text="✖  SALIR", 
    bg="#DC3545", 
    fg="white", 
    width=16, 
    height=2, 
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    cursor="hand2",
    command=ventana.destroy
)
btn_salir.original_color = "#DC3545"
btn_salir.hover_color = "#C82333"
btn_salir.grid(row=0, column=2, padx=10)
btn_salir.bind("<Enter>", on_button_enter)
btn_salir.bind("<Leave>", on_button_leave)

frame_info = tk.LabelFrame(
    ventana, 
    text="  Parámetros del Sistema  ", 
    bg="#2A4A6F",
    font=("Segoe UI", 11, "bold"), 
    fg="#FFFFFF",
    bd=0,
    relief="flat"
)
frame_info.pack(padx=20, pady=10, fill="x")
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.Treeview", 
                background="#F5F7FA",
                foreground="#2C3E50",
                fieldbackground="#F5F7FA",
                rowheight=25)
style.configure("Custom.Treeview.Heading",
                background="#4A90E2",
                foreground="white",
                font=("Segoe UI", 10, "bold"))
style.map("Custom.Treeview", background=[("selected", "#4A90E2")])

tabla_info = ttk.Treeview(
    frame_info, 
    columns=("Concepto", "Valor"), 
    show="headings", 
    height=3,
    style="Custom.Treeview"
)
tabla_info.heading("Concepto", text="Concepto")
tabla_info.heading("Valor", text="Valor (Bs.)")
tabla_info.column("Concepto", width=400, anchor="center")
tabla_info.column("Valor", width=150, anchor="center")
tabla_info.insert("", "end", values=("Costo del juego (jugador paga)", "2"))
tabla_info.insert("", "end", values=("Pérdida de la casa si gana jugador", "5"))
tabla_info.insert("", "end", values=("Ganancia inicial de la casa", "0"))
tabla_info.pack(padx=15, pady=10)

tabla_info.bind("<Double-1>", editar_celda)

frame_tabla = tk.LabelFrame(
    ventana, 
    text="  Resultados de los Lanzamientos  ", 
    bg="#2A4A6F",
    font=("Segoe UI", 11, "bold"), 
    fg="#FFFFFF",
    bd=0,
    relief="flat"
)
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

columnas = ("Juego", "Dado 1", "Dado 2", "Suma", "Ganador", "Ganancia Casa")
tabla_resultados = ttk.Treeview(
    frame_tabla, 
    columns=columnas, 
    show="headings", 
    height=8,
    style="Custom.Treeview"
)
for col in columnas:
    tabla_resultados.heading(col, text=col)
    tabla_resultados.column(col, width=130, anchor="center")
tabla_resultados.pack(fill="both", expand=True, pady=10, padx=10)

lbl_resultados = tk.Label(
    ventana,
    text="Resultados aparecerán aquí.",
    bg="#1E3A5F",
    justify="left",
    font=("Segoe UI", 10),
    fg="#D4E3F0"
)
lbl_resultados.pack(pady=10)

ventana.mainloop()