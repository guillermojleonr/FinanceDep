import sqlite3

miConexion = sqlite3.connect("finance") #Si no existe la base de datos la crea
miCursor = miConexion.cursor() 

""" ----------------- DDL ----------------------"""

miCursor.execute(""" 
     CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR(50),
        measure_unit VARCHAR(10),
        value_clp DOUBLE(20)
        ) 
    """)

miCursor.execute(""" 
     CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR(50)
        ) 
    """)

miCursor.execute(""" 
     CREATE TABLE IF NOT EXISTS product_details(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id.product INTEGER,
        id.item INTEGER,
        quantity INTEGER,
        value DOUBLE,
        FOREIGN KEY (id.product) REFERENCES products(id),
        FOREIGN KEY (id.item) REFERENCES items(id)
        ) 
    """)

""" ------------------ DML ---------------------"""

""" Insert single element """

miCursor.execute("""
     INSERT INTO items VALUES(
        'Disco de circonio',
        'gramos',
        100)
     """)

""" Insert many elements """
# items
variosProductos = [
    ('Disco de cromo cobalto', 'gramos', 200),
    ('Hora-Hombre', 'minuto', 185.18),
    ('Hora-Maquina', 'minuto', 500),
    ('Aditivos de fibra', 'gramos', 30)
]
miCursor.executemany("INSERT INTO items VALUES(NULL,?,?,?.?)",variosProductos)

# products
variosProductos = [
    ('Diente de circonio'),
    ('Diente de cromo')
]
miCursor.executemany("INSERT INTO items VALUES(NULL,?)",variosProductos)

""" Select elements """
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'JUGUETERIA'") #SQL is case sensitive
productos=miCursor.fetchall() #Stores in a variable the result of the query in tuples
print(productos) #Prints on console.

""" Update elements """
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE nombre_articulo = 'CAMISETA'")

""" Delete elements """
miCursor.execute("DELETE FROM PRODUCTOS WHERE codigo_articulo = 1")
miConexion.commit()


miConexion.close()