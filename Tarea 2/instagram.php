
<?php
require 'conexion.php';
$nombre = $_POST['name'];
$user= $_POST['user'];
$pass = $_POST['pass'];
$email = $_POST['mail'];
echo $db;
$query=pg_query_params("INSERT INTO usuarios VALUES (default,$1,$2,$3,0,0,0,0,0,$4)",array($email,$nombre,$user,$pass));



if ($query){
    echo "Te has registrado correctamente";
}
else{
    $error = pg_last_error($db);
    if (preg_match('/duplicada/i',$error)){
        echo "Ya existe un usuario con ese nombre, escoge otro.";
    }
}
