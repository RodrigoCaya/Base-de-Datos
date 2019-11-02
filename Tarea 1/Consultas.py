import pyodbc

#Ingresar un juego a la vista
def create(conexion):
    cursor = conexion.cursor()
    nombre = input("\nIngrese el nombre: ")
    genero = input("\nIngrese el genero: ")
    desarrollador = input("\nIngrese el desarrollador: ")
    publicador = input("\nIngrese el publicador: ")
    fecha = input("Ingrese la fecha de estreno (YYYY/MM/DD): ")
    exclusividad = input("\nIngrese exclusividad (Si/No): ")
    rating = int(input("\nIngrese rating (0-10): "))
    precio = int(input("\nIngrese el precio: "))
    ventas_globales = int(input("\nIngrese ventas globales: "))
    stock = int(input("\nIngrese stock en tienda: "))
    bodega = input("\nIngrese stock en bodega: ")
    cursor.execute(f"""
        INSERT INTO Sansando(NOMBRE, GENERO, DESARROLLADOR, PUBLICADOR, FECHA_DE_ESTRENO,
        EXCLUSIVIDAD, RATING, PRECIO, VENDIDOS, VENTAS_GLOBALES, STOCK, BODEGA)
        VALUES('{nombre}', '{genero}', '{desarrollador}', '{publicador}', TO_DATE('{fecha}','YYYY/MM/DD'), '{exclusividad}',
        '{rating}', '{precio}', 0, '{ventas_globales}', '{stock}', '{bodega}');
        """)
    cursor.commit()

#Leer una cantidad de juegos de la vista
def read(conexion,cantidad):
    cont = 0
    cursor = conexion.cursor()
    i = 0
    while(i < cantidad):
        id = input("\nIngrese ID del juego:\n")
        cursor.execute(f"select * from Sansando WHERE ID = {id};")
        for row in cursor:
            cont += 1
            row[5] = str(row[5]).split(' ')
            row[5] = row[5][0]
            print(f"ID = {row[0]}")
            print(f"Nombre = {row[1]}")
            print(f"Genero = {row[2]}")
            print(f"Desarrollador = {row[3]}")
            print(f"Publicador = {row[4]}")
            print(f"Fecha de estreno = {row[5]}")
            print(f"Exclusividad = {row[6]}")
            print(f"Rating = {row[7]}/10")
            print(f"Precio = {row[8]}")
            print(f"Vendidos = {row[9]}")
            print(f"Ventas Globales = {row[10]}")
            print(f"Stock = {row[11]}")
            print(f"Bodega = {row[12]}")
        if(cont == 0):
            print("\nNo existe un juego con ese ID.")
            i -= 1
        i += 1
        conexion.commit()

