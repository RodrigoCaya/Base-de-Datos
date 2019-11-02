<!DOCTYPE html>
<html>

<head>
    <link href="instagram-icon.png" rel="icon">
<title>
Instagram
</title>
</head>
<body class="StyleBackground1">
    <link rel="stylesheet" href="styles.css">
<div class="StyleCaja1">
    <img src="instagram2.png" class="StyleImagenIg" >
    <p class=StyleLetra1> Regístrate para ver fotos y videos de tus amigos. </p>
    <form action="instagram.php" method="POST">
        <input class="StyleCaja3" type="text" placeholder="Número de celular o correo electronico" name="mail" /><br />
        <input class="StyleCaja3" type="text" placeholder="Nombre completo" name="name" /><br />
        <input class="StyleCaja3" type="text" placeholder="Nombre de usuario" name="user" /><br />
        <input class="StyleCaja3" type="password" placeholder="Contraseña" name="pass" /><br />
        <input class="StyleCaja3" type="submit" action="instagram.php" value="Registrarte" name="enviar" />
    </form>
</div>

<div class="StyleCaja2">

</div>
</body>

</html>


<?php
    function crearUsuarios($conexion, $id )
    {
        $sql = "DELETE FROM Usuarios";
        // Si 'id' es diferente de 'null' sólo se borra la persona con el 'id' especificado:
        if( $id != null )
            $sql .= " WHERE id=".$id;
        // Ejecutamos la consulta (se devolverá true o false):
         return pg_query( $conexion, $sql );
    }
?>

<?php
    function borrarPersona( $conexion, $id )
    {
        $sql = "DELETE FROM Usuarios";
        // Si 'id' es diferente de 'null' sólo se borra la persona con el 'id' especificado:
        if( $id != null )
            $sql .= " WHERE id=".$id;
        // Ejecutamos la consulta (se devolverá true o false):
         return pg_query( $conexion, $sql );
    }
?>

<?php
    function insertarPersona( $conexion, $id, $nombre )
    {
        $sql = "INSERT INTO Usuarios VALUES (".$id.", '".$nombre."')";
        // Ejecutamos la consulta (se devolverá true o false):
         return pg_query( $conexion, $sql );
    }
?>

<?php
    function modificarPersona( $conexion, $id, $nombre )
    {
        $sql = "UPDATE Usuarios SET nombre='".$nombre."' WHERE id=".$id;
        // Ejecutamos la consulta (se devolverá true o false):
         return pg_query( $conexion, $sql );
    }
?>

<?php
    function listarPersonas( $conexion )
    {
        $sql = "SELECT * FROM Usuarios ORDER BY id";
        $ok = true;
        // Ejecutar la consulta:
         $rs = pg_query( $conexion, $sql );
        if( $rs )
        {
            // Obtener el número de filas:
             if( pg_num_rows($rs) > 0 )
            {
                echo "<p/>LISTADO DE PERSONAS<br/>";
                echo "===================<p />";
                // Recorrer el resource y mostrar los datos:
                 while( $obj = pg_fetch_object($rs) )
                     echo $obj->id." - ".$obj->nombre."<br />";
            }
            else
                echo "<p>No se encontraron personas</p>";
        }
        else
            $ok = false;
        return $ok;
    }
?>

<?php
    function buscarPersona( $conexion, $id )
    {
        $sql = "SELECT * FROM Usuarios WHERE id=".$id."";
        $devolver = null;
        // Ejecutar la consulta:
        $rs = pg_query( $conexion, $sql );
        if( $rs )
        {
            // Si se encontró el registro, se obtiene un objeto en PHP con los datos de los campos:
             if( pg_num_rows($rs) > 0 )
                 $devolver = pg_fetch_object( $rs, 0 );
        }
        return $devolver;
    }
?>