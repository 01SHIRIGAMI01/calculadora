import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x650")
        self.root.configure(bg="#2e2e2e")
        self.historial = []

        # Entrada de texto
        self.entrada = tk.Entry(self.root, font=("Arial", 24), bd=0, insertwidth=2, width=18, borderwidth=4, 
                                justify="right", bg="#1e1e1e", fg="white")
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Crear botones
        self.crear_botones()

    def crear_botones(self):
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("C", 5, 0), ("√", 5, 1), ("^", 5, 2), ("Hist", 5, 3),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("%", 6, 3)
        ]

        for texto, fila, columna in botones:
            color_boton = "#333" if texto in "1234567890." else "#555"
            tk.Button(self.root, text=texto, padx=20, pady=20, font=("Arial", 16), bg=color_boton, fg="white",
                      activebackground="#777", activeforeground="white", borderwidth=0, 
                      command=lambda t=texto: self.click_boton(t)).grid(row=fila, column=columna, padx=5, pady=5)

    def click_boton(self, texto):
        if texto == "C":
            self.entrada.delete(0, tk.END)
        elif texto == "=":
            try:
                expresion = self.entrada.get()
                resultado = eval(expresion)
                self.historial.append(f"{expresion} = {resultado}")
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
            except Exception:
                messagebox.showerror("Error", "Expresión inválida")
        elif texto == "√":
            try:
                valor = float(self.entrada.get())
                if valor < 0:
                    raise ValueError("Raíz negativa")
                resultado = math.sqrt(valor)
                self.historial.append(f"√{valor} = {resultado}")
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
            except Exception:
                messagebox.showerror("Error", "Número inválido")
        elif texto == "Hist":
            messagebox.showinfo("Historial", "\n".join(self.historial) if self.historial else "Sin historial")
        elif texto == "sin":
            self._operacion_trigonometrica(math.sin, "sin")
        elif texto == "cos":
            self._operacion_trigonometrica(math.cos, "cos")
        elif texto == "tan":
            self._operacion_trigonometrica(math.tan, "tan")
        elif texto == "^":
            self.entrada.insert(tk.END, "**")
        else:
            self.entrada.insert(tk.END, texto)

    def _operacion_trigonometrica(self, funcion, nombre):
        try:
            angulo = float(self.entrada.get())
            resultado = funcion(math.radians(angulo))
            self.historial.append(f"{nombre}({angulo}) = {resultado}")
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, resultado)
        except Exception:
            messagebox.showerror("Error", "Ángulo inválido")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
 