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
-- Table structure for table `hosts`
--

DROP TABLE IF EXISTS `hosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hosts` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `latin` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts`
--

LOCK TABLES `hosts` WRITE;
/*!40000 ALTER TABLE `hosts` DISABLE KEYS */;
INSERT INTO `hosts` VALUES (1,'Human','Homo sapiens',1),(2,'bug','melanogaster',2);
/*!40000 ALTER TABLE `hosts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assembly_methods`
--

DROP TABLE IF EXISTS `assembly_methods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assembly_methods` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assembly_methods`
--

LOCK TABLES `assembly_methods` WRITE;
/*!40000 ALTER TABLE `assembly_methods` DISABLE KEYS */;
INSERT INTO `assembly_methods` VALUES (1,'CLC Genomics Workbench 12',1),(2,'Geneious 10.2.4',2),(3,'SPAdes/MEGAHIT v1.2.9',3),(4,'UGENE v. 33',4);
/*!40000 ALTER TABLE `assembly_methods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sampling_strategies`
--

DROP TABLE IF EXISTS `sampling_strategies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sampling_strategies` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sampling_strategies`
--

LOCK TABLES `sampling_strategies` WRITE;
/*!40000 ALTER TABLE `sampling_strategies` DISABLE KEYS */;
INSERT INTO `sampling_strategies` VALUES (1,'Sentinel surveillance (ILI)',1),(2,'Sentinel surveillance (ARI)',2),(3,'Sentinel surveillance (SARI)',3),(4,'Non-sentinel-surveillance (hospital)',3),(5,'Non-sentinel-surveillance (GP network)',4),(6,'Longitudinal sampling on same patient(s)',5),(7,'S gene dropout',6);
/*!40000 ALTER TABLE `sampling_strategies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specimen_sources`
--

DROP TABLE IF EXISTS `specimen_sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specimen_sources` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specimen_sources`
--

LOCK TABLES `specimen_sources` WRITE;
/*!40000 ALTER TABLE `specimen_sources` DISABLE KEYS */;
INSERT INTO `specimen_sources` VALUES (1,'Sputum',1),(2,'Alveolar lavage fluid',2),(3,'Oro-pharyngeal swab',3),(4,'Blood',4),(5,'Tracheal swab',5),(6,'Urine',6),(7,'Stool',7),(8,'Cloakal swab',8),(9,'Organ',9),(10,'Feces',10),(11,'Other ',11);
/*!40000 ALTER TABLE `specimen_sources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_devices`
--

DROP TABLE IF EXISTS `collection_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collection_devices` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_devices`
--

LOCK TABLES `collection_devices` WRITE;
/*!40000 ALTER TABLE `collection_devices` DISABLE KEYS */;
INSERT INTO `collection_devices` VALUES (1,'swab',1),(2,'naso-swab',2);
/*!40000 ALTER TABLE `collection_devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_anatomical_materials`
--

DROP TABLE IF EXISTS `host_anatomical_materials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `host_anatomical_materials` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_anatomical_materials`
--

LOCK TABLES `host_anatomical_materials` WRITE;
/*!40000 ALTER TABLE `host_anatomical_materials` DISABLE KEYS */;
INSERT INTO `host_anatomical_materials` VALUES (1,'stool',1),(2,'mucus',2),(3,'saliva',3);
/*!40000 ALTER TABLE `host_anatomical_materials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_body_products`
--

DROP TABLE IF EXISTS `host_body_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `host_body_products` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_body_products`
--

LOCK TABLES `host_body_products` WRITE;
/*!40000 ALTER TABLE `host_body_products` DISABLE KEYS */;
INSERT INTO `host_body_products` VALUES (1,'stool',1),(2,'mucus',2),(3,'saliva',3);
/*!40000 ALTER TABLE `host_body_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purposes_of_sampling`
--

DROP TABLE IF EXISTS `purposes_of_sampling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purposes_of_sampling` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purposes_of_sampling`
--

LOCK TABLES `purposes_of_sampling` WRITE;
/*!40000 ALTER TABLE `purposes_of_sampling` DISABLE KEYS */;
INSERT INTO `purposes_of_sampling` VALUES (1,'diagnostic testing',1);
/*!40000 ALTER TABLE `purposes_of_sampling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purposes_of_sequencing`
--

DROP TABLE IF EXISTS `purposes_of_sequencing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purposes_of_sequencing` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` varchar(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purposes_of_sequencing`
--

LOCK TABLES `purposes_of_sequencing` WRITE;
/*!40000 ALTER TABLE `purposes_of_sequencing` DISABLE KEYS */;
INSERT INTO `purposes_of_sequencing` VALUES (1,'baseline surveillance (random sampling)',1);
/*!40000 ALTER TABLE `purposes_of_sequencing` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-27  8:11:15
