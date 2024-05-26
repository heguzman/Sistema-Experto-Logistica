import tkinter as tk
from tkinter import messagebox

from SE_Disponibilidad_Personal import define_SE_Disponibilidad_Personal
from SE_Pedido import define_SE_Pedido
from SE_Tiempo_De_Entrega import define_SE_Tiempo_De_Entrega

def ejecutar_SE_Logistica():
    # Inicio los valores
    # Inventario 30
    inventario_value = float(entry_numero1.get())
    # Demanda 80
    demanda_value = float(entry_numero2.get())
    # Capacidad Almacen 80
    capacidad_alamacen_value = float(entry_numero3.get())

    #Obtengo el valor del pedido
    pedido_value = define_SE_Pedido(inventario_value, demanda_value)

    #Obtengo el valor de la disponibilidad del personal
    disp_personal_value = define_SE_Disponibilidad_Personal(pedido_value, capacidad_alamacen_value)

    #Obtengo el tiempo de entrega
    tiempo_entrega_value = define_SE_Tiempo_De_Entrega(disp_personal_value, demanda_value)

    #Imprimo el resultado
    label_resultado.config(text=f"Resultado: \n\n\nPedido: {pedido_value:.2f}\n\nDisponibilidad Personal: {disp_personal_value:.2f}\n\nTiempo Entrega: {tiempo_entrega_value:.2f}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto Logistica")
ventana.geometry("400x400")

# Etiqueta y campo de entrada para el primer número
label_numero1 = tk.Label(ventana, text="Ingrese el valor del inventario:")
label_numero1.pack(pady=5)
entry_numero1 = tk.Entry(ventana)
entry_numero1.pack(pady=5)

# Etiqueta y campo de entrada para el segundo número
label_numero2 = tk.Label(ventana, text="Ingrese el valor de la demanda:")
label_numero2.pack(pady=5)
entry_numero2 = tk.Entry(ventana)
entry_numero2.pack(pady=5)

# Etiqueta y campo de entrada para el segundo número
label_numero3 = tk.Label(ventana, text="Ingrese el valor de la capacidad del almacen:")
label_numero3.pack(pady=5)
entry_numero3 = tk.Entry(ventana)
entry_numero3.pack(pady=5)

# Botón para realizar la suma
boton_SE = tk.Button(ventana, text="Ejecutar Sist Exp", command=ejecutar_SE_Logistica)
boton_SE.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack(pady=5)

ventana.mainloop()



