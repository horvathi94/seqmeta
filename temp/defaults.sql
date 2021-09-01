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
-- Table structure for table `default_values`
--

DROP TABLE IF EXISTS `default_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `default_values` (
  `item_key` varchar(100) NOT NULL,
  `item_value` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`item_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_values`
--

LOCK TABLES `default_values` WRITE;
/*!40000 ALTER TABLE `default_values` DISABLE KEYS */;
INSERT INTO `default_values` VALUES ('author_group_id','0'),('collection_device_id','0'),('collector_id','0'),('consensus_assembly_method','0'),('contigs_assembly_method','0'),('continent_id','3'),('country_id','207'),('geo_loc_latitude',NULL),('geo_loc_longitude',NULL),('host_anatomical_material_id','0'),('host_body_product_id','0'),('host_health_state_id','0'),('host_id','0'),('insert_size','300'),('library_construction_protocol',''),('library_design_description','\r\n\r\n\r\n'),('library_layout_paired','1'),('library_selection_id','0'),('library_source_id','0'),('library_strategy_id','0'),('locality','Sfantu Gheorghe'),('originating_lab_id','0'),('passage_method',''),('passage_number','0'),('patient_status_id','0'),('purpose_of_sampling_id','0'),('purpose_of_sequencing_id','0'),('region','Covasna'),('sample_capture_status_id','0'),('sample_storage_conditions',''),('sampling_strategy_id','0'),('sars_cov_2_diag_gene_name_1_id','0'),('sars_cov_2_diag_gene_name_2_id','0'),('scaffolds_assembly_method','0'),('sequencing_instrument_id','0'),('sequencing_lab_id','0'),('specimen_source_id','0'),('submitting_lab_id','0');
/*!40000 ALTER TABLE `default_values` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-27  7:41:55
