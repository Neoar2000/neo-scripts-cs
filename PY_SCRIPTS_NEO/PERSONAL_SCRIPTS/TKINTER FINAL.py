import tkinter as tk
import sqlite3

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Verificar credenciales en la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user is not None:
        # Iniciar sesión exitosamente
        print("Inicio de sesión exitoso")
        # Aquí puedes abrir una nueva ventana o realizar otras acciones después del inicio de sesión
    else:
        # Credenciales incorrectas
        print("Credenciales incorrectas")

# Crear ventana de inicio de sesión
root = tk.Tk()
root.title("Sistema Contable de Ventas")

# Crear campos de entrada
label_username = tk.Label(root, text="Usuario:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Crear botón de inicio de sesión
btn_login = tk.Button(root, text="Iniciar sesión", command=login)
btn_login.pack()

root.mainloop()