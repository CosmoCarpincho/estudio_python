# Importación de Tkinter
import tkinter as tk

# Creción y configuración de la ventana
ventana = tk.Tk()
ventana.title("Python: Interfaces gráficas")
ventana.geometry("500x300")


# Creamos una fuente persoanlizada
fuente_personalizada = ("Roboto", 36, "bold")

# label -> Etiqueta
# funciona bg en vez de backgorund
# foreground -> fg ; color de la letra
# borderwidth -> border -> bd ; para borde
etiqueta = tk.Label(text="Hola que tal",
                    background="lightgreen",
                    fg="red",
                    bd=25,
                    cursor="hand2",
                    state=tk.DISABLED,
                    disabledforeground="sky blue",
                    font=fuente_personalizada)

# Muestra la etiqueta en la ventana
etiqueta.pack()

ventana.mainloop()