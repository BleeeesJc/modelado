import tkinter as tk
from tkinter import ttk, messagebox
import random

def simular():
    try:
        horas = int(entry_horas.get())
        sims = int(entry_sims.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos en los campos numéricos.")
        return

    tabla_resultados.delete(*tabla_resultados.get_children())

    total_clientes = 0
    total_articulos = 0
    probs = []
    for child in tabla_prob.get_children():
        valores = tabla_prob.item(child, "values")
        try:
            probs.append(float(valores[1]))
        except ValueError:
            messagebox.showerror("Error", "Las probabilidades deben ser numéricas.")
            return

    if abs(sum(probs) - 1.0) > 0.001:
        messagebox.showerror("Error", "Las probabilidades deben sumar 1.")
        return

    articulos = [0, 1, 2, 3]
    limites = [sum(probs[:i+1]) for i in range(len(probs))]

    for sim in range(1, sims + 1):
        clientes_totales = 0
        articulos_totales = 0

        for hora in range(1, horas + 1):
            clientes = random.uniform(0, 1)
            llegadas = int(random.uniform(0, 4))
            clientes_totales += llegadas

            articulos_hora = 0
            for _ in range(llegadas):
                r = random.random()
                for i, limite in enumerate(limites):
                    if r <= limite:
                        articulos_hora += articulos[i]
                        break

            articulos_totales += articulos_hora
            tabla_resultados.insert("", "end", values=(sim, hora, llegadas, articulos_hora))

        total_clientes += clientes_totales
        total_articulos += articulos_totales

    prom_clientes = total_clientes / sims
    prom_articulos = total_articulos / sims
    lbl_resultados.config(
        text=f"RESULTADOS PROMEDIO\n\nPromedio Clientes Totales: {prom_clientes:.2f}\nPromedio Artículos Vendidos: {prom_articulos:.2f}"
    )

def limpiar():
    entry_horas.delete(0, tk.END)
    entry_horas.insert(0, "10")
    entry_sims.delete(0, tk.END)
    entry_sims.insert(0, "5")
    tabla_resultados.delete(*tabla_resultados.get_children())
    lbl_resultados.config(text="Resultados aparecerán aquí.")

def editar_celda(event):
    item = tabla_prob.identify_row(event.y)
    col = tabla_prob.identify_column(event.x)
    if col != "#2" or not item:
        return

    x, y, width, height = tabla_prob.bbox(item, "Probabilidad")
    valor_actual = tabla_prob.item(item, "values")[1]
    entry_edit = tk.Entry(tabla_prob)
    entry_edit.place(x=x, y=y, width=width, height=height)
    entry_edit.insert(0, valor_actual)
    entry_edit.focus()

    def guardar(event):
        nuevo = entry_edit.get()
        tabla_prob.set(item, "Probabilidad", nuevo)
        entry_edit.destroy()

    entry_edit.bind("<Return>", guardar)
    entry_edit.bind("<FocusOut>", lambda e: entry_edit.destroy())

ventana = tk.Tk()
ventana.title("Simulación de Llegadas de Clientes")
ventana.geometry("800x650")
ventana.config(bg="#102542")

titulo = tk.Label(
    ventana,
    text="🛒 Simulación de Llegadas de Clientes a una Tienda",
    font=("Segoe UI", 18, "bold"),
    bg="#102542",
    fg="white"
)
titulo.pack(pady=15)

frame_param = tk.LabelFrame(ventana, text="Parámetros", bg="#102542", fg="white", font=("Segoe UI", 11, "bold"))
frame_param.pack(padx=20, pady=10, fill="x")

tk.Label(frame_param, text="Horas a simular:", bg="#102542", fg="white").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_horas = tk.Entry(frame_param, width=10, justify="center")
entry_horas.grid(row=0, column=1, padx=10, pady=8)
entry_horas.insert(0, "10")

tk.Label(frame_param, text="Número de simulaciones:", bg="#102542", fg="white").grid(row=0, column=2, padx=10, pady=8, sticky="e")
entry_sims = tk.Entry(frame_param, width=10, justify="center")
entry_sims.grid(row=0, column=3, padx=10, pady=8)
entry_sims.insert(0, "5")

frame_prob = tk.LabelFrame(ventana, text="Distribución de Artículos Comprados", bg="#102542", fg="white", font=("Segoe UI", 11, "bold"))
frame_prob.pack(padx=20, pady=10, fill="x")

tabla_prob = ttk.Treeview(frame_prob, columns=("Artículos", "Probabilidad"), show="headings", height=4)
tabla_prob.heading("Artículos", text="Artículos")
tabla_prob.heading("Probabilidad", text="Probabilidad")
tabla_prob.column("Artículos", anchor="center", width=100)
tabla_prob.column("Probabilidad", anchor="center", width=100)
tabla_prob.pack(pady=5)

tabla_prob.insert("", "end", values=("0", "0.2"))
tabla_prob.insert("", "end", values=("1", "0.3"))
tabla_prob.insert("", "end", values=("2", "0.4"))
tabla_prob.insert("", "end", values=("3", "0.1"))

tabla_prob.bind("<Double-1>", editar_celda)

frame_botones = tk.Frame(ventana, bg="#102542")
frame_botones.pack(pady=15)

btn_simular = tk.Button(frame_botones, text="▶ Simular", command=simular, bg="#1D72B8", fg="white", width=15, height=2)
btn_simular.grid(row=0, column=0, padx=10)

btn_limpiar = tk.Button(frame_botones, text="🔄 Limpiar", command=limpiar, bg="#6C757D", fg="white", width=15, height=2)
btn_limpiar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="✖ Salir", command=ventana.destroy, bg="#C82333", fg="white", width=15, height=2)
btn_salir.grid(row=0, column=2, padx=10)

frame_tabla = tk.LabelFrame(ventana, text="Resultados", bg="#102542", fg="white", font=("Segoe UI", 11, "bold"))
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

columnas = ("Sim", "Hora", "Clientes", "Artículos Vendidos")
tabla_resultados = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
for col in columnas:
    tabla_resultados.heading(col, text=col)
    tabla_resultados.column(col, anchor="center", width=150)
tabla_resultados.pack(fill="both", expand=True)

lbl_resultados = tk.Label(
    ventana,
    text="Resultados aparecerán aquí.",
    bg="#102542",
    fg="white",
    font=("Segoe UI", 10, "bold")
)
lbl_resultados.pack(pady=10)

ventana.mainloop()
