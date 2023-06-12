-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 12, 2023 at 09:47 PM
-- Server version: 8.0.32
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `work`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `id` int NOT NULL,
  `locationName` text NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`id`, `locationName`, `Date`) VALUES
(8, 'Warehouse1', '2023-06-01'),
(9, 'Warehouse2', '2023-06-14'),
(10, 'Warehouse3', '2023-06-30'),
(11, 'Warehouse4', '2023-04-12'),
(12, 'Warehouse5', '2023-07-06'),
(14, 'Warehouse6', '2023-06-28');

-- --------------------------------------------------------

--
-- Table structure for table `movements`
--

CREATE TABLE `movements` (
  `id` int NOT NULL,
  `pid` int NOT NULL,
  `Quantity` int NOT NULL,
  `fromLocation` int DEFAULT NULL,
  `toLocation` int DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `movements`
--

INSERT INTO `movements` (`id`, `pid`, `Quantity`, `fromLocation`, `toLocation`, `time`) VALUES
(117, 27, 100, NULL, 8, '2023-06-12 17:59:22'),
(119, 25, 10, NULL, 8, '2023-06-12 18:00:16'),
(120, 22, 46, 8, 9, '2023-06-12 18:31:15'),
(121, 23, 35, 8, 9, '2023-06-12 18:31:43'),
(122, 22, 10, NULL, 14, '2023-06-12 19:05:27'),
(123, 25, 10, NULL, 12, '2023-06-12 19:06:02'),
(124, 23, 23, NULL, 9, '2023-06-12 19:06:59'),
(125, 24, 36, 11, 12, '2023-06-12 19:07:15'),
(126, 27, 10, NULL, 9, '2023-06-12 19:07:54'),
(127, 24, 10, 12, 14, '2023-06-12 19:08:28'),
(128, 25, 90, NULL, 8, '2023-06-12 19:08:41'),
(129, 27, 52, 10, 12, '2023-06-12 19:13:08'),
(130, 22, 26, NULL, 11, '2023-06-12 19:13:41'),
(131, 25, 50, 8, 11, '2023-06-12 19:14:38'),
(132, 27, 8, 12, 8, '2023-06-12 19:15:40'),
(133, 22, 26, NULL, 10, '2023-06-12 19:16:09'),
(134, 23, 24, NULL, 11, '2023-06-12 19:16:21'),
(135, 24, 3, 14, NULL, '2023-06-12 19:16:48'),
(136, 23, 10, NULL, 11, '2023-06-12 19:17:16'),
(137, 27, 50, NULL, 14, '2023-06-12 19:18:02');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int NOT NULL,
  `productName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `productName`, `date`) VALUES
(22, 'Apple', '2023-06-01'),
(23, 'Nike', '2023-06-30'),
(24, 'Amazon Products', '2023-06-30'),
(25, 'Greyhound', '2023-07-09'),
(27, 'Prada', '2022-12-12');

-- --------------------------------------------------------

--
-- Table structure for table `tblemployee`
--

CREATE TABLE `tblemployee` (
  `id` int NOT NULL,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `department` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tblemployee`
--

INSERT INTO `tblemployee` (`id`, `name`, `department`, `phone`) VALUES
(37, 'Rasha', 'Engineering', '+972594058607'),
(38, 'rashasalahat1', 'Eng', '+972594058607');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `movements`
--
ALTER TABLE `movements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pid` (`pid`),
  ADD KEY `fromLocation` (`fromLocation`),
  ADD KEY `toLocation` (`toLocation`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tblemployee`
--
ALTER TABLE `tblemployee`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `movements`
--
ALTER TABLE `movements`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=138;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `tblemployee`
--
ALTER TABLE `tblemployee`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `movements`
--
ALTER TABLE `movements`
  ADD CONSTRAINT `movements_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `product` (`id`),
  ADD CONSTRAINT `movements_ibfk_2` FOREIGN KEY (`fromLocation`) REFERENCES `location` (`id`),
  ADD CONSTRAINT `movements_ibfk_3` FOREIGN KEY (`toLocation`) REFERENCES `location` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