def update(conexion):
    opcion3 = -1
    cont = 0
    id = int(input("\nIngrese la ID del juego a actualizar: "))
    cursor = conexion.cursor()
    cursor.execute(f"select * from Sansando WHERE ID = {id};")
    cursor.commit()
    for row in cursor:
        cont += 1
    if(cont == 0):
        print("\nNo existe un juego con ese ID.")
    else:
        while (opcion3 != 0):
            print("\nIngrese el número de la opción que desea:")
            print("--------------------------------------------------------------------------------")
            print("| 1. Nombre                                                                    |")
            print("| 2. Genero                                                                    |")
            print("| 3. Desarrollador                                                             |")
            print("| 4. Publicador                                                                |")
            print("| 5. Fecha de estreno                                                          |")
            print("| 6. Exclusividad                                                              |")
            print("| 7. Rating                                                                    |")
            print("| 8. Precio                                                                    |")
            print("| 9. Vendidos                                                                  |")
            print("| 10. Ventas Globales                                                          |")
            print("| 11. Stock                                                                    |")
            print("| 12. Bodega                                                                   |")
            print("| 0. Volver                                                                    |")
            print("--------------------------------------------------------------------------------")
            opcion3 = int(input())
            if (opcion3 == 1):
                valor = input("Ingrese el nuevo nombre: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    NOMBRE = '{valor}'
                    WHERE ID = {id};
                """)
                cursor.commit()

            elif (opcion3 == 2):
                valor = input("Ingrese el nuevo genero: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    GENERO = '{valor}'
                    WHERE ID = {id}
                """
                )
                cursor.commit()

            elif (opcion3 == 3):
                valor = input("Ingrese el nuevo desarrollador: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    DESARROLLADOR = '{valor}'
                    WHERE ID = {id};
                """)
                cursor.commit()

            elif (opcion3 == 4):
                valor = input("Ingrese el nuevo publicador: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    PUBLICADOR = '{valor}'
                    WHERE ID = {id};
                """)
                cursor.commit()

            elif (opcion3 == 5):
                valor = input("Ingrese la nueva fecha de estreno (YYYY/MM/DD): ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    FECHA_DE_ESTRENO = TO_DATE('{valor}','YYY/MM/DD')
                    WHERE ID = {id};
                """)
                cursor.commit()

            elif (opcion3 == 6):
                valor = input("Ingrese la nueva exclusividad (Si/No): ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    EXCLUSIVIDAD = '{valor}'
                    WHERE ID = {id};
                """)

                cursor.commit()
            elif (opcion3 == 7):
                valor = input("Ingrese el nuevo rating [0-10]: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    RATING = '{valor}'
                    WHERE ID = {id}
                """
                )
                cursor.commit()

            elif (opcion3 == 8):
                valor = input("Ingrese el nuevo precio: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    PRECIO = '{valor}'
                    WHERE ID = {id}
                """
                )
                cursor.commit()

            elif (opcion3 == 9):
                valor = input("Ingrese la nueva cantidad de vendidos localmente: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    VENDIDOS = '{valor}'
                    WHERE ID = {id}
                """
                )
                cursor.commit()

            elif (opcion3 == 10):
                valor = input("Ingrese la nueva cantidad de ventas globales: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    VENTAS_GLOBALES = '{valor}'
                    WHERE ID = {id}
                """
                )
                cursor.commit()

            elif (opcion3 == 11):
                valor = input("Ingrese el nuevo stock: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    STOCK = '{valor}'
                    WHERE ID = {id}
                """
                )
                cursor.commit()

            elif (opcion3 == 12):
                valor = input("Ingrese el nuevo stock en bodega: ")
                cursor = conexion.cursor()
                cursor.execute(
                f"""
                    UPDATE Sansando SET
                    BODEGA = '{valor}'
                    WHERE ID = {id}
                """
                )
                cursor.commit()

            elif(opcion3 != 0):
                print("\nOpcion ingresada no valida")

#Borrar una cantidad de juegos de la vista
def delete(connexion,cantidad):
    cursor = conexion.cursor()
    i = 0
    while(i < cantidad):
        cont = 0
        id = int(input("\nIngrese el ID del juego que desea borrar: "))
        cursor.execute(f"select * from Sansando WHERE ID = {id};")
        cursor.commit()
        for row in cursor:
            cont += 1
        if(cont == 0):
            print("\nNo existe un juego con ese ID.")
        else:
            i += 1
            cursor.execute(
            f"""
                DELETE FROM Sansando WHERE ID = {id};
            """)
            cursor.commit()


#Crear la vista del join entre las dos tablas
def view(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE OR REPLACE VIEW Sansando AS
        SELECT Nintendo.ID, Sansanoplay.NOMBRE, Nintendo.GENERO, Nintendo.DESARROLLADOR, Nintendo.PUBLICADOR,
        Nintendo.FECHA_DE_ESTRENO, Nintendo.EXCLUSIVIDAD, Nintendo.RATING, Sansanoplay.PRECIO, Sansanoplay.VENDIDOS, Nintendo.VENTAS_GLOBALES,
        Sansanoplay.STOCK, Sansanoplay.BODEGA
        FROM Sansanoplay
        INNER JOIN Nintendo
        ON Nintendo.ID = Sansanoplay.ID;
        """
    )
    conexion.commit()

#Vista de los 5 juegos mejores valorados
def top_view(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        """
            CREATE OR REPLACE VIEW top_view AS
            SELECT NOMBRE, PRECIO FROM
                (SELECT NOMBRE, PRECIO FROM Sansando
                WHERE EXCLUSIVIDAD = 'Si'
                ORDER BY PRECIO DESC)
            WHERE ROWNUM <= 5;
        """)
    cursor.commit()

#Vista de los 3 generos más vendidos
def top_selled_view(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        """
            CREATE OR REPLACE VIEW top_selled_view AS
            SELECT GENERO, VENDIDOS, VENTAS_GLOBALES FROM
                (SELECT GENERO, VENDIDOS, VENTAS_GLOBALES
                FROM  Sansando ORDER BY VENDIDOS+VENTAS_GLOBALES DESC)
            WHERE ROWNUM <= 3;
        """)
    cursor.commit()

