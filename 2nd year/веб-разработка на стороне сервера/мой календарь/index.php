<!DOCTYPE html>

<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Мой календарь</title>
    </head>
    <style>
        body {
            text-align: center;
            font-size: 16px;
            font-family: fantasy;
            background-color:darkslategray;
        }
        h1 {
            font-size: 30px;
        }
        h2 {
            font-size: 25px;
        }
        p {
            padding-top: 0px;
        }
        .put {
            width: 500px;
            font-size: 20px;
            border-radius: 10px;
            border: 2px solid dimgray;
        }
        .put1 {
            width: 190px;
        }
        .put2 {
            height: 100px;
            overflow: scroll;
        }
        .padd {
            margin-right: 20px;
        }
        .phon {
            position: absolute;
            background-color: white;
            width: 700px;
            height: 770px;
            border-radius: 35px;
            border: 3px solid black;
            left: 33%;
        }
        .phon1 {
            margin-top: 780px;
        }
        button {
            font-size: 20px;
            height: 60px;
            width: 250px;
            border-radius: 10px;
        }
        table {
            left: 5%;
            position: absolute;
            width: 90%;
            align-self: center;
            overflow: scroll;
            border-radius: 5px;
            border: 2px solid dimgray;
        }
        td {
            font-family: century gothic;
            border-radius: 5px;
            border: 2px solid dimgray;
        }
    </style>
    <body>
        <div class='phon'>
        <h1>Календарик</h1>
        <h2>Новая задача</h2>
        <form action="tabl.php" method="post">
            <p> Тема: <p><input type="text" name="theme" class='put' required>
            <p> Тип:  <p><select name="type"  class='put' required>
                <option>Встреча</option>
                <option>Звонок</option>
                <option>Совещание</option>
                <option>Дело</option>
            </select>
            <p> Место: <p><input type="text" name="place" class='put'>
            <p> Дата и время: <p><input type="date" name="date" class='put put1 padd' required><input type="time" name="time" class='put put1'>
            <p> Длительность: <p><input type="text" name="length" class='put'>
            <p> Комментарий: <p><textarea name="comment" class='put put2'></textarea>
            
            <p> <button type="submit">Добавить</button>
        </form>
        </div>
        <div class='phon phon1'>
            <h2>Список задач</h2>
            
<!--
            <table name="export_table">
                <tr>
                    <th>Тип</th>
                    <th>Задача</th>
                    <th>Место</th>
                    <th>Дата</th>
                    <th>Время</th>
                </tr>
                <tr>
                    <td name="type1">. </td>
                    <td name="theme1">. </td>
                    <td name="place1">. </td>
                    <td name="date1">. </td>
                    <td name="time1">. </td>
                </tr>
            </table>
-->
<?php
    $hostname="localhost";
    $db="tdlist";
    $username="root";
    $password = "";
    
    $conn = new PDO(
        "mysql:host=localhost;dbname=$db",
        $username,
        $password
    );
            
    $sql1 = "SELECT type, theme, place, date, time FROM todolist";
    
    if ($result = $conn->query($sql1)) {
        echo "<table><tr><th>Тип</th><th>Задача</th><th>Место</th><th>Дата</th><th>Время</th></tr>";
        foreach ($result as $row){
            if(strtotime($row["date"])<strtotime(date('Y-m-d'))) {
                echo "<tr bgcolor=red>";
            }
            else if(strtotime($row["date"])==strtotime(date('Y-m-d'))){
                echo "<tr bgcolor=#FFEE77>";
            }
            else {
                echo "<tr>";
            }
                echo "<td>" . $row["type"] . "</td>";
                echo "<td>" . $row["theme"] . "</td>";
                echo "<td>" . $row["place"] . "</td>";
                echo "<td>" . $row["date"] . "</td>";
                echo "<td>" . $row["time"] . "</td>";
                echo "<td><form action='delete.php' method='post'>
                        <input type='hidden' name='id' value='" . $row["id"] . "' />
                        <input type='submit' value='&#9842;'>
                       </form></td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "<p> Ошибка вывода данных";
    }
?>
        </div>
    </body>
</html>

