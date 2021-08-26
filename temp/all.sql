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
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Istvan','','Horvath'),(2,'Monika','','Korodi'),(3,'Szilard','N','Fejer'),(4,'Kinga','','Rakosi');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `author_groups`
--

LOCK TABLES `author_groups` WRITE;
/*!40000 ALTER TABLE `author_groups` DISABLE KEYS */;
INSERT INTO `author_groups` VALUES (1,'TestGroup'),(2,'inserted');
/*!40000 ALTER TABLE `author_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `authors_in_group`
--

LOCK TABLES `authors_in_group` WRITE;
/*!40000 ALTER TABLE `authors_in_group` DISABLE KEYS */;
INSERT INTO `authors_in_group` VALUES (1,2,1,1),(2,1,1,2),(3,1,2,1),(4,2,2,2),(5,4,2,3);
/*!40000 ALTER TABLE `authors_in_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `institutions`
--

LOCK TABLES `institutions` WRITE;
/*!40000 ALTER TABLE `institutions` DISABLE KEYS */;
INSERT INTO `institutions` VALUES (1,'Pro-Vitam','16 Muncitorilor Street',500123,207,'Covasna','Sfantu Gheorghe','PV'),(2,'Pro-Vitam2','16 Muncitorilor Street',500123,207,'Covasna','','');
/*!40000 ALTER TABLE `institutions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-26 11:04:47
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
INSERT INTO `samples` VALUES (1,'TWONEW1','Added with new save','','Test description of sample.','','hCoV-19Europe/Romania_PV_TWONEW1/-gsdgdsg','Sars-CoV-2/None/Europe/Romania-/'),(10,'TEST01','testcomment','First test sample','First detected Delta variant in Romania.','ELP_324324','dfgdfgdfg','Sars-CoV-2/Homo sapiens/Europe/Romania-4/2021'),(11,'NEW01','','','','','hCoV-19Europe/Romania_PV_NEW01/2022','Sars-CoV-2/Homo sapiens/Europe/Romania-7/2022'),(12,'test2','testing add multiple','','','','hCoV-19Europe/Romania_PV_test2/-gsdgdsg','Sars-CoV-2/None/Europe/Romania-/'),(13,'test3','testing add multiple','','','','hCoV-19Europe/Romania_PV_test3/-gsdgdsg','Sars-CoV-2/None/Europe/Romania-/'),(14,'1','multi add','','','','hCoV-19Europe/Romania_PV_1/-gsdgdsg','Sars-CoV-2/None/Europe/Romania-/'),(15,'3223','multi add','','','','hCoV-19Europe/Romania_PV_3223/-gsdgdsg','Sars-CoV-2/None/Europe/Romania-/');
/*!40000 ALTER TABLE `samples` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_collection`
--

LOCK TABLES `samples_collection` WRITE;
/*!40000 ALTER TABLE `samples_collection` DISABLE KEYS */;
INSERT INTO `samples_collection` VALUES (1,NULL,NULL,NULL,0,0,0,'',0,'',0),(10,2021,4,5,0,0,0,'',0,'',0),(11,2022,7,3,0,0,0,'',0,'',0),(12,NULL,NULL,NULL,0,0,0,'',0,'',0),(13,NULL,NULL,NULL,0,0,0,'',0,'',0),(14,NULL,NULL,NULL,0,0,0,'',0,'',0),(15,NULL,NULL,NULL,0,0,0,'',0,'',0);
/*!40000 ALTER TABLE `samples_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_health_status`
--

LOCK TABLES `samples_health_status` WRITE;
/*!40000 ALTER TABLE `samples_health_status` DISABLE KEYS */;
INSERT INTO `samples_health_status` VALUES (1,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL),(10,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL),(11,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL),(12,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL),(13,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL),(14,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL),(15,'','','',NULL,NULL,'',0,0,'',0,NULL,0,NULL);
/*!40000 ALTER TABLE `samples_health_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_host`
--

LOCK TABLES `samples_host` WRITE;
/*!40000 ALTER TABLE `samples_host` DISABLE KEYS */;
INSERT INTO `samples_host` VALUES (1,1,'SUBJECTID','additional host info',_binary '\0',41,0,'',0,0,'','','',NULL),(10,1,'13333','',_binary '\0',43,1,'',0,0,'','','',NULL),(11,1,'','',_binary '',8,0,'',0,0,'','','',NULL),(12,0,NULL,NULL,NULL,NULL,0,'',0,0,'','','',NULL),(13,0,NULL,NULL,NULL,NULL,0,'',0,0,'','','',NULL),(14,0,NULL,NULL,NULL,NULL,0,'',0,0,'','','',NULL),(15,0,NULL,NULL,NULL,NULL,0,'',0,0,'','','',NULL);
/*!40000 ALTER TABLE `samples_host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_library`
--

LOCK TABLES `samples_library` WRITE;
/*!40000 ALTER TABLE `samples_library` DISABLE KEYS */;
INSERT INTO `samples_library` VALUES (1,NULL,_binary '',9,6,4,'',NULL,300,''),(10,'None',NULL,0,0,0,'Long design description',NULL,300,''),(11,NULL,NULL,0,0,0,'',NULL,NULL,''),(12,NULL,_binary '',0,0,0,'',NULL,0,''),(13,NULL,_binary '',0,0,0,'',NULL,0,''),(14,NULL,_binary '',0,0,0,'',NULL,0,''),(15,NULL,_binary '',0,0,0,'',NULL,0,'');
/*!40000 ALTER TABLE `samples_library` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_location`
--

LOCK TABLES `samples_location` WRITE;
/*!40000 ALTER TABLE `samples_location` DISABLE KEYS */;
INSERT INTO `samples_location` VALUES (1,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL,0),(10,3,207,'Covasna','Sfantu Gheorghe','',12.46,-52.20,0),(11,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL,0),(12,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL,0),(13,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL,0),(14,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL,0),(15,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL,0);
/*!40000 ALTER TABLE `samples_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_patient_treatment`
--

LOCK TABLES `samples_patient_treatment` WRITE;
/*!40000 ALTER TABLE `samples_patient_treatment` DISABLE KEYS */;
INSERT INTO `samples_patient_treatment` VALUES (1,_binary '',NULL,_binary '\0',NULL,0,NULL,'','',''),(10,NULL,NULL,_binary '',NULL,0,NULL,'isolate/ss','',''),(11,NULL,NULL,NULL,NULL,0,NULL,'','',''),(12,NULL,NULL,NULL,NULL,0,NULL,'','',''),(13,NULL,NULL,NULL,NULL,0,NULL,'','',''),(14,NULL,NULL,NULL,NULL,0,NULL,'','',''),(15,NULL,NULL,NULL,NULL,0,NULL,'','','');
/*!40000 ALTER TABLE `samples_patient_treatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_sampling`
--

LOCK TABLES `samples_sampling` WRITE;
/*!40000 ALTER TABLE `samples_sampling` DISABLE KEYS */;
INSERT INTO `samples_sampling` VALUES (1,NULL,7,'',0,'','','',0,0,'','','',0,0,1,0),(10,NULL,0,'',0,'','','',0,0,'','','',0,0,0,0),(11,NULL,0,'',0,'','','',0,0,'','','',0,0,0,0);
/*!40000 ALTER TABLE `samples_sampling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `samples_sequencing`
--

LOCK TABLES `samples_sequencing` WRITE;
/*!40000 ALTER TABLE `samples_sequencing` DISABLE KEYS */;
INSERT INTO `samples_sequencing` VALUES (1,15,3005,0),(10,0,NULL,0),(12,0,NULL,0),(14,0,NULL,0),(15,0,NULL,0);
/*!40000 ALTER TABLE `samples_sequencing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `seqfiles`
--

LOCK TABLES `seqfiles` WRITE;
/*!40000 ALTER TABLE `seqfiles` DISABLE KEYS */;
INSERT INTO `seqfiles` VALUES (1,1,1,_binary '',NULL,3,3),(2,1,1,_binary '',NULL,1,2),(3,1,1,_binary '',NULL,2,1),(4,1,1,_binary '\0',_binary '',NULL,NULL),(5,1,1,_binary '\0',_binary '\0',NULL,NULL),(9,12,1,_binary '',NULL,1,3),(10,10,1,_binary '',NULL,2,4),(11,14,1,_binary '',NULL,2,4),(12,15,1,_binary '',NULL,2,4);
/*!40000 ALTER TABLE `seqfiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-26 11:04:47
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

-- Dump completed on 2021-08-26 11:04:47
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
-- Dumping data for table `virusnames`
--

LOCK TABLES `virusnames` WRITE;
/*!40000 ALTER TABLE `virusnames` DISABLE KEYS */;
INSERT INTO `virusnames` VALUES (1,'gisaid','hCoV-19{{continent}}/{{country}}_PV_{{sample_name}}/{{collection_year}}-gsdgdsg'),(2,'ena-isolate','Sars-CoV-2/{{host_scientific_name}}/{{continent}}/{{country}}-{{collection_month}}/{{collection_year}}');
/*!40000 ALTER TABLE `virusnames` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-26 11:04:47