#Vista de las 3 desarrolladoras con más ventas
def top_developers_view(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        """
            CREATE OR REPLACE VIEW top_developers_view AS
            SELECT DESARROLLADOR, VENDIDOS FROM
                (SELECT DESARROLLADOR, VENDIDOS FROM Sansando
                ORDER BY VENDIDOS DESC)
            WHERE ROWNUM <= 3;
        """)
    cursor.commit()

#Vista con los juegos mejores valorados
def top_rating_view(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        """
            CREATE OR REPLACE VIEW top_rating_view AS
            SELECT NOMBRE, FECHA_DE_ESTRENO, RATING
            FROM Sansando ORDER BY RATING DESC;
        """)
    cursor.commit()

#----------------Triggers------------------#

#Trigger insert Sansando
def create_t(conexion):
    cursor = conexion.cursor()
    cursor.execute(
    """
        CREATE OR REPLACE TRIGGER createTrigger
        INSTEAD OF INSERT ON Sansando
        FOR EACH ROW BEGIN
            INSERT INTO Sansanoplay(NOMBRE, PRECIO, STOCK, BODEGA, VENDIDOS)
            VALUES(:new.NOMBRE, :new.PRECIO, :new.STOCK, :new.BODEGA, :new.VENDIDOS);
            INSERT INTO Nintendo(NOMBRE, GENERO, DESARROLLADOR, PUBLICADOR, FECHA_DE_ESTRENO, EXCLUSIVIDAD, VENTAS_GLOBALES, RATING)
            VALUES(:new.NOMBRE, :new.GENERO, :new.DESARROLLADOR, :new.PUBLICADOR, :new.FECHA_DE_ESTRENO, :new.EXCLUSIVIDAD, :new.VENTAS_GLOBALES, :new.RATING);
        END;
    """)
    cursor.commit()

#Trigger update Sansando
def update_t(conexion):
    cursor = conexion.cursor()
    cursor.execute(
    """
        CREATE OR REPLACE TRIGGER updateTrigger
        INSTEAD OF UPDATE ON Sansando
        FOR EACH ROW BEGIN
            UPDATE Sansanoplay SET
            NOMBRE = :new.NOMBRE,
            PRECIO = :new.PRECIO,
            STOCK = :new.STOCK,
            BODEGA = :new.BODEGA,
            VENDIDOS = :new.VENDIDOS
            WHERE ID = :new.ID;

            UPDATE Nintendo SET
            NOMBRE = :new.NOMBRE,
            GENERO = :new.GENERO,
            DESARROLLADOR = :new.DESARROLLADOR,
            PUBLICADOR = :new.PUBLICADOR,
            FECHA_DE_ESTRENO = :new.FECHA_DE_ESTRENO,
            EXCLUSIVIDAD = :new.EXCLUSIVIDAD,
            VENTAS_GLOBALES = :new.VENTAS_GLOBALES,
            RATING = :new.RATING
            WHERE ID = :new.ID;
        END;
    """)
    cursor.commit()

#Trigger delete Sansando
def delete_t(conexion):
    cursor = conexion.cursor()
    cursor.execute(
    """
        CREATE OR REPLACE TRIGGER deleteTrigger
        INSTEAD OF DELETE ON Sansando
        FOR EACH ROW BEGIN
            DELETE FROM Sansanoplay WHERE ID = :old.ID;
            DELETE FROM Nintendo WHERE ID = :old.ID;
        END;
    """)
    cursor.commit()


#----------------------------------------------------#

conexion = pyodbc.connect(
    'Driver={Oracle in XE};'
    'DBQ=[dbq];'
    'Uid=SYSTEM;'
    'Pwd=[Contraseña]')

cursor=conexion.cursor()
view(conexion)
top_view(conexion)
top_developers_view(conexion)
top_selled_view(conexion)
top_rating_view(conexion)
create_t(conexion)
update_t(conexion)
delete_t(conexion)

