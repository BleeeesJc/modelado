import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

def simular():
    try:
        n_sim = int(entry_sims.get())
        n_dias = int(entry_dias.get())
        precio_huevo = float(entry_phuevo.get())
        precio_pollo = float(entry_ppollo.get())
        media = float(entry_media.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
        return

    tabla_resultados.delete(*tabla_resultados.get_children())

    total_ingreso = 0
    total_huevos = 0
    total_pollos = 0
    total_rotos = 0

    prob_roto = float(tabla1.item(tabla1.get_children()[0])['values'][1])
    prob_pollo = float(tabla1.item(tabla1.get_children()[1])['values'][1])
    prob_huevo = float(tabla1.item(tabla1.get_children()[2])['values'][1])

    prob_muere = float(tabla2.item(tabla2.get_children()[0])['values'][1])
    prob_sobrevive = float(tabla2.item(tabla2.get_children()[1])['values'][1])

    for sim in range(1, n_sim + 1):
        ingreso = 0
        huevos_vendidos = 0
        pollos_vivos = 0
        huevos_rotos = 0

        for _ in range(n_dias):
            L = math.exp(-media)
            k = 0
            p = 1
            while p > L:
                k += 1
                p *= random.random()
            n_huevos = k - 1

            for _ in range(n_huevos):
                r = random.random()
                if r < prob_roto:
                    huevos_rotos += 1
                elif r < prob_roto + prob_pollo:
                    r2 = random.random()
                    if r2 >= prob_muere:
                        pollos_vivos += 1
                        ingreso += precio_pollo
                else:
                    huevos_vendidos += 1
                    ingreso += precio_huevo

        tabla_resultados.insert(
            "",
            "end",
            values=(sim, f"{ingreso:.2f}", huevos_rotos, huevos_vendidos, pollos_vivos),
        )

        total_ingreso += ingreso
        total_huevos += huevos_vendidos
        total_pollos += pollos_vivos
        total_rotos += huevos_rotos

    ingreso_prom = total_ingreso / n_sim
    ingreso_dia = ingreso_prom / n_dias
    prom_huevos = total_huevos / n_sim
    prom_pollos = total_pollos / n_sim
    prom_rotos = total_rotos / n_sim

    lbl_resultados.config(
        text=(
            f"PROMEDIO DE RESULTADOS\n"
            f"Ingreso Bruto Promedio: ${ingreso_prom:.2f}\n"
            f"Ingreso Promedio por Día: ${ingreso_dia:.2f}\n"
            f"Nº Promedio de Huevos Rotos: {prom_rotos:.2f}\n"
            f"Nº Promedio de Pollos Vivos: {prom_pollos:.2f}\n"
            f"Nº Promedio de Huevos Vendidos: {prom_huevos:.2f}"
        )
    )

def limpiar():
    for entry in [entry_sims, entry_dias, entry_phuevo, entry_ppollo, entry_media]:
        entry.delete(0, tk.END)
    entry_sims.insert(0, "5")
    entry_dias.insert(0, "300")
    entry_phuevo.insert(0, "2")
    entry_ppollo.insert(0, "30")
    entry_media.insert(0, "2")
    tabla_resultados.delete(*tabla_resultados.get_children())
    lbl_resultados.config(text="Resultados de la simulación aparecerán aquí.")

def editar_celda(event, tabla):
    item = tabla.identify_row(event.y)
    columna = tabla.identify_column(event.x)

    if not item or columna == "#0":
        return

    col_index = int(columna.replace("#", "")) - 1
    valor_actual = tabla.item(item, "values")[col_index]

    x, y, ancho, alto = tabla.bbox(item, columna)

    entry_edit = tk.Entry(tabla, justify="center")
    entry_edit.place(x=x, y=y, width=ancho, height=alto)
    entry_edit.insert(0, valor_actual)
    entry_edit.focus()

    def guardar_edicion(event):
        nuevo_valor = entry_edit.get()
        valores = list(tabla.item(item, "values"))
        valores[col_index] = nuevo_valor
        tabla.item(item, values=valores)
        entry_edit.destroy()

    entry_edit.bind("<Return>", guardar_edicion)
    entry_edit.bind("<FocusOut>", lambda e: entry_edit.destroy())

ventana = tk.Tk()
ventana.title("Simulación de Gallina Ponedora de Huevos")
ventana.geometry("900x720")
ventana.config(bg="#1E3A5F")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="🥚 SIMULACIÓN DE EVENTOS DISCRETOS",
    font=("Segoe UI", 20, "bold"),
    bg="#1E3A5F",
    fg="#FFFFFF",
)
titulo.pack(pady=15)

linea = tk.Frame(ventana, height=3, bg="#4A90E2", width=400)
linea.pack()

