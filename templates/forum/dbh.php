<?php
    $servername = "localhost";
    $dbUsername = "root";
    $dbPassword = "plmokn12";
    $dbName = "flaskapp";

    //connecting to database
    $connection = mysqli_connect($servername, $dbUsername, $dbPassword, $dbName);
            
    //error message if connection fails
    if(!$connection){
        die("Connection failed: ".mysqli_connect_error());
    }
?>