import sqlite3

# Conectar a la base de datos o crear una nueva si no existe
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear tabla de usuarios si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL)''')

# Insertar un usuario de ejemplo
username = "Neo"
password = "123"
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Usuario creado exitosamente.")