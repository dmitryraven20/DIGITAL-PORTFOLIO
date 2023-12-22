<?php

if(isset($_POST["id"]))
{
        
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
    
    $sql2 = "DELETE FROM todolist WHERE id = :rid;";
    echo 'id' . $_POST['id'];
    $sdt = $conn->prepare($sql2);
//    $sdt->bindValue(":rid", $_POST["id"]);
    $sdt->execute(["rid" => $_POST["id"]]);
    
    if($conn->query($sql2)){
        header('Location: index.php');
    }
    else{
        die("Ошибка: ");
    } 
}
?>