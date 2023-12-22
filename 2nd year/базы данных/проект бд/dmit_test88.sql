Основная информация перенесена из .sql-файла по базе данных. 
Тема – радиостанция. 1 основная таблица и 3 дополнительные, а также 5 представлений.
Основные операции – создание, правка и смена статусов

-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Май 20 2023 г., 20:08
-- Версия сервера: 5.7.36-39
-- Версия PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `dmit_test88`
--

-- --------------------------------------------------------

--
-- Дублирующая структура для представления `AirD 20-05 20-06`
-- (См. Ниже фактическое представление)
--
CREATE TABLE `AirD 20-05 20-06` (
`playlist` varchar(255)
,`song amount` varchar(255)
,`airdate` date
);

-- --------------------------------------------------------

--
-- Дублирующая структура для представления `Cancelled`
-- (См. Ниже фактическое представление)
--
CREATE TABLE `Cancelled` (
`playlist` varchar(255)
,`airdate` date
,`type` varchar(255)
);

-- --------------------------------------------------------

--
-- Структура таблицы `djs`
--

CREATE TABLE `djs` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `djs`
--

INSERT INTO `djs` (`id`, `name`, `age`, `phone`) VALUES
(1, 'Teri', '25', '454112'),
(2, 'Adam', '27', '887934'),
(3, 'Lazlow', '41', '146735'),
(4, 'Kenny', '36', '464124');

-- --------------------------------------------------------

--
-- Дублирующая структура для представления `Full tab`
-- (См. Ниже фактическое представление)
--
CREATE TABLE `Full tab` (
`playlist` varchar(255)
,`song amount` varchar(255)
,`airdate` date
,`dj` varchar(255)
,`genre` varchar(255)
,`status` varchar(255)
);

-- --------------------------------------------------------

--
-- Структура таблицы `genrelist`
--

CREATE TABLE `genrelist` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `genrelist`
--

INSERT INTO `genrelist` (`id`, `name`) VALUES
(1, 'Rock'),
(2, 'Synthpop'),
(3, 'Disco'),
(4, 'Europop');

-- --------------------------------------------------------

--
-- Дублирующая структура для представления `Pop`
-- (См. Ниже фактическое представление)
--
CREATE TABLE `Pop` (
`playlist` varchar(255)
,`song amount` varchar(255)
,`airdate` date
,`dj` varchar(255)
,`genre` varchar(255)
,`status` varchar(255)
);

-- --------------------------------------------------------

--
-- Структура таблицы `radiostations`
--

