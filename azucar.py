import tkinter as tk
from tkinter import ttk, messagebox
import random
import math


def simular():
    try:
        dias_sim = int(entry_dias.get())
        if dias_sim <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido de días (entero positivo).")
        return

    tabla_resultados.delete(*tabla_resultados.get_children())

    try:
        capacidad_bodega = float(tabla_info.item(tabla_info.get_children()[0])['values'][1])
        costo_orden = float(tabla_info.item(tabla_info.get_children()[1])['values'][1])
        costo_inventario = float(tabla_info.item(tabla_info.get_children()[2])['values'][1])
        costo_adquisicion = float(tabla_info.item(tabla_info.get_children()[3])['values'][1])
        precio_venta = float(tabla_info.item(tabla_info.get_children()[4])['values'][1])
        media_demanda = float(tabla_info.item(tabla_info.get_children()[5])['values'][1])
    except ValueError:
        messagebox.showerror("Error", "Los valores de la tabla deben ser numéricos.")
        return

    dias_revision = 7
    inventario = capacidad_bodega
    pedido_en_curso = 0
    dias_entrega = 0

    costo_total = 0
    demanda_insatisfecha = 0
    ingresos = 0

    for dia in range(1, dias_sim + 1):
        if dias_entrega > 0:
            dias_entrega -= 1
        if dias_entrega == 0 and pedido_en_curso > 0:
            inventario += pedido_en_curso
            pedido_en_curso = 0
        demanda = round(-media_demanda * math.log(1 - random.random()))
        if demanda <= inventario:
            ventas = demanda
            inventario -= demanda
            faltante = 0
        else:
            ventas = inventario
            faltante = demanda - inventario
            demanda_insatisfecha += faltante
            inventario = 0

        ingresos += ventas * precio_venta
        costo_total += inventario * costo_inventario

        pedido = 0
        if dia % dias_revision == 0 and pedido_en_curso == 0:
            pedido = capacidad_bodega - inventario
            if pedido > 0:
                pedido_en_curso = pedido
                dias_entrega = random.randint(1, 3)
                costo_total += costo_orden + pedido * costo_adquisicion

        tabla_resultados.insert(
            "", "end",
            values=(dia, demanda, ventas, faltante, round(inventario,2), pedido, round(costo_total, 2))
        )
    ganancia_neta = ingresos - costo_total
    lbl_resultados.config(
        text=(
            f"RESULTADOS FINALES\n\n"
            f"Costo Total: {costo_total:.2f} Bs\n"
            f"Demanda Insatisfecha Total: {demanda_insatisfecha:.2f} Kg\n"
            f"Ingresos Totales: {ingresos:.2f} Bs\n"
            f"Ganancia Neta: {ganancia_neta:.2f} Bs"
        )
    )

def limpiar():
    entry_dias.delete(0, tk.END)
    entry_dias.insert(0, "60")
    tabla_resultados.delete(*tabla_resultados.get_children())
    lbl_resultados.config(text="Resultados aparecerán aquí.")
    valores_iniciales = [
        ("Capacidad de Bodega (Kg)", "700"),
        ("Costo de Orden (Bs/orden)", "100"),
        ("Costo de Inventario (Bs/kg)", "0.1"),
        ("Costo de Adquisición (Bs/kg)", "3.5"),
        ("Precio de Venta (Bs/kg)", "5"),
        ("Demanda Media (Kg/día)", "100"),
    ]
    for i, val in enumerate(valores_iniciales):
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
ventana.title("Simulación de Inventario de Azúcar")
ventana.geometry("950x680")
ventana.config(bg="#EAF0F6")

titulo = tk.Label(
    ventana,
    text="SIMULACIÓN DE INVENTARIO - DISTRIBUCIÓN EXPONENCIAL",
    font=("Segoe UI", 18, "bold"),
    bg="#EAF0F6",
    fg="#1E3A8A"
)
titulo.pack(pady=10)

frame_param = tk.LabelFrame(
    ventana, text="Parámetros de Simulación", bg="#EAF0F6",
    font=("Segoe UI", 11, "bold"), fg="#1E3A8A"
)
frame_param.pack(pady=10, padx=20, fill="x")

tk.Label(frame_param, text="Número de días a simular:", bg="#EAF0F6", font=("Segoe UI", 10)).grid(
    row=0, column=0, padx=10, pady=5, sticky="e"
)
entry_dias = tk.Entry(frame_param, width=10)
entry_dias.grid(row=0, column=1, padx=5, pady=5)
entry_dias.insert(0, "60")

tk.Button(frame_param, text="SIMULAR", bg="#2563EB", fg="white", width=14, height=1,
          font=("Segoe UI", 10, "bold"), command=simular).grid(row=0, column=2, padx=15)
tk.Button(frame_param, text="LIMPIAR", bg="#DC2626", fg="white", width=14, height=1,
          font=("Segoe UI", 10, "bold"), command=limpiar).grid(row=0, column=3, padx=15)
tk.Button(frame_param, text="SALIR", bg="#6B7280", fg="white", width=14, height=1,
          font=("Segoe UI", 10, "bold"), command=ventana.destroy).grid(row=0, column=4, padx=15)

frame_info = tk.LabelFrame(ventana, text="Parámetros del Sistema", bg="#EAF0F6",
                           font=("Segoe UI", 11, "bold"), fg="#1E3A8A")
frame_info.pack(padx=20, pady=10, fill="x")

tabla_info = ttk.Treeview(frame_info, columns=("Concepto", "Valor"), show="headings", height=6)
tabla_info.heading("Concepto", text="Concepto")
tabla_info.heading("Valor", text="Valor")
tabla_info.column("Concepto", width=320, anchor="center")
tabla_info.column("Valor", width=150, anchor="center")

valores_iniciales = [
    ("Capacidad de Bodega (Kg)", "700"),
    ("Costo de Orden (Bs/orden)", "100"),
    ("Costo de Inventario (Bs/kg)", "0.1"),
    ("Costo de Adquisición (Bs/kg)", "3.5"),
    ("Precio de Venta (Bs/kg)", "5"),
    ("Demanda Media (Kg/día)", "100"),
]
for val in valores_iniciales:
    tabla_info.insert("", "end", values=val)

tabla_info.pack(padx=15, pady=5)
tabla_info.bind("<Double-1>", editar_celda)

frame_tabla = tk.LabelFrame(ventana, text="Resultados Diarios", bg="#EAF0F6",
                             font=("Segoe UI", 11, "bold"), fg="#1E3A8A")
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

columnas = ("Día", "Demanda", "Ventas", "Faltante", "Inventario", "Pedido", "Costo Acum (Bs)")
tabla_resultados = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
for col in columnas:
    tabla_resultados.heading(col, text=col)
    tabla_resultados.column(col, width=120, anchor="center")
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
