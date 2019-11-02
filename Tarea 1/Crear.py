import pyodbc
import csv
from random import randrange as rand
from random import choice

#Crea el Trigger de la Id Serial SansanoPlay
def SerialIdSansanoplay(conexion):
    cursor = conexion.cursor()
    cursor.execute("CREATE SEQUENCE SerialS START WITH 1;")
    cursor.execute("""CREATE OR REPLACE TRIGGER SerialIdSansanoPlay
    BEFORE INSERT ON SansanoPlay
    FOR EACH ROW BEGIN
        SELECT SerialS.NEXTVAL
        INTO :new.ID
        FROM dual;
    END;""")
    cursor.commit()

#Crea el Trigger de la Id Serial Nintendo
def SerialIdNintendo(conexion):
    cursor = conexion.cursor()
    cursor.execute("CREATE SEQUENCE SerialN START WITH 1;")
    cursor.execute("""CREATE OR REPLACE TRIGGER SerialIdNintendo
    BEFORE INSERT ON Nintendo
    FOR EACH ROW BEGIN
        SELECT SerialN.NEXTVAL
        INTO :new.ID
        FROM dual;
    END;""")
    cursor.commit()

#Borra el Trigger de la Id Serial Nintendo
def borrarSequenceSerialN(conexion):
    cursor = conexion.cursor()
    cursor.execute("DROP SEQUENCE SerialN;")
    cursor.commit()

#Borra el Trigger de la Id Serial SansanoPlay
def borrarSequenceSerialS(conexion):
    cursor = conexion.cursor()
    cursor.execute("DROP SEQUENCE SerialS;")
    cursor.commit()

#Borra la tabla Nintendo
def borrarNintendo(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        "DROP TABLE Nintendo")
    cursor.commit()

#Borra la tabla SansanoPlay
def borrarSansanoplay(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        "DROP TABLE Sansanoplay")
    cursor.commit()

#Crea tabla Nintendo
def crearNintendo(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE Nintendo(
            ID INTEGER,
            NOMBRE VARCHAR2(128),
            GENERO VARCHAR2(128),
            DESARROLLADOR VARCHAR2(128),
            PUBLICADOR VARCHAR2(128),
            FECHA_DE_ESTRENO DATE,
            EXCLUSIVIDAD VARCHAR2(2),
            VENTAS_GLOBALES INTEGER,
            RATING INTEGER );
            """
        )
    cursor.commit()

#Crea tabla SansanoPlay
def crearSansanoplay(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE Sansanoplay(
            ID INTEGER,
            NOMBRE VARCHAR2(128),
            PRECIO INTEGER,
            STOCK INTEGER,
            BODEGA INTEGER,
            VENDIDOS INTEGER );
            """
    )
    cursor.commit()

#Define la id como PK en SansanoPlay
def primary_key1(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
                    ALTER TABLE SansanoPlay
                    ADD CONSTRAINT id_pk PRIMARY KEY (ID);
                    """)
    cursor.commit()

#Define la id como PK en Nintendo
def primary_key2(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
                    ALTER TABLE Nintendo
                    ADD CONSTRAINT id_pk2 PRIMARY KEY (ID);
                    """)
    cursor.commit()

#Reemplaza los trimestres por fechas reales
def rellenarFechas(row):
    fecha = row[5].split(' ')
    year = fecha[1].strip()
    dia = 15
    if (fecha[0] == 'Q1'):
        mes = 'February'
    if (fecha[0] == 'Q2'):
        mes = 'May'
    if (fecha[0] == 'Q3'):
        mes = 'August'
    if (fecha[0] == 'Q4'):
        mes = 'November'
    tupla = (year,mes,dia)
    return tupla

#Convierte los meses en números
def conversionMes(mes):
    if (mes == 'January'):
        mes = "01"
    if (mes == 'February'):
        mes = "02"
    if (mes == 'March'):
        mes = "03"
    if (mes == 'April'):
        mes = "04"
    if (mes == 'May'):
        mes = "05"
    if (mes == 'June'):
        mes = "06"
    if (mes == 'July'):
        mes = "07"
    if (mes == 'August'):
        mes = "08"
    if (mes == 'September'):
        mes = "09"
    if (mes == 'October'):
        mes = "10"
    if (mes == 'November'):
        mes = "11"
    if (mes == 'December'):
        mes = "12"
    return mes