subtitulo = tk.Label(
    ventana,
    text="Gallina Ponedora de Huevos",
    font=("Segoe UI", 12),
    bg="#1E3A5F",
    fg="#A8C5E2",
)
subtitulo.pack(pady=(5, 15))

frame_param = tk.LabelFrame(
    ventana, 
    text="  Parámetros de la Simulación  ", 
    bg="#2A4A6F", 
    font=("Segoe UI", 11, "bold"), 
    fg="#FFFFFF",
    bd=0,
    relief="flat"
)
frame_param.pack(pady=10, padx=20, fill="x")

campos = [
    ("Número de Simulaciones:", entry_sims := tk.Entry(frame_param, width=12, font=("Segoe UI", 10), justify="center"), "5"),
    ("Número de Días:", entry_dias := tk.Entry(frame_param, width=12, font=("Segoe UI", 10), justify="center"), "300"),
    ("Precio Venta Huevo ($):", entry_phuevo := tk.Entry(frame_param, width=12, font=("Segoe UI", 10), justify="center"), "2"),
    ("Precio Venta Pollo ($):", entry_ppollo := tk.Entry(frame_param, width=12, font=("Segoe UI", 10), justify="center"), "30"),
    ("Media (λ) huevos/día:", entry_media := tk.Entry(frame_param, width=12, font=("Segoe UI", 10), justify="center"), "2"),
]
for i, (label_text, entry, default_val) in enumerate(campos):
    row = i // 2
    col = (i % 2) * 2
    
    tk.Label(
        frame_param, 
        text=label_text, 
        bg="#2A4A6F", 
        fg="#D4E3F0",
        font=("Segoe UI", 10)
    ).grid(row=row, column=col, padx=10, pady=8, sticky="e")
    
    entry.grid(row=row, column=col+1, padx=10, pady=8, sticky="w")
    entry.insert(0, default_val)
frame_prob = tk.LabelFrame(
    ventana, 
    text="  Probabilidades del Sistema  ", 
    bg="#2A4A6F", 
    font=("Segoe UI", 11, "bold"), 
    fg="#FFFFFF",
    bd=0,
    relief="flat"
)
frame_prob.pack(pady=10, padx=20, fill="x")
contenedor_tablas = tk.Frame(frame_prob, bg="#2A4A6F")
contenedor_tablas.pack(pady=10, padx=10)

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

tabla1 = ttk.Treeview(contenedor_tablas, columns=("Fin", "Prob"), show="headings", height=3, style="Custom.Treeview")
tabla1.heading("Fin", text="Finalidad del Huevo")
tabla1.heading("Prob", text="Probabilidad")
tabla1.column("Fin", width=200, anchor="center")
tabla1.column("Prob", width=100, anchor="center")
tabla1.insert("", "end", values=("Roto", "0.2"))
tabla1.insert("", "end", values=("Pollo", "0.3"))
tabla1.insert("", "end", values=("Permanece Huevo", "0.5"))
tabla1.grid(row=0, column=0, padx=10, pady=5)

tabla2 = ttk.Treeview(contenedor_tablas, columns=("Destino", "Prob"), show="headings", height=2, style="Custom.Treeview")
tabla2.heading("Destino", text="Destino del Pollo")
tabla2.heading("Prob", text="Probabilidad")
tabla2.column("Destino", width=200, anchor="center")
tabla2.column("Prob", width=100, anchor="center")
tabla2.insert("", "end", values=("Muere", "0.2"))
tabla2.insert("", "end", values=("Sobrevive", "0.8"))
tabla2.grid(row=0, column=1, padx=10, pady=5)

tabla1.bind("<Double-1>", lambda e: editar_celda(e, tabla1))
tabla2.bind("<Double-1>", lambda e: editar_celda(e, tabla2))

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


frame_tabla = tk.LabelFrame(
    ventana, 
    text="  Resultados de Simulaciones  ", 
    bg="#2A4A6F", 
    font=("Segoe UI", 11, "bold"), 
    fg="#FFFFFF",
    bd=0,
    relief="flat"
)
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)


columnas = ("Sim", "Ingreso", "Huevos Rotos", "Huevos Vendidos", "Pollos Vivos")
tabla_resultados = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=5, style="Custom.Treeview")
for col in columnas:
    tabla_resultados.heading(col, text=col)
    tabla_resultados.column(col, width=150, anchor="center")
tabla_resultados.pack(fill="both", expand=True, pady=10, padx=10)


lbl_resultados = tk.Label(
    ventana,
    text="Resultados de la simulación aparecerán aquí.",
    bg="#1E3A5F",
    justify="left",
    font=("Segoe UI", 10),
    fg="#D4E3F0",
)
lbl_resultados.pack(pady=10)

ventana.mainloop()