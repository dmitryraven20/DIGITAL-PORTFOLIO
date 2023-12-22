<?php

//echo $_POST['theme'];
//echo '<br>';
//echo $_POST['type'];
//echo '<br>';
//echo $_POST['place'];
//echo '<br>';
//echo $_POST['date'];
//echo '<br>';
//echo $_POST['time'];
//echo '<br>';
//echo $_POST['length'];
//echo '<br>';
//echo $_POST['comment'];
//echo '<br>';

if (getenv('REQUEST_METHOD')==='POST') {
    
    $theme = strip_tags($_POST["theme"]);
    $type = strip_tags($_POST["type"]);
    $place = strip_tags($_POST["place"]);
    $date = strip_tags($_POST["date"]);
    $time = strip_tags($_POST["time"]);
    $length = strip_tags($_POST["length"]);
    $comment = strip_tags($_POST["comment"]);
    
    error_reporting(E_ALL);
    ini_set('display_errors', 1);

    $hostname="localhost";
    $db="tdlist";
    $username="root";
    $password = "";
    
    $conn = new PDO(
        "mysql:host=localhost;dbname=$db",
        $username,
        $password
    );
    
    if($conn) {
        echo("Связь есть");
    } else {
        die("Ошибка - нет связи с БД");
    }
    
    $sql = "INSERT INTO todolist (type, theme, place, date, time, length, comment) 
    VALUES ('$theme','$type','$place','$date','$time','$length','$comment')";
    echo $sql;
    
    if ($conn->query($sql)) {
        echo "Данные добавлены";
    } else {
        echo "Ошибка добавления данных";
    }
    header ('Location: thanks.php');
}
?>