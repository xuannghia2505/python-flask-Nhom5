-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: qlloteria
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `food` (
  `foodId` int(11) NOT NULL AUTO_INCREMENT,
  `foodName` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `description` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`foodId`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES (1,'Combo Burger bò Teriyaki trứng',5,'Burger bò Teriyaki trứng + Mì ý + Khoai tây chiên (M) + Pepsi (M)','1','food'),(2,'Combo  Burger double double',7,'Burger double double + Gà rán + Khoai tây lắc + 2 Pepsi (M)','2','food'),(3,'Combo Gà sốt đậu',4,'Burger double double + Gà rán + Khoai tây lắc + 2 Pepsi (M)','3','food'),(4,'Combo Burger bò Bulgogi',5,'Burger Bulgogi + Khoai Tây Chiên (S) + Pepsi (M)','4','food'),(5,'Gà rán ',2,'Gà rán chiên giòn (1 miếng)','5','food'),(6,'Gà rán phần ',4,'Chicken set ','6','food'),(7,'Gà H&S phần ',8,'H&S Chicken set ','7','food'),(8,'Gà đậu sốt set ',8,'soy bean chicken set ','8','food'),(9,'Gà H&S phần lớn ',12,'H&S Chicken set (3 miếng) ','9','food'),(10,'Gà phomai phần không cay ',6,'Cheese chicken 3 miếng không cay ','10','food'),(11,'Gà rán phần lớn',8,'Gà rán phần lớn (6 miếng) ','11','food'),(12,'Burger bò teriyaki',3,'1 burger bò teriyaki ','12','food'),(13,'Burger Tôm ',3,'1 Burger tôm ','13','food'),(14,'Burger gà thượng hạng',4,'Burger với nguồn nguyên liệu gà ','14','food'),(15,'Burger Phomai ',4,'Phô mai hảo hạng tan chảy trên nhân bò ','15','food'),(16,'Burger Double Double ',7,'1 Burger bò double double ','16','food'),(17,'Burger Hawai ',6,'Burger Hawai hòa quyện phomai ','17','food'),(18,'Cơm gà sốt đậu',5,'1 phần cơm gà sốt đậu ','18','food'),(19,'Cơm thịt bò',5,'1 phần cơm thịt bò nướng ','19','food'),(20,'Cơm gà viên',5,'1 phần cơm gà viên + trứng ','20','food'),(21,'Pepsi (M)',2,'1 ly pepsi size M ','21','drink'),(22,'Pepsi (L)',3,'1 ly pepsi size L ','22','drink'),(23,'7 up (L)',3,'1  ly 7 up size L','23','drink'),(24,'Milo',5,'1 ly Milo size L ','24','drink'),(25,'Nước cam',4,'1 ly nước cam size L ','25','drink'),(27,'Thịt heo',10,'Thịt heo chiên giòn ăn ngon lắm','thitheo','food'),(29,'Thịt heo',10,'Thịt heo chiên giòn ăn ngon lắm','flt2','food'),(31,'Trà sữa',6,'Trà sữa trân châu ','trasua','drink');
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'nghia','123',1),(2,'tuan','123',2),(3,'trang','123',3);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-16 21:14:11
