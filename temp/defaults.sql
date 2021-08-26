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
-- Dumping data for table `default_values`
--

LOCK TABLES `default_values` WRITE;
/*!40000 ALTER TABLE `default_values` DISABLE KEYS */;
INSERT INTO `default_values` VALUES ('assembly_file','1'),('assembly_method_id','0'),('author_group_id','0'),('collection_device_id','0'),('collector_id','0'),('consensus_assembly_method','2'),('consensus_assembly_method_id',NULL),('contigs_assembly_method','4'),('contigs_assembly_method_id',NULL),('continent_id','0'),('country_id','0'),('geo_loc_latitude',NULL),('geo_loc_longitude',NULL),('host_anatomical_material_id','0'),('host_body_product_id','0'),('host_health_state_id','0'),('host_id','0'),('insert_size','0'),('library_construction_protocol',''),('library_design_description','\r\n\r\n\r\n\r\n'),('library_layout_paired','0'),('library_selection_id','0'),('library_source_id','0'),('library_strategy_id','0'),('locality',NULL),('originating_lab_id','0'),('passage_method',''),('passage_number','0'),('patient_status_id','0'),('purpose_of_sampling_id','0'),('purpose_of_sequencing_id','0'),('region',NULL),('sample_capture_status_id','0'),('sample_storage_conditions',''),('sampling_strategy_id','0'),('sars_cov_2_diag_gene_name_1_id','0'),('sars_cov_2_diag_gene_name_2_id','0'),('scaffolds_assembly_method','1'),('scaffolds_assembly_method_id',NULL),('sequencing_instrument_id','0'),('sequencing_lab_id','0'),('specimen_source_id','0'),('submitting_lab_id','0');
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

-- Dump completed on 2021-08-26 11:04:03
