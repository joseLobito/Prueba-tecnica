
import sqlite3
from sqlite3 import Error


class MetodosBD():

    def __init__(self):
        try:
            self.conexion = sqlite3.connect("BD/base_de_datos.db")
        except Exception as e:
            print(f'ocurrio el error: {e}')
    def abrir(self):
        self.conexion = sqlite3.connect("BD/base_de_datos.db")
        self.cursor = self.conexion.cursor()
    def cerrar(self):
        self.conexion.close()

    def crear_tabla(self):
        try:
            self.abrir()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tabla (id INTEGER PRIMARY KEY AUTOINCREMENT, region TEXT, country TEXT, language TEXT, time REAL)")
            self.conexion.commit()
        except Exception as e:
            print(f'Ocurrio el error: {e} creando tabla')
            
        finally:
            self.cerrar()
    def insertar_datos(self,dato):
        try:
            self.abrir()
            self.cursor.execute(f"INSERT INTO tabla (region, country, language, time) VALUES (?, ?, ? ,?)", dato)
            self.conexion.commit()
        except Exception as e:
            print(f'Ocurrio el error {e} insertando datos')
        finally:
            self.cerrar()
        
    def mostrar_datos(self):
        try:
            self.abrir()
            self.cursor.execute(f'SELECT * FROM tabla')
            columnas = self.cursor.fetchall()
            return columnas
        except Exception as e:
            print(f"Ocurrio el error: {e} mostrando datos")
        finally:
            self.cerrar()


if __name__=='__main__':
    
    db = MetodosBD()
    filas = ['America','Colombia','español','123']
    db.crear_tabla()
    for i in filas:
        db.insertar_datos(i)

# Se muestra la tabla

    print("----------- Tabla de sqlite ----------------")
    for i in db.mostrar_datos():
        print(i)