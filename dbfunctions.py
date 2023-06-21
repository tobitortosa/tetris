import sqlite3


def create_table_jugadores():
    with sqlite3.connect("data.db") as conexion:
        try:
            sentencia = """ create table jugadores 
                            (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT NOT NULL UNIQUE,
                                puntaje INTEGER DEFAULT 0
                            )
                        """
            conexion.execute(sentencia)
            print("Se creo la table jugadores")

        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")


def create_jugador(nombre):
    with sqlite3.connect("data.db") as conexion:
        try:
            conexion.execute("insert into jugadores (nombre) values (?)", [nombre])
            conexion.commit()

        except sqlite3.OperationalError:
            print("Error")


def get_jugadores():
    with sqlite3.connect("data.db") as conexion:
        lista = []

        cursor = conexion.execute("SELECT * FROM jugadores")

        for fila in cursor:
            lista_fila = list(fila)
            lista_fila.reverse()
            lista.append(lista_fila)

    sorted(lista, key=lambda jugador: jugador[1])

    lista.reverse()

    print(lista)

    return lista


def update_puntaje_by_name(puntaje, nombre):
    with sqlite3.connect("data.db") as conexion:
        cursor = conexion.execute("SELECT * FROM jugadores")

        for fila in cursor:
            lista = list(fila)
            for element in lista:
                if element == nombre:
                    lista[2] = puntaje

        sentencia = "UPDATE jugadores SET puntaje=? WHERE id=?"

        conexion.execute(
            sentencia,
            (
                puntaje,
                str(lista[0]),
            ),
        )
