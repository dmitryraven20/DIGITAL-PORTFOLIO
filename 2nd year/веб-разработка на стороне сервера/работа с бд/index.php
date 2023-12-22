<!DOCTYPE html>

<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Регистрация на конференцию (mysql)</title>
    </head>
    <style>
        body {
            text-align: center;
            font-size: 25px;
            font-family: fantasy;
            background-color: darkred;
        }
        h1 {
            font-size: 35px;
        }
        .put {
            width: 400px;
            font-size: 20px;
            border-radius: 10px;
            border: 2px solid darkred;
        }
        .put1 {
            font-family: sans-serif;
            font-size: 18px;
        }
        button {
            font-size: 20px;
            height: 60px;
            width: 250px;
        }
        .phon {
            position: absolute;
            background-color: white;
            width: 510px;
            height: 730px;
            border-radius: 35px;
            left: 33%;
        }
    </style>
    <body>
        <div class='phon'>
        <h1>Регистрация на конференцию</h1>
        <form action="register.php" method="post">
            <p> <input type="text" placeholder="Имя" name="name" class='put' required>
            <p> <input type="text" placeholder="Фамилия" name="surname" class='put' required>
            <p> <input type="email" placeholder="Email" name="email" class='put' required>
            <p> <input type="number" placeholder="Номер телефона" name="num" class='put' required>
            
            <p> Выберите тему конференции:
            <p> <select name="theme"  class='put' required>
                <option>Бизнес</option>
                <option>Технологии</option>
                <option>Реклама и маркетинг</option>
            </select>
            
            <p> Метод оплаты участия:
            <p> <select name="payment"  class='put' required>
                <option>WebMoney</option>
                <option>Яндекс.Деньги</option>
                <option>PayPal</option>
                <option>кредитная карта</option>
            </select>
                
            <p> <input type="checkbox" name="subscr"> <div class='put1'>Хочу получать рассылку о конференции</div>
            
            <p> <button type="submit">Зарегистрироваться</button>
        </form>
        </div>
    </body>
</html>