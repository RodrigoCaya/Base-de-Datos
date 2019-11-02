<?php

$db = pg_connect("host=localhost port=8080 dbname=tarea2 user=postgres password=caya") or die ('Error de conexión.');

if ($db){
    echo "Connected to ". pg_host($db);
}

else {
    echo "Error in connecting to database.";
}

?>