#Rellena con los juegos la tabla Nintendo
def rellenarNintendo(conexion):
    line_count = 0
    cursor = conexion.cursor()
    with open('Nintendo.csv','r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if (line_count == 0):
                print('Cargando...')
                line_count += 1
            else:
                if (row[5][0] == 'Q'):
                    (year,mes,dia) = rellenarFechas(row)
                elif(',' not in row[5]):
                    fecha = row[5].split(' ')
                    mes = fecha[0]
                    year = fecha[1]
                    dia = 15
                else:
                    fecha = row[5].split(',')
                    year = fecha[1].strip()
                    fecha = fecha[0].split(' ')
                    dia = fecha[1]
                    mes = fecha[0]
                mes = conversionMes(mes)
                fecha = year+'-'+mes+'-'+str(dia)
                if(rand(50) == 0):
                    rating = 10
                else:
                    rating = rand(9) + 1
                ventas_globales = rand(100000)
                row[1] = row[1].replace("'","`")
                row[2] = row[2].replace("'","`")#generos como beat 'em up
                row[3] = row[3].replace("'","`")
                row[4] = row[4].replace("'","`")
                cursor.execute(
                    f"""
                        INSERT INTO Nintendo (NOMBRE,GENERO,DESARROLLADOR,PUBLICADOR,FECHA_DE_ESTRENO,EXCLUSIVIDAD,VENTAS_GLOBALES,RATING)
                        VALUES ('{row[1]}','{row[2]}','{row[3]}','{row[4]}',TO_DATE('{fecha}','YYYY/MM/DD'),'{row[6]}','{ventas_globales}','{rating}');
                    """
                    )
                cursor.commit()

#Rellena con los juego la tabla SansanoPlay
def rellenarSansanoplay(conexion):
    line_count = 0
    cursor = conexion.cursor()
    with open('Sansanoplay.csv','r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if (line_count == 0):
                print('Cargando...')
                line_count += 1
            else:
                precio = choice([9990, 10990, 11990, 12990, 13990,14990, 17990, 19990, 24990, 29990, 34990, 39990, 44990])
                stock = 20
                vendidos = rand(100)
                bodega = 180 - vendidos
                row[1] = row[1].replace("'","`")
                cursor.execute(
                    f"""
                        INSERT INTO Sansanoplay (NOMBRE,PRECIO,STOCK,BODEGA,VENDIDOS)
                        VALUES ('{row[1]}','{precio}','{stock}','{bodega}','{vendidos}');
                    """
                    )
                cursor.commit()

#Creacion del join SansandoT entre las dos tablas
def crearSansandoT(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE SansandoT AS
        SELECT Nintendo.ID, Sansanoplay.NOMBRE, Nintendo.GENERO, Nintendo.DESARROLLADOR, Nintendo.PUBLICADOR,
        Nintendo.FECHA_DE_ESTRENO, Nintendo.EXCLUSIVIDAD, Nintendo.RATING, Sansanoplay.PRECIO, Sansanoplay.VENDIDOS, Nintendo.VENTAS_GLOBALES,
        Sansanoplay.STOCK, Sansanoplay.BODEGA
        FROM Sansanoplay
        INNER JOIN Nintendo
        ON Nintendo.ID = Sansanoplay.ID;
        """
    )
    conexion.commit()

#Eliminacion del join SansandoT
def borrarSansandoT(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        "DROP TABLE SansandoT")
    cursor.commit()


conexion = pyodbc.connect(
    'Driver={Oracle in XE};'
    'DBQ=[dbq];'
    'Uid=SYSTEM;'
    'Pwd=[Contraseña]')


#borrarNintendo(conexion)               #FUNCION DE BORRADO (DESCOMENTAR SI SE DESEA USAR EL CODIGO MÁS VECES)
#borrarSansanoplay(conexion)            #FUNCION DE BORRADO (DESCOMENTAR SI SE DESEA USAR EL CODIGO MÁS VECES)

crearNintendo(conexion)
crearSansanoplay(conexion)

primary_key1(conexion)
primary_key2(conexion)

#borrarSequenceSerialN(conexion)         #FUNCION DE BORRADO (DESCOMENTAR SI SE DESEA USAR EL CODIGO MÁS VECES)
#borrarSequenceSerialS(conexion)         #FUNCION DE BORRADO (DESCOMENTAR SI SE DESEA USAR EL CODIGO MÁS VECES)

SerialIdNintendo(conexion)
SerialIdSansanoplay(conexion)

rellenarNintendo(conexion)
rellenarSansanoplay(conexion)

#borrarSansandoT(conexion)              #FUNCION DE BORRADO (DESCOMENTAR SI SE DESEA USAR EL CODIGO MÁS VECES)
crearSansandoT(conexion)

print('Tablas creadas correctamente.')

conexion.close()
