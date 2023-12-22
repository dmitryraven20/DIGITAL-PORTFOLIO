<?php

//echo $_POST['name'];
//echo '<br>';
//echo $_POST['surname'];
//echo '<br>';
//echo $_POST['email'];
//echo '<br>';
//echo $_POST['num'];
//echo '<br>';
//echo $_POST['theme'];
//echo '<br>';
//echo $_POST['payment'];
//echo '<br>';
//
//var_dump($_POST['subscr']);
//echo '<br>';

$name = $_POST['name'];
$surname = $_POST['surname'];
$email = $_POST['email'];
    
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


file_put_contents('userz.txt',
    'имя: ' . $_POST['name'] . " || "
    . 'фамилия: ' . $_POST['surname'] . " || "
    . 'email: ' . $_POST['email'] . " || "
    . 'номер телефона: ' . $_POST['num'] . " || "
    . 'тема конференции: ' . $_POST['theme'] . " || "
    . 'метод оплаты: ' . $_POST['payment'] . " || "
    . 'рассылка: ' . $_POST['subscr'] . " || "
    . 'дата подачи заявки: ' . date('Y-m-d H:i') . " || "
    . 'ip заявителя: ' . $_SERVER['REMOTE_ADDR'] . " \n" ,
    FILE_APPEND | LOCK_EX);

header ('Location: thanks.php');