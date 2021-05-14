-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: sequencing_data
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `author_groups`
--

DROP TABLE IF EXISTS `author_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author_groups` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` char(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author_groups`
--

LOCK TABLES `author_groups` WRITE;
/*!40000 ALTER TABLE `author_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `author_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authors` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `first_name` char(100) NOT NULL,
  `middle_name` char(100) DEFAULT NULL,
  `last_name` char(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Szilard','Nabor','Fejer'),(2,'Monika','','Korodi'),(3,'Zsuzsanna','','Jenei'),(4,'Kinga','','Rakosi'),(5,'Istvan','','Horvath');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authors_in_group`
--

DROP TABLE IF EXISTS `authors_in_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authors_in_group` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `author_id` int unsigned DEFAULT NULL,
  `author_group_id` int unsigned DEFAULT NULL,
  `order_index` tinyint unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors_in_group`
--

LOCK TABLES `authors_in_group` WRITE;
/*!40000 ALTER TABLE `authors_in_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `authors_in_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institutions`
--

DROP TABLE IF EXISTS `institutions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institutions` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` char(100) DEFAULT NULL,
  `address` text NOT NULL,
  `postal_code` mediumint unsigned DEFAULT NULL,
  `county` char(100) DEFAULT NULL,
  `country` char(100) DEFAULT NULL,
  `city` char(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institutions`
--

LOCK TABLES `institutions` WRITE;
/*!40000 ALTER TABLE `institutions` DISABLE KEYS */;
/*!40000 ALTER TABLE `institutions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_data`
--

DROP TABLE IF EXISTS `sample_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sample_data` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` char(100) NOT NULL,
  `submission_date` date NOT NULL,
  `collection_date` date NOT NULL,
  `patient_age` tinyint DEFAULT NULL,
  `patient_gender` bit(1) DEFAULT NULL,
  `originating_lab_id` int unsigned NOT NULL,
  `submitting_lab_id` int unsigned NOT NULL,
  `author_group_id` int unsigned NOT NULL,
  `assembly_method` char(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_data`
--

LOCK TABLES `sample_data` WRITE;
/*!40000 ALTER TABLE `sample_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `sample_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_authors_in_groups`
--

DROP TABLE IF EXISTS `view_authors_in_groups`;
/*!50001 DROP VIEW IF EXISTS `view_authors_in_groups`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_authors_in_groups` AS SELECT 
 1 AS `group_id`,
 1 AS `group_name`,
 1 AS `author_id`,
 1 AS `first_name`,
 1 AS `middle_name`,
 1 AS `last_name`,
 1 AS `order_index`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples`
--

DROP TABLE IF EXISTS `view_samples`;
/*!50001 DROP VIEW IF EXISTS `view_samples`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples` AS SELECT 
 1 AS `sample_id`,
 1 AS `sample_name`,
 1 AS `collection_date`,
 1 AS `author_group_id`,
 1 AS `author_group_name`,
 1 AS `originating_lab_id`,
 1 AS `originating_lab_name`,
 1 AS `submitting_lab_id`,
 1 AS `submitting_lab_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_authors_in_groups`
--

/*!50001 DROP VIEW IF EXISTS `view_authors_in_groups`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_authors_in_groups` AS select `groups`.`id` AS `group_id`,`groups`.`name` AS `group_name`,`authors`.`id` AS `author_id`,`authors`.`first_name` AS `first_name`,`authors`.`middle_name` AS `middle_name`,`authors`.`last_name` AS `last_name`,`as_in_g`.`order_index` AS `order_index` from ((`author_groups` `groups` left join `authors_in_group` `as_in_g` on((`groups`.`id` = `as_in_g`.`author_group_id`))) left join `authors` on((`as_in_g`.`author_id` = `authors`.`id`))) order by `groups`.`id`,`as_in_g`.`order_index` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples`
--

/*!50001 DROP VIEW IF EXISTS `view_samples`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples` AS select `sample`.`id` AS `sample_id`,`sample`.`name` AS `sample_name`,`sample`.`collection_date` AS `collection_date`,`agroup`.`id` AS `author_group_id`,`agroup`.`name` AS `author_group_name`,`originating_lab`.`id` AS `originating_lab_id`,`originating_lab`.`name` AS `originating_lab_name`,`submitting_lab`.`id` AS `submitting_lab_id`,`submitting_lab`.`name` AS `submitting_lab_name` from (((`sample_data` `sample` left join `author_groups` `agroup` on((`sample`.`author_group_id` = `agroup`.`id`))) left join `institutions` `originating_lab` on((`sample`.`originating_lab_id` = `originating_lab`.`id`))) left join `institutions` `submitting_lab` on((`sample`.`submitting_lab_id` = `submitting_lab`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-14  7:47:50
