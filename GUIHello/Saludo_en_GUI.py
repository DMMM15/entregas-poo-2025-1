
import tkinter as tk
from tkinter import messagebox

class AplicacionSaludo:
    def __init__(self):
        # Ventana raíz
        self.ventana = tk.Tk()
        self.ventana.title("Saludo con Tkinter")
        self.ventana.geometry("450x550")
        self.ventana.configure(bg="#e6f7ff")

        # Frame principal para organizar mejor
        self.frame = tk.Frame(self.ventana, bg="#e6f7ff")
        self.frame.pack(expand=True)

        # Mensaje decorativo de Bienvenida
        self.titulo = tk.Label(self.frame, text="¡Bienvenido!", font=("Arial", 30, "bold"), bg="#e6f7ff", fg="#007acc")
        self.titulo.pack(pady=10)

        # Etiqueta de entrada
        self.etiqueta = tk.Label(self.frame, text="Ingresa tu nombre:", bg="#e6f7ff", font=("Arial", 12))
        self.etiqueta.pack(pady=5)

        # Entrada de texto
        self.entrada = tk.Entry(self.frame, font=("Arial", 12), width=25)
        self.entrada.pack(pady=5)

        # Botón Saludar
        self.boton_saludo = tk.Button(self.frame, text="Saludar", command=self.saludar,
                                      bg="#87f351", font=("Arial", 11), width=15)
        self.boton_saludo.pack(pady=10)

        # Botón Salir
        self.boton_salir = tk.Button(self.frame, text="Salir", command=self.ventana.quit,
                                     bg="#e01d1d", font=("Arial", 11), width=15)
        self.boton_salir.pack()

        # Iniciar bucle de la ventana
        self.ventana.mainloop()

    def saludar(self):
        nombre = self.entrada.get().strip()

        # Validación: nombre no vacío y sin números
        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")
        elif any(char.isdigit() for char in nombre):
            messagebox.showerror("Error", "El nombre no debe contener números.")
        else:
            messagebox.showinfo("Saludo", f"Hola {nombre}!")

if __name__ == "__main__":
    app = AplicacionSaludo()
