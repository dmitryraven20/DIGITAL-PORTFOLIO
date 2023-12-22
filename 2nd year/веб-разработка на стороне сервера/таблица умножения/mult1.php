<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Таблица умножения</title>
    </head>
    <style>
        td {
            border: 2px solid black;
            width: 60px;
            font-size: 26px;
            background-color: #FFDFBB;
            text-align: center;
            font-family: century gothic;
        }
        
        .prim {
            background-color: crimson;
        }
        .sec {
            background-color: lightyellow;
        }
    </style>
    <body>
        <table>
            <?php
            include 'mult.php';
            ?>
        </table>
        
        
    </body>
</html>