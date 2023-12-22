<?php

$name = $_POST['name'];
$surname = $_POST['surname'];
$email = $_POST['email'];
$num = $_POST['num'];
$theme = $_POST['theme'];
$paym = $_POST['payment'];
$subscr =  $_POST['subscr'];
$regdate = date('Y-m-d H:i');
$ip = $_SERVER['REMOTE_ADDR'];
    
if (preg_match('~[\\\/:*?"\'<>|]~', $name))
{
    echo "Недопустимые символы";
    exit;
}    
if (preg_match('~[\\\/:*?"\'<>|]~', $surname))
{
    echo "Недопустимые символы";
    exit;
}
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
    
$sql = "INSERT INTO confer (`name`, `surname`, `email`, `phone number`, `theme`, `payment type`, `subscription`, `registration date`, `user ip`) 
VALUES ('$name','$surname','$email','$num','$theme','$paym','$subscr','$regdate','$ip')";
echo $sql;
    
if ($conn->query($sql)) {
    echo "Данные добавлены";
} else {
    echo "Ошибка добавления данных";
}
        
header ('Location: thanks.php');