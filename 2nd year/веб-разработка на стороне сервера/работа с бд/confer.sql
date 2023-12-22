-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 26 2023 г., 18:56
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `tdlist`
--

-- --------------------------------------------------------

--
-- Структура таблицы `confer`
--

CREATE TABLE `confer` (
  `id` int UNSIGNED NOT NULL,
  `name` varchar(100) NOT NULL,
  `surname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone number` int NOT NULL,
  `theme` varchar(100) NOT NULL,
  `payment type` varchar(100) NOT NULL,
  `subscription` varchar(10) NOT NULL,
  `registration date` datetime NOT NULL,
  `user ip` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `confer`
--

INSERT INTO `confer` (`id`, `name`, `surname`, `email`, `phone number`, `theme`, `payment type`, `subscription`, `registration date`, `user ip`) VALUES
(3, 'Дмитрий', 'Власов', 't@r', 1234, 'Реклама и маркетинг', 'кредитная карта', 'on', '2023-05-26 18:50:00', '127.0.0.1'),
(4, 'Алексей', 'Шабалин', 'h@a', 9876, 'Технологии', 'Яндекс.Деньги', '', '2023-05-26 18:51:00', '127.0.0.1'),
(5, 'Даниил', 'Ботвенко', 't@a', 4561, 'Бизнес', 'Яндекс.Деньги', 'on', '2023-05-26 18:52:00', '127.0.0.1');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `confer`
--
ALTER TABLE `confer`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `confer`
--
ALTER TABLE `confer`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
