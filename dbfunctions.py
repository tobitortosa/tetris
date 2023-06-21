import sqlite3


def create_table_players():
    with sqlite3.connect("data.db") as conexion:
        try:
            sentence = """ create table jugadores 
                            (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT NOT NULL UNIQUE,
                                puntaje INTEGER DEFAULT 0
                            )
                        """
            conexion.execute(sentence)
            print("Se creo la table jugadores")

        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")


def create_player(name):
    with sqlite3.connect("data.db") as conexion:
        try:
            conexion.execute("insert into jugadores (nombre) values (?)", [name])
            conexion.commit()

        except sqlite3.OperationalError:
            print("Error")


def get_players():
    with sqlite3.connect("data.db") as conexion:
        final_list = []
        cursor = conexion.execute("SELECT * FROM jugadores")

        for element in cursor:
            lista_element = list(element)
            lista_element.reverse()
            final_list.append(lista_element)

    final_list.sort(key=lambda x: x[0])
    final_list.reverse()

    return final_list


def update_puntaje_by_name(points, name):
    with sqlite3.connect("data.db") as conexion:
        cursor = conexion.execute("SELECT * FROM jugadores")

        for fila in cursor:
            lista = list(fila)
            print(lista)
            if lista[1] == name:
                id = lista[0]

        sentence = "UPDATE jugadores SET puntaje=? WHERE id=?"

        conexion.execute(
            sentence,
            (
                points,
                str(id),
            ),
        )