CREATE TABLE `radiostations` (
  `id` int(10) UNSIGNED NOT NULL,
  `playlist` varchar(255) NOT NULL,
  `song amount` varchar(255) NOT NULL,
  `airdate` date NOT NULL,
  `genre_id` int(10) UNSIGNED DEFAULT NULL,
  `dj_id` int(10) UNSIGNED DEFAULT NULL,
  `status_id` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `radiostations`
--

INSERT INTO `radiostations` (`id`, `playlist`, `song amount`, `airdate`, `genre_id`, `dj_id`, `status_id`) VALUES
(1, '707', '12', '2023-06-15', 2, 2, 1),
(2, 'VROCK', '15', '2023-06-02', 1, 3, 2),
(3, 'Jam Session', '9', '2023-06-23', 3, 1, 2),
(4, 'Sample U later', '10', '2023-05-02', 2, 2, 3),
(5, 'Lowkik', '14', '2023-06-12', 1, 3, 1),
(6, 'LS-RR', '15', '2023-06-26', 1, 4, 1),
(7, 'Flash!', '14', '2023-05-08', 2, 1, 3),
(8, 'Bridge msc', '13', '2023-06-19', 4, 1, 1),
(9, 'Beware', '9', '2023-06-27', 3, 2, 2),
(10, 'A Final Mix', '16', '2023-06-17', 2, 2, 1),
(11, 'PPK', '13', '2023-05-20', 3, 2, 3),
(12, '2037', '16', '2023-05-31', 1, 4, 2),
(13, 'Masterpiece', '9', '2023-06-10', 4, 3, 1),
(14, 'DasAscribblE', '13', '2023-06-06', 1, 4, 4),
(15, 'West Pacifica', '11', '2023-05-28', 2, 4, 4);

-- --------------------------------------------------------

--
-- Дублирующая структура для представления `Reschedule`
-- (См. Ниже фактическое представление)
--
CREATE TABLE `Reschedule` (
`playlist` varchar(255)
,`song amount` varchar(255)
,`airdate` date
,`status` varchar(255)
);

-- --------------------------------------------------------

--
-- Структура таблицы `statuses`
--

CREATE TABLE `statuses` (
  `id` int(10) UNSIGNED NOT NULL,
  `type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `statuses`
--

INSERT INTO `statuses` (`id`, `type`) VALUES
(1, 'Work In Progress'),
(2, 'Scheduled To Air'),
(3, 'Ended'),
(4, 'Cancelled');

-- --------------------------------------------------------

--
-- Структура для представления `AirD 20-05 20-06`
--
DROP TABLE IF EXISTS `AirD 20-05 20-06`;

CREATE ALGORITHM=UNDEFINED DEFINER=`dmit_test88`@`localhost` SQL SECURITY DEFINER VIEW `AirD 20-05 20-06`  AS SELECT `radiostations`.`playlist` AS `playlist`, `radiostations`.`song amount` AS `song amount`, `radiostations`.`airdate` AS `airdate` FROM `radiostations` WHERE (`radiostations`.`airdate` between '2023-05-20' and '2023-06-20')  ;

-- --------------------------------------------------------

--
-- Структура для представления `Cancelled`
--
DROP TABLE IF EXISTS `Cancelled`;

CREATE ALGORITHM=UNDEFINED DEFINER=`dmit_test88`@`localhost` SQL SECURITY DEFINER VIEW `Cancelled`  AS SELECT `radiostations`.`playlist` AS `playlist`, `radiostations`.`airdate` AS `airdate`, `statuses`.`type` AS `type` FROM (`radiostations` join `statuses` on((`radiostations`.`status_id` = `statuses`.`id`))) WHERE (`statuses`.`type` = 'Cancelled') GROUP BY `radiostations`.`id``id`  ;

-- --------------------------------------------------------

--
-- Структура для представления `Full tab`
--
DROP TABLE IF EXISTS `Full tab`;

CREATE ALGORITHM=UNDEFINED DEFINER=`dmit_test88`@`localhost` SQL SECURITY DEFINER VIEW `Full tab`  AS SELECT `radiostations`.`playlist` AS `playlist`, `radiostations`.`song amount` AS `song amount`, `radiostations`.`airdate` AS `airdate`, `djs`.`name` AS `dj`, `genrelist`.`name` AS `genre`, `statuses`.`type` AS `status` FROM (((`radiostations` join `genrelist` on((`radiostations`.`genre_id` = `genrelist`.`id`))) join `djs` on((`radiostations`.`dj_id` = `djs`.`id`))) join `statuses` on((`radiostations`.`status_id` = `statuses`.`id`))) GROUP BY `radiostations`.`id``id`  ;

-- --------------------------------------------------------

--
-- Структура для представления `Pop`
--
DROP TABLE IF EXISTS `Pop`;

CREATE ALGORITHM=UNDEFINED DEFINER=`dmit_test88`@`localhost` SQL SECURITY DEFINER VIEW `Pop`  AS SELECT `Full tab`.`playlist` AS `playlist`, `Full tab`.`song amount` AS `song amount`, `Full tab`.`airdate` AS `airdate`, `Full tab`.`dj` AS `dj`, `Full tab`.`genre` AS `genre`, `Full tab`.`status` AS `status` FROM `Full tab` WHERE (`Full tab`.`genre` in ('Europop','Synthpop'))  ;

-- --------------------------------------------------------

--
-- Структура для представления `Reschedule`
--
DROP TABLE IF EXISTS `Reschedule`;

CREATE ALGORITHM=UNDEFINED DEFINER=`dmit_test88`@`localhost` SQL SECURITY DEFINER VIEW `Reschedule`  AS SELECT `radiostations`.`playlist` AS `playlist`, `radiostations`.`song amount` AS `song amount`, `radiostations`.`airdate` AS `airdate`, `statuses`.`type` AS `status` FROM (`radiostations` join `statuses` on((`radiostations`.`status_id` = `statuses`.`id`))) WHERE (`radiostations`.`airdate` between '2023-05-01' and '2023-06-20') GROUP BY `radiostations`.`id``id`  ;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `djs`
--
ALTER TABLE `djs`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `genrelist`
--
ALTER TABLE `genrelist`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `radiostations`
--
ALTER TABLE `radiostations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `genre_id` (`genre_id`),
  ADD KEY `dj_id` (`dj_id`),
  ADD KEY `radiostations_ibfk_3` (`status_id`);

--
-- Индексы таблицы `statuses`
--
ALTER TABLE `statuses`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `djs`
--
ALTER TABLE `djs`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `genrelist`
--
ALTER TABLE `genrelist`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `radiostations`
--
ALTER TABLE `radiostations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT для таблицы `statuses`
--
ALTER TABLE `statuses`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `radiostations`
--
ALTER TABLE `radiostations`
  ADD CONSTRAINT `radiostations_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genrelist` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `radiostations_ibfk_2` FOREIGN KEY (`dj_id`) REFERENCES `djs` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `radiostations_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `statuses` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
