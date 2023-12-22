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

$dataDir = 'data';

if (!is_dir($dataDir)) {
    mkdir($dataDir, 0777, true);
}

$fileName = date('Ymd-His') . '-' . rand(100,999) . ".txt";

while (is_file($dataDir . '/' . $fileName)) {
    $fileName = date('Ymd-His') . '-' . rand(100, 999) . ".txt";
}

file_put_contents($dataDir . '/' . $fileName,
    'имя: ' . $_POST['name'] . "\n"
    . 'фамилия: ' . $_POST['surname'] . "\n"
    . 'email: ' . $_POST['email'] . "\n"
    . 'номер телефона: ' . $_POST['num'] . "\n"
    . 'тема конференции: ' . $_POST['theme'] . "\n"
    . 'метод оплаты: ' . $_POST['payment'] . "\n"
    . 'рассылка: ' . $_POST['subscr']);

header ('Location: thanks.php');