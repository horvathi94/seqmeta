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
-- Dumping data for table `samples`
--

LOCK TABLES `samples` WRITE;
/*!40000 ALTER TABLE `samples` DISABLE KEYS */;
INSERT INTO `samples` VALUES (1,'TEST01','First detected Delta variant in Romania.','','','','hCoV-19/Europe/Romania_PV_TEST01/2020-text','Sars-CoV-2/Homo sapiens/Europe/Romania-3/2020_new');
/*!40000 ALTER TABLE `samples` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_collection`
--

LOCK TABLES `samples_collection` WRITE;
/*!40000 ALTER TABLE `samples_collection` DISABLE KEYS */;
INSERT INTO `samples_collection` VALUES (1,2020,3,4,0,1,1,'ORIGID',1,'SUBMITTINGID',1);
/*!40000 ALTER TABLE `samples_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_health_status`
--

LOCK TABLES `samples_health_status` WRITE;
/*!40000 ALTER TABLE `samples_health_status` DISABLE KEYS */;
INSERT INTO `samples_health_status` VALUES (1,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL);
/*!40000 ALTER TABLE `samples_health_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_host`
--

LOCK TABLES `samples_host` WRITE;
/*!40000 ALTER TABLE `samples_host` DISABLE KEYS */;
INSERT INTO `samples_host` VALUES (1,1,NULL,NULL,_binary '',47,1,'',0,0,'','','',NULL);
/*!40000 ALTER TABLE `samples_host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_library`
--

LOCK TABLES `samples_library` WRITE;
/*!40000 ALTER TABLE `samples_library` DISABLE KEYS */;
INSERT INTO `samples_library` VALUES (1,NULL,_binary '',0,0,0,'',NULL,300,'');
/*!40000 ALTER TABLE `samples_library` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_location`
--

LOCK TABLES `samples_location` WRITE;
/*!40000 ALTER TABLE `samples_location` DISABLE KEYS */;
INSERT INTO `samples_location` VALUES (1,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL,0);
/*!40000 ALTER TABLE `samples_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_patient_treatment`
--

LOCK TABLES `samples_patient_treatment` WRITE;
/*!40000 ALTER TABLE `samples_patient_treatment` DISABLE KEYS */;
INSERT INTO `samples_patient_treatment` VALUES (1,NULL,NULL,NULL,NULL,0,NULL,'','','');
/*!40000 ALTER TABLE `samples_patient_treatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_sampling`
--

LOCK TABLES `samples_sampling` WRITE;
/*!40000 ALTER TABLE `samples_sampling` DISABLE KEYS */;
/*!40000 ALTER TABLE `samples_sampling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_sequencing`
--

LOCK TABLES `samples_sequencing` WRITE;
/*!40000 ALTER TABLE `samples_sequencing` DISABLE KEYS */;
INSERT INTO `samples_sequencing` VALUES (1,0,NULL,1);
/*!40000 ALTER TABLE `samples_sequencing` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-27  8:15:29
