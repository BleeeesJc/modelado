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
ventana.geometry("850x650")
ventana.config(bg="#EAF0F6")

titulo = tk.Label(
    ventana,
    text="SIMULACIÓN DE EVENTOS DISCRETOS - JUEGO DE DADOS",
    font=("Segoe UI", 18, "bold"),
    bg="#EAF0F6",
    fg="#1E3A8A"
)
titulo.pack(pady=10)

frame_param = tk.LabelFrame(
    ventana, text="Parámetros del Juego", bg="#EAF0F6",
    font=("Segoe UI", 11, "bold"), fg="#1E3A8A"
)
frame_param.pack(pady=10, padx=20, fill="x")

tk.Label(frame_param, text="Número de Juegos:", bg="#EAF0F6", font=("Segoe UI", 10)).grid(
    row=0, column=0, padx=10, pady=5, sticky="e"
)
entry_juegos = tk.Entry(frame_param, width=10)
entry_juegos.grid(row=0, column=1, padx=5, pady=5)
entry_juegos.insert(0, "10")

tk.Button(frame_param, text="SIMULAR", bg="#2563EB", fg="white", width=14, height=1,
           font=("Segoe UI", 10, "bold"), command=simular).grid(row=0, column=2, padx=15)
tk.Button(frame_param, text="LIMPIAR", bg="#DC2626", fg="white", width=14, height=1,
           font=("Segoe UI", 10, "bold"), command=limpiar).grid(row=0, column=3, padx=15)
tk.Button(frame_param, text="SALIR", bg="#6B7280", fg="white", width=14, height=1,
           font=("Segoe UI", 10, "bold"), command=ventana.destroy).grid(row=0, column=4, padx=15)

frame_info = tk.LabelFrame(ventana, text="Parámetros del Sistema", bg="#EAF0F6",
                            font=("Segoe UI", 11, "bold"), fg="#1E3A8A")
frame_info.pack(padx=20, pady=10, fill="x")

tabla_info = ttk.Treeview(frame_info, columns=("Concepto", "Valor"), show="headings", height=3)
tabla_info.heading("Concepto", text="Concepto")
tabla_info.heading("Valor", text="Valor (Bs.)")
tabla_info.column("Concepto", width=250, anchor="center")
tabla_info.column("Valor", width=100, anchor="center")
tabla_info.insert("", "end", values=("Costo del juego (jugador paga)", "2"))
tabla_info.insert("", "end", values=("Pérdida de la casa si gana jugador", "5"))
tabla_info.insert("", "end", values=("Ganancia inicial de la casa", "0"))
tabla_info.pack(padx=15, pady=5)

tabla_info.bind("<Double-1>", editar_celda)

frame_tabla = tk.LabelFrame(ventana, text="Resultados de los Lanzamientos", bg="#EAF0F6",
                             font=("Segoe UI", 11, "bold"), fg="#1E3A8A")
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

columnas = ("Juego", "Dado1", "Dado2", "Suma", "Ganador", "GananciaCasa")
tabla_resultados = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
for col in columnas:
    tabla_resultados.heading(col, text=col)
    tabla_resultados.column(col, width=130, anchor="center")
tabla_resultados.pack(fill="both", expand=True, pady=5)

lbl_resultados = tk.Label(
    ventana,
    text="Resultados aparecerán aquí.",
    bg="#EAF0F6",
    justify="left",
    font=("Segoe UI", 10, "bold"),
    fg="#1E3A8A",
)
lbl_resultados.pack(pady=15)

ventana.mainloop()