#menu
opcion=-1
while(opcion!=0):
    print("\nIngrese el número de la opción que desea:")
    print("--------------------------------------------------------------------------------")
    print("| 1. Los 5 exclusivos más caros                                               |")
    print("| 2. Los 3 géneros más vendidos                                               |")
    print("| 3. Las 3 desarrolladoras con más ventas locales                             |")
    print("| 4. Los juegos con mejor rating                                              |")
    print("| 5. Vender juegos                                                            |")
    print("| 6. CRUD                                                                     |")
    print("| 0. Salir                                                                    |")
    print("--------------------------------------------------------------------------------")
    opcion=int(input())
    cursor = conexion.cursor()
    if(opcion==1):
        print("\nLos 5 exclusivos más caros son:\n")
        cursor.execute(
        """
        SELECT * from top_view;
        """
        )
        for row in cursor:
            print(f"Nombre = {row[0]}   Precio = {row[1]}")
        cursor.commit()

    elif(opcion==2):
        print("\nLos 3 géneros más vendidos son:\n")
        cursor.execute(
        """
        SELECT * from top_selled_view
        """
        )
        for row in cursor:
            ventas = row[1] + row[2]
            print(f"Genero = {row[0]}   Ventas Totales = {ventas}")
        cursor.commit()

    elif(opcion==3):
        print("\nLas 3 desarrolladoras con más ventas locales son:\n")
        cursor.execute(
        """
        SELECT * FROM top_developers_view;
        """
        )
        for row in cursor:
            print(f"Desarrollador = {row[0]}   Ventas locales = {row[1]}")

        cursor.commit()

    elif(opcion==4):
        print("\nLos juegos con mejor rating son:\n")
        cursor.execute(
        "SELECT * FROM top_rating_view;"
        )
        cont = 0
        max_rating = 0
        for row in cursor:
            row[1] = str(row[1]).split(' ')
            row[1] = row[1][0]
            if(cont == 0):
                cont += 1
                max_rating = row[2]
                print(f"Nombre = {row[0]}   Fecha de Estreno = {row[1]}   Rating = {max_rating}/10")
            else:
                if(max_rating > row[2]):
                    cont = -1
                else:
                    print(f"Nombre = {row[0]}   Fecha de Estreno = {row[1]}   Rating = {max_rating}/10")
            if(cont == -1):
                break
        cursor.commit()

    elif(opcion==5):
        cont = 0
        id = input("Ingrese el ID del juego a vender: ")
        cursor = conexion.cursor()
        cursor.execute(f"select * from Sansando WHERE ID = {id};")
        cursor.commit()
        for row in cursor:
            cont += 1
        if(cont == 0):
            print("\nNo existe un juego con ese ID.")
        else:
            cantidad = int(input("Ingrese la cantidad de copias a vender: "))
            cursor.execute(
            f"""
                SELECT VENDIDOS, STOCK, BODEGA FROM Sansando WHERE ID = {id};
            """
            )
            conexion.commit()
            for row in cursor:
                cont = 0
                vendidos = int(row[0])
                stock = int(row[1])
                bodega = int(row[2])
                if(stock < cantidad):
                    if(bodega < cantidad - stock):
                        print("\n|||No es posible realizar la venta.|||")
                        cont += 1
                    else:
                        bodega -= (cantidad - stock)
                        stock = 0
                        vendidos += cantidad
                        print("\nSe realizó la venta exitosamente.")

                else:
                    stock -= cantidad
                    vendidos += cantidad
                    print("\nSe realizó la venta exitosamente.")
                if(stock < 10):
                    if(bodega >= 10- stock):
                        bodega -= (10 - stock)
                        stock = 10
                    elif(cont == 0):
                        print("\n|||No se puede reponer completamente.|||")
                cursor.execute(
                f"""
                    UPDATE Sansando
                    SET VENDIDOS = {vendidos}, STOCK = {stock}, BODEGA = {bodega}
                    WHERE ID = {id};
                """
                )
                conexion.commit()
                break

    elif(opcion == 6):
        opcion2 = -1
        while(opcion2 != 0):
            print("\nIngrese el número de la opción que desea:")
            print("--------------------------------------------------------------------------------")
            print("| 1. Crear                                                                    |")
            print("| 2. Leer                                                                     |")
            print("| 3. Actualizar                                                               |")
            print("| 4. Borrar                                                                   |")
            print("| 0. Volver al menú principal                                                 |")
            print("--------------------------------------------------------------------------------")
            opcion2=int(input())
            if(opcion2 == 1):
                create(conexion)

            elif(opcion2 == 2):
                cantidad = int(input("Ingrese la cantidad de juegos que quiere leer: "))
                read(conexion,cantidad)

            elif(opcion2 == 3):
                update(conexion)

            elif(opcion2 == 4):
                cantidad = int(input("Ingrese la cantidad de juegos que quiere eliminar: "))
                delete(conexion,cantidad)

            elif(opcion2 != 0):
                print("\nOpcion ingresada no valida")

    elif(opcion != 0):
        print("\nOpcion ingresada no valida")


conexion.close()
