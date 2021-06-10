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
-- Table structure for table `assembly_methods`
--

DROP TABLE IF EXISTS `assembly_methods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assembly_methods` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
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
-- Table structure for table `author_groups`
--

DROP TABLE IF EXISTS `author_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author_groups` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` char(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author_groups`
--

LOCK TABLES `author_groups` WRITE;
/*!40000 ALTER TABLE `author_groups` DISABLE KEYS */;
INSERT INTO `author_groups` VALUES (1,'TestGroup'),(2,'TestGroup2');
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
  `first_name` char(150) DEFAULT NULL,
  `middle_name` char(150) DEFAULT NULL,
  `last_name` char(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Szilard','Nabor','Fejer'),(2,'Monika','','Korodi'),(3,'Kinga','','Rakosi');
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
  `author_id` int unsigned NOT NULL,
  `author_group_id` int unsigned NOT NULL,
  `order_index` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors_in_group`
--

LOCK TABLES `authors_in_group` WRITE;
/*!40000 ALTER TABLE `authors_in_group` DISABLE KEYS */;
INSERT INTO `authors_in_group` VALUES (1,1,1,1),(2,2,1,2),(3,3,1,3),(4,1,2,1),(5,2,2,0),(6,3,2,3);
/*!40000 ALTER TABLE `authors_in_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `continents`
--

DROP TABLE IF EXISTS `continents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `continents` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `continents`
--

LOCK TABLES `continents` WRITE;
/*!40000 ALTER TABLE `continents` DISABLE KEYS */;
INSERT INTO `continents` VALUES (1,'Asia',1),(2,'Africa',2),(3,'Europe',3),(4,'North America',4),(5,'South America',5),(6,'Australia/Oceania',6),(7,'Antartica',7);
/*!40000 ALTER TABLE `continents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=279 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'Afghanistan',1),(2,'Albania',2),(3,'Algeria',3),(4,'American Samoa',4),(5,'Andorra',5),(6,'Angola',6),(7,'Anguilla',7),(8,'Antarctica',8),(9,'Antigua and Barbuda',9),(10,'Arctic Ocean',10),(11,'Argentina',11),(12,'Armenia',12),(13,'Aruba',13),(14,'Ashmore and Cartier Islands',14),(15,'Atlantic Ocean',15),(16,'Australia',16),(17,'Austria',17),(18,'Azerbaijan',18),(19,'Bahamas',19),(20,'Bahrain',20),(21,'Baltic Sea',21),(22,'Baker Island',22),(23,'Bangladesh',23),(24,'Barbados',24),(25,'Bassas da India',25),(26,'Belarus',26),(27,'Belgium',27),(28,'Belize',28),(29,'Benin',29),(30,'Bermuda',30),(31,'Bhutan',31),(32,'Bolivia',32),(33,'Borneo',33),(34,'Bosnia and Herzegovina',34),(35,'Botswana',35),(36,'Bouvet Island',36),(37,'Brazil',37),(38,'British Virgin Islands',38),(39,'Brunei',39),(40,'Bulgaria',40),(41,'Burkina Faso',41),(42,'Burundi',42),(43,'Cambodia',43),(44,'Cameroon',44),(45,'Canada',45),(46,'Cape Verde',46),(47,'Cayman Islands',47),(48,'Central African Republic',48),(49,'Chad',49),(50,'Chile',50),(51,'China',51),(52,'Christmas Island',52),(53,'Clipperton Island',53),(54,'Cocos Islands',54),(55,'Colombia',55),(56,'Comoros',56),(57,'Cook Islands',57),(58,'Coral Sea Islands',58),(59,'Costa Rica',59),(60,'Cote d`Ivoire',60),(61,'Croatia',61),(62,'Cuba',62),(63,'Curacao',63),(64,'Cyprus',64),(65,'Czech Republic',65),(66,'Democratic Republic of the Congo',66),(67,'Denmark',67),(68,'Djibouti',68),(69,'Dominica',69),(70,'Dominican Republic',70),(71,'Ecuador',71),(72,'Egypt',72),(73,'El Salvador',73),(74,'Equatorial Guinea',74),(75,'Eritrea',75),(76,'Estonia',76),(77,'Eswatini',77),(78,'Ethiopia',78),(79,'Europa Island',79),(80,'Falkland Islands (Islas Malvinas)',80),(81,'Faroe Islands',81),(82,'Fiji',82),(83,'Finland',83),(84,'France',84),(85,'French Guiana',85),(86,'French Polynesia',86),(87,'French Southern and Antarctic Lands',87),(88,'Gabon',88),(89,'Gambia',89),(90,'Gaza Strip',90),(91,'Georgia',91),(92,'Germany',92),(93,'Ghana',93),(94,'Gibraltar',94),(95,'Glorioso Islands',95),(96,'Greece',96),(97,'Greenland',97),(98,'Grenada',98),(99,'Guadeloupe',99),(100,'Guam',100),(101,'Guatemala',101),(102,'Guernsey',102),(103,'Guinea',103),(104,'Guinea-Bissau',104),(105,'Guyana',105),(106,'Haiti',106),(107,'Heard Island and McDonald Islands',107),(108,'Honduras',108),(109,'Hong Kong',109),(110,'Howland Island',110),(111,'Hungary',111),(112,'Iceland',112),(113,'India',113),(114,'Indian Ocean',114),(115,'Indonesia',115),(116,'Iran',116),(117,'Iraq',117),(118,'Ireland',118),(119,'Isle of Man',119),(120,'Israel',120),(121,'Italy',121),(122,'Jamaica',122),(123,'Jan Mayen',123),(124,'Japan',124),(125,'Jarvis Island',125),(126,'Jersey',126),(127,'Johnston Atoll',127),(128,'Jordan',128),(129,'Juan de Nova Island',129),(130,'Kazakhstan',130),(131,'Kenya',131),(132,'Kerguelen Archipelago',132),(133,'Kingman Reef',133),(134,'Kiribati',134),(135,'Kosovo',135),(136,'Kuwait',136),(137,'Kyrgyzstan',137),(138,'Laos',138),(139,'Latvia',139),(140,'Lebanon',140),(141,'Lesotho',141),(142,'Liberia',142),(143,'Libya',143),(144,'Liechtenstein',144),(145,'Line Islands',145),(146,'Lithuania',146),(147,'Luxembourg',147),(148,'Macau',148),(149,'Madagascar',149),(150,'Malawi',150),(151,'Malaysia',151),(152,'Maldives',152),(153,'Mali',153),(154,'Malta',154),(155,'Marshall Islands',155),(156,'Martinique',156),(157,'Mauritania',157),(158,'Mauritius',158),(159,'Mayotte',159),(160,'Mediterranean Sea',160),(161,'Mexico',161),(162,'Micronesia',162),(163,'Midway Islands',163),(164,'Moldova',164),(165,'Monaco',165),(166,'Mongolia',166),(167,'Montenegro',167),(168,'Montserrat',168),(169,'Morocco',169),(170,'Mozambique',170),(171,'Myanmar',171),(172,'Namibia',172),(173,'Nauru',173),(174,'Navassa Island',174),(175,'Nepal',175),(176,'Netherlands',176),(177,'New Caledonia',177),(178,'New Zealand',178),(179,'Nicaragua',179),(180,'Niger',180),(181,'Nigeria',181),(182,'Niue',182),(183,'Norfolk Island',183),(184,'North Korea',184),(185,'North Macedonia',185),(186,'North Sea',186),(187,'Northern Mariana Islands',187),(188,'Norway',188),(189,'Oman',189),(190,'Pacific Ocean',190),(191,'Pakistan',191),(192,'Palau',192),(193,'Palmyra Atoll',193),(194,'Panama',194),(195,'Papua New Guinea',195),(196,'Paracel Islands',196),(197,'Paraguay',197),(198,'Peru',198),(199,'Philippines',199),(200,'Pitcairn Islands',200),(201,'Poland',201),(202,'Portugal',202),(203,'Puerto Rico',203),(204,'Qatar',204),(205,'Republic of the Congo',205),(206,'Reunion',206),(207,'Romania',207),(208,'Ross Sea',208),(209,'Russia',209),(210,'Rwanda',210),(211,'Saint Helena',211),(212,'Saint Kitts and Nevis',212),(213,'Saint Lucia',213),(214,'Saint Pierre and Miquelon',214),(215,'Saint Vincent and the Grenadines',215),(216,'Samoa',216),(217,'San Marino',217),(218,'Sao Tome and Principe',218),(219,'Saudi Arabia',219),(220,'Senegal',220),(221,'Serbia',221),(222,'Seychelles',222),(223,'Sierra Leone',223),(224,'Singapore',224),(225,'Sint Maarten',225),(226,'Slovakia',226),(227,'Slovenia',227),(228,'Solomon Islands',228),(229,'Somalia',229),(230,'South Africa',230),(231,'South Georgia and the South Sandwich Islands',231),(232,'South Korea',232),(233,'South Sudan',233),(234,'Southern Ocean',234),(235,'Spain',235),(236,'Spratly Islands',236),(237,'Sri Lanka',237),(238,'State of Palestine',238),(239,'Sudan',239),(240,'Suriname',240),(241,'Svalbard',241),(242,'Sweden',242),(243,'Switzerland',243),(244,'Syria',244),(245,'Taiwan',245),(246,'Tajikistan',246),(247,'Tanzania',247),(248,'Tasman Sea',248),(249,'Thailand',249),(250,'Timor-Leste',250),(251,'Togo',251),(252,'Tokelau',252),(253,'Tonga',253),(254,'Trinidad and Tobago',254),(255,'Tromelin Island',255),(256,'Tunisia',256),(257,'Turkey',257),(258,'Turkmenistan',258),(259,'Turks and Caicos Islands',259),(260,'Tuvalu',260),(261,'USA',261),(262,'Uganda',262),(263,'Ukraine',263),(264,'United Arab Emirates',264),(265,'United Kingdom',265),(266,'Uruguay',266),(267,'Uzbekistan',267),(268,'Vanuatu',268),(269,'Venezuela',269),(270,'Viet Nam',270),(271,'Virgin Islands',271),(272,'Wake Island',272),(273,'Wallis and Futuna',273),(274,'West Bank',274),(275,'Western Sahara',275),(276,'Yemen',276),(277,'Zambia',277),(278,'Zimbabwe',278);
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ena_studies`
--

DROP TABLE IF EXISTS `ena_studies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ena_studies` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `project_name` varchar(500) NOT NULL,
  `project_title` varchar(500) NOT NULL,
  `project_alias` varchar(500) NOT NULL,
  `project_description` text NOT NULL,
  `project_link_db` char(100) DEFAULT NULL,
  `project_link_id` char(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_alias` (`project_alias`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ena_studies`
--

LOCK TABLES `ena_studies` WRITE;
/*!40000 ALTER TABLE `ena_studies` DISABLE KEYS */;
/*!40000 ALTER TABLE `ena_studies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_behaviours`
--

DROP TABLE IF EXISTS `host_behaviours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `host_behaviours` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_behaviours`
--

LOCK TABLES `host_behaviours` WRITE;
/*!40000 ALTER TABLE `host_behaviours` DISABLE KEYS */;
INSERT INTO `host_behaviours` VALUES (1,'captive-wild (e.g. at zoo)',1),(2,'domestic',2),(3,'other',3),(4,'wild',4);
/*!40000 ALTER TABLE `host_behaviours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_disease_outcome`
--

DROP TABLE IF EXISTS `host_disease_outcome`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `host_disease_outcome` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_disease_outcome`
--

LOCK TABLES `host_disease_outcome` WRITE;
/*!40000 ALTER TABLE `host_disease_outcome` DISABLE KEYS */;
INSERT INTO `host_disease_outcome` VALUES (1,'dead',1),(2,'recovered',2),(3,'recovered with sequelae',3);
/*!40000 ALTER TABLE `host_disease_outcome` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_habitats`
--

DROP TABLE IF EXISTS `host_habitats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `host_habitats` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_habitats`
--

LOCK TABLES `host_habitats` WRITE;
/*!40000 ALTER TABLE `host_habitats` DISABLE KEYS */;
INSERT INTO `host_habitats` VALUES (1,'domestic:free-range farm',1),(2,'domestic:indoor farm',2),(3,'domestic:live market',3),(4,'domestic:semi-enclosed housing',4),(5,'other',5),(6,'wild:migratory',6),(7,'wild:resident',7);
/*!40000 ALTER TABLE `host_habitats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_health_states`
--

DROP TABLE IF EXISTS `host_health_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `host_health_states` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_health_states`
--

LOCK TABLES `host_health_states` WRITE;
/*!40000 ALTER TABLE `host_health_states` DISABLE KEYS */;
INSERT INTO `host_health_states` VALUES (1,'diseased',1),(2,'healthy',2),(3,'not applicable',3),(4,'not collected',4),(5,'not provided',5),(6,'restricted access',6);
/*!40000 ALTER TABLE `host_health_states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts`
--

DROP TABLE IF EXISTS `hosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hosts` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `latin` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts`
--

LOCK TABLES `hosts` WRITE;
/*!40000 ALTER TABLE `hosts` DISABLE KEYS */;
INSERT INTO `hosts` VALUES (1,'Human','Homo-sapiens',1);
/*!40000 ALTER TABLE `hosts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institutions`
--

DROP TABLE IF EXISTS `institutions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institutions` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` char(200) DEFAULT NULL,
  `street_address` text NOT NULL,
  `postal_code` mediumint unsigned DEFAULT NULL,
  `county` char(100) DEFAULT NULL,
  `country` char(100) DEFAULT NULL,
  `city` char(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institutions`
--

LOCK TABLES `institutions` WRITE;
/*!40000 ALTER TABLE `institutions` DISABLE KEYS */;
INSERT INTO `institutions` VALUES (1,'Pro-Vitam','16 Muncitorilor Street',500123,'Covasna','Romania','Sfantu Gheorghe');
/*!40000 ALTER TABLE `institutions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_selections`
--

DROP TABLE IF EXISTS `library_selections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library_selections` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `item_key` char(200) NOT NULL,
  `item_value` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_key` (`item_key`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_selections`
--

LOCK TABLES `library_selections` WRITE;
/*!40000 ALTER TABLE `library_selections` DISABLE KEYS */;
INSERT INTO `library_selections` VALUES (1,'RANDOM','Random selection by shearing or other method'),(2,'PCR','Source material was selected by designed primers'),(3,'RANDOM PCR','Source material was selected by randomly generated primers'),(4,'RT-PCR','Source material was selected by reverse transcription PCR'),(5,'HMPR','Hypo-methylated partial restriction digest'),(6,'MF','Methyl Filtrated'),(7,'CF-S','Cot-filtered single/low-copy genomic DNA'),(8,'CF-M','Cot-filtered moderately repetitive genomic DNA'),(9,'CF-H','Cot-filtered highly repetitive genomic DNA'),(10,'CF-T','Cot-filtered theoretical single-copy genomic DNA'),(11,'MDA','Multiple displacement amplification'),(12,'MSLL','Methylation Spanning Linking Library'),(13,'cDNA','complementary DNA'),(14,'ChIP','Chromatin immunoprecipitation'),(15,'MNase','Micrococcal Nuclease (MNase) digestion'),(16,'DNAse','Deoxyribonuclease (MNase) digestion'),(17,'Hybrid Selection','Selection by hybridization in array or solution'),(18,'Reduced Representation','Reproducible genomic subsets, often generated by restriction fragment size selection, containing a manageable number of loci to facilitate re-sampling'),(19,'Restriction Digest','DNA fractionation using restriction enzymes'),(20,'5-methylcytidine antibody','Selection of methylated DNA fragments using an antibody raised against 5-methylcytosine or 5-methylcytidine (m5C)'),(21,'MBD2 protein methyl-CpG binding domain','Enrichment by methyl-CpG binding domain'),(22,'CAGE','Cap-analysis gene expression'),(23,'RACE','Rapid Amplification of cDNA Ends'),(24,'size fractionation','Physical selection of size appropriate targets'),(25,'Padlock probes capture method','Circularized oligonucleotide probes'),(26,'other','Other library enrichment, screening, or selection process (please include additional info in the `design description`)'),(27,'unspecified','Library enrichment, screening, or selection is not specified (please include additional info in the `design description`)'),(28,'cDNA_oligo_dT',''),(29,'cDNA_randomPriming',''),(30,'Inverse rRNA','depletion of ribosomal RNA by oligo hybridization.'),(31,'Oligo-dT','enrichment of messenger RNA (mRNA) by hybridization to Oligo-dT.'),(32,'PolyA','PolyA selection or enrichment for messenger RNA (mRNA); should replace cDNA enumeration.'),(33,'repeat fractionation','Selection for less repetitive (and more gene rich) sequence through Cot filtration (CF) or other fractionation techniques based on DNA kinetics.');
/*!40000 ALTER TABLE `library_selections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_sources`
--

DROP TABLE IF EXISTS `library_sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library_sources` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `item_key` char(200) NOT NULL,
  `item_value` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_key` (`item_key`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_sources`
--

LOCK TABLES `library_sources` WRITE;
/*!40000 ALTER TABLE `library_sources` DISABLE KEYS */;
INSERT INTO `library_sources` VALUES (1,'GENOMIC','Genomic DNA (includes PCR products from genomic DNA)'),(2,'TRANSCRIPTOMIC','Transcription products or non genomic DNA (EST, cDNA, RT-PCR, screened libraries)'),(3,'METAGENOMIC','Mixed material from metagenome'),(4,'METATRANSCRIPTOMIC','Transcription products from community targets'),(5,'SYNTHETIC','Synthetic DNA'),(6,'VIRAL RNA','Viral RNA'),(7,'GENOMIC SINGLE CELL',''),(8,'TRANSCRIPTOMIC SINGLE CELL',''),(9,'OTHER','Other, unspecified, or unknown library source material (please include additional info in the `design description`)');
/*!40000 ALTER TABLE `library_sources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_strategies`
--

DROP TABLE IF EXISTS `library_strategies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library_strategies` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `item_key` char(200) NOT NULL,
  `item_value` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_key` (`item_key`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_strategies`
--

LOCK TABLES `library_strategies` WRITE;
/*!40000 ALTER TABLE `library_strategies` DISABLE KEYS */;
INSERT INTO `library_strategies` VALUES (1,'WGA','Random sequencing of the whole genome following non-pcr amplification'),(2,'WGS','Random sequencing of the whole genome'),(3,'WXS','Random sequencing of exonic regions selected from the genome'),(4,'RNA-Seq','Random sequencing of whole transcriptome'),(5,'miRNA-Seq','Random sequencing of small miRNAs'),(6,'WCS','Random sequencing of a whole chromosome or other replicon isolated from a genome'),(7,'CLONE','Genomic clone based (hierarchical) sequencing'),(8,'POOLCLONE','Shotgun of pooled clones (usually BACs and Fosmids)'),(9,'AMPLICON','Sequencing of overlapping or distinct PCR or RT-PCR products'),(10,'CLONEEND','Clone end (5`, 3`, or both) sequencing'),(11,'FINISHING','Sequencing intended to finish (close) gaps in existing coverage'),(12,'ChIP-Seq','Direct sequencing of chromatin immunoprecipitates'),(13,'MNase-Seq','Direct sequencing following MNase digestion'),(14,'DNase-Hypersensitivity','Sequencing of hypersensitive sites, or segments of open chromatin that are more readily cleaved by DNaseI'),(15,'Bisulfite-Seq','Sequencing following treatment of DNA with bisulfite to convert cytosine residues to uracil depending on methylation status'),(16,'Tn-Seq','Sequencing from transposon insertion sites'),(17,'EST','Single pass sequencing of cDNA templates'),(18,'FL-cDNA','Full-length sequencing of cDNA templates'),(19,'CTS','Concatenated Tag Sequencing'),(20,'MRE-Seq','Methylation-Sensitive Restriction Enzyme Sequencing strategy'),(21,'MeDIP-Seq','Methylated DNA Immunoprecipitation Sequencing strategy'),(22,'MBD-Seq','Direct sequencing of methylated fractions sequencing strategy'),(23,'Synthetic-Long-Read',''),(24,'ATAC-seq','Assay for Transposase-Accessible Chromatin (ATAC) strategy is used to study genome-wide chromatin accessibility. alternative method to DNase-seq that uses an engineered Tn5 transposase to cleave DNA and to integrate primer DNA sequences into the cleaved genomic DNA'),(25,'ChIA-PET','Direct sequencing of proximity-ligated chromatin immunoprecipitates.'),(26,'FAIRE-seq','Formaldehyde Assisted Isolation of Regulatory Elements. reveals regions of open chromatin'),(27,'Hi-C','Chromosome Conformation Capture technique where a biotin-labeled nucleotide is incorporated at the ligation junction, enabling selective purification of chimeric DNA ligation junctions followed by deep sequencing'),(28,'ncRNA-Seq','Capture of other non-coding RNA types, including post-translation modification types such as snRNA (small nuclear RNA) or snoRNA (small nucleolar RNA), or expression regulation types such as siRNA (small interfering RNA) or piRNA/piwi/RNA (piwi-interacting RNA).'),(29,'RAD-Seq',''),(30,'RIP-Seq','Direct sequencing of RNA immunoprecipitates (includes CLIP-Seq, HITS-CLIP and PAR-CLIP).'),(31,'SELEX','Systematic Evolution of Ligands by EXponential enrichment'),(32,'ssRNA-seq','strand-specific RNA sequencing'),(33,'Targeted-Capture',''),(34,'Tethered Chromatin Conformation Capture',''),(35,'OTHER','Library strategy not listed (please include additional info in the ` description`)');
/*!40000 ALTER TABLE `library_strategies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passage_details`
--

DROP TABLE IF EXISTS `passage_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passage_details` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passage_details`
--

LOCK TABLES `passage_details` WRITE;
/*!40000 ALTER TABLE `passage_details` DISABLE KEYS */;
INSERT INTO `passage_details` VALUES (1,'Original',1),(2,'Vero',2);
/*!40000 ALTER TABLE `passage_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_statuses`
--

DROP TABLE IF EXISTS `patient_statuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_statuses` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_statuses`
--

LOCK TABLES `patient_statuses` WRITE;
/*!40000 ALTER TABLE `patient_statuses` DISABLE KEYS */;
INSERT INTO `patient_statuses` VALUES (1,'Live',1),(2,'Hospitalized',2),(3,'Released',3),(4,'Deceased',4),(5,'unknown',5);
/*!40000 ALTER TABLE `patient_statuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reference_genomes`
--

DROP TABLE IF EXISTS `reference_genomes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reference_genomes` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reference_genomes`
--

LOCK TABLES `reference_genomes` WRITE;
/*!40000 ALTER TABLE `reference_genomes` DISABLE KEYS */;
/*!40000 ALTER TABLE `reference_genomes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_capture_status`
--

DROP TABLE IF EXISTS `sample_capture_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sample_capture_status` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_capture_status`
--

LOCK TABLES `sample_capture_status` WRITE;
/*!40000 ALTER TABLE `sample_capture_status` DISABLE KEYS */;
INSERT INTO `sample_capture_status` VALUES (1,'active surveillance in response to outbreak',1),(2,'active surveillance not initiated by an outbreak',2),(3,'farm sample',3),(4,'market sample',4),(5,'other',5),(6,'pet sample',6),(7,'zoo sample',7);
/*!40000 ALTER TABLE `sample_capture_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples`
--

DROP TABLE IF EXISTS `samples`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` char(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples`
--

LOCK TABLES `samples` WRITE;
/*!40000 ALTER TABLE `samples` DISABLE KEYS */;
INSERT INTO `samples` VALUES (1,'TEST01'),(3,'TEST02'),(4,'TEST04'),(7,'TEST05');
/*!40000 ALTER TABLE `samples` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples_collection`
--

DROP TABLE IF EXISTS `samples_collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples_collection` (
  `sample_id` int unsigned NOT NULL,
  `year` smallint unsigned NOT NULL,
  `month` tinyint unsigned DEFAULT NULL,
  `day` tinyint unsigned DEFAULT NULL,
  `collector_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`sample_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples_collection`
--

LOCK TABLES `samples_collection` WRITE;
/*!40000 ALTER TABLE `samples_collection` DISABLE KEYS */;
INSERT INTO `samples_collection` VALUES (1,2020,4,8,2),(3,2020,2,4,2),(4,2019,NULL,NULL,3);
/*!40000 ALTER TABLE `samples_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples_health_status`
--

DROP TABLE IF EXISTS `samples_health_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples_health_status` (
  `sample_id` int unsigned NOT NULL,
  `subject_exposure` varchar(600) DEFAULT NULL,
  `subject_exposure_duration` varchar(600) DEFAULT NULL,
  `type_exposure` varchar(600) DEFAULT NULL,
  `hospitalization` bit(1) DEFAULT NULL,
  `ilness_duration` smallint unsigned DEFAULT NULL,
  `ilness_symptoms` varchar(600) DEFAULT NULL,
  `host_disease_outcome_id` tinyint unsigned DEFAULT NULL,
  `host_health_state_id` tinyint unsigned DEFAULT NULL,
  `treatment` varchar(500) DEFAULT NULL,
  `outbreak` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`sample_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples_health_status`
--

LOCK TABLES `samples_health_status` WRITE;
/*!40000 ALTER TABLE `samples_health_status` DISABLE KEYS */;
INSERT INTO `samples_health_status` VALUES (1,'subject expo','expo duration','type of expo',_binary '\0',6,'symptoms',2,3,'drugs','outbreak'),(3,'','','',NULL,NULL,'',0,3,'',''),(4,'','','',NULL,NULL,'',0,5,'','');
/*!40000 ALTER TABLE `samples_health_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples_host`
--

DROP TABLE IF EXISTS `samples_host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples_host` (
  `sample_id` int unsigned NOT NULL,
  `host_id` int unsigned DEFAULT NULL,
  `host_subject_id` varchar(200) DEFAULT NULL,
  `additional_host_info` varchar(200) DEFAULT NULL,
  `patient_gender` bit(1) DEFAULT NULL,
  `patient_age` tinyint unsigned DEFAULT NULL,
  `patient_status_id` int unsigned DEFAULT NULL,
  `last_vaccinated` varchar(200) DEFAULT NULL,
  `ppe` varchar(600) DEFAULT NULL,
  `host_habitat_id` tinyint unsigned DEFAULT NULL,
  `host_behaviour_id` tinyint unsigned DEFAULT NULL,
  `host_description` varchar(1000) DEFAULT NULL,
  `gravidity` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`sample_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples_host`
--

LOCK TABLES `samples_host` WRITE;
/*!40000 ALTER TABLE `samples_host` DISABLE KEYS */;
INSERT INTO `samples_host` VALUES (1,1,'SUBJECTID','additional host info',_binary '',27,2,'last vaccinated','ppe',1,1,'description','no gravidity'),(3,1,'SUBJECTID','additional host info',_binary '',0,1,'last vaccinated','ppe',2,0,'',''),(4,1,'','',NULL,4,3,'','',0,0,'','');
/*!40000 ALTER TABLE `samples_host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples_library`
--

DROP TABLE IF EXISTS `samples_library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples_library` (
  `sample_id` int unsigned NOT NULL,
  `lib_id` varchar(200) DEFAULT NULL,
  `layout_paired` bit(1) DEFAULT NULL,
  `strategy_id` smallint unsigned DEFAULT NULL,
  `source_id` smallint unsigned DEFAULT NULL,
  `selection_id` smallint unsigned DEFAULT NULL,
  `design_description` varchar(1000) DEFAULT NULL,
  `preparation_date` date DEFAULT NULL,
  PRIMARY KEY (`sample_id`),
  UNIQUE KEY `lib_id` (`lib_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples_library`
--

LOCK TABLES `samples_library` WRITE;
/*!40000 ALTER TABLE `samples_library` DISABLE KEYS */;
INSERT INTO `samples_library` VALUES (1,NULL,NULL,0,0,0,'',NULL),(4,'',NULL,0,0,0,'',NULL);
/*!40000 ALTER TABLE `samples_library` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples_location`
--

DROP TABLE IF EXISTS `samples_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples_location` (
  `sample_id` int unsigned NOT NULL,
  `continent_id` tinyint unsigned DEFAULT NULL,
  `country_id` smallint unsigned DEFAULT NULL,
  `region` varchar(150) DEFAULT NULL,
  `locality` varchar(150) DEFAULT NULL,
  `additional_info` varchar(1000) DEFAULT NULL,
  `geo_loc_latitude` decimal(5,2) DEFAULT NULL,
  `geo_loc_longitude` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`sample_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples_location`
--

LOCK TABLES `samples_location` WRITE;
/*!40000 ALTER TABLE `samples_location` DISABLE KEYS */;
INSERT INTO `samples_location` VALUES (0,2,0,'','','',NULL,NULL),(1,3,207,'Covasna','Sfantu Gheorghe','addlocinfo',-11.30,102.02),(3,2,1,'Covasna','Sfantu Gheorghe','addlocinfo',-0.10,-56.02),(4,1,6,'Covasna','Sfantu Gheorghe','addlocinfo',-11.20,52.02),(7,3,207,'Covasna','Sfantu Gheorghe','',NULL,NULL),(10,2,8,'','','',NULL,NULL);
/*!40000 ALTER TABLE `samples_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples_sampling`
--

DROP TABLE IF EXISTS `samples_sampling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples_sampling` (
  `sample_id` int unsigned NOT NULL,
  `originating_lab_id` int unsigned DEFAULT NULL,
  `originating_lab_sample_name` char(200) DEFAULT NULL,
  `submitting_lab_id` int unsigned DEFAULT NULL,
  `submitting_lab_sample_name` char(200) DEFAULT NULL,
  `author_group_id` int unsigned DEFAULT NULL,
  `receipt_date` date DEFAULT NULL,
  `sampling_strategy_id` int unsigned DEFAULT NULL,
  `passage_details_id` int unsigned DEFAULT NULL,
  `isolate` varchar(500) DEFAULT NULL,
  `strain` varchar(500) DEFAULT NULL,
  `isolation_source_host_associated` varchar(600) DEFAULT NULL,
  `isolation_source_non_host_associated` varchar(600) DEFAULT NULL,
  `sample_capture_status_id` tinyint unsigned DEFAULT NULL,
  `specimen_source_id` int unsigned DEFAULT NULL,
  `sample_storage_conditions` varchar(500) DEFAULT NULL,
  `definition_for_seropositive_sample` varchar(500) DEFAULT NULL,
  `serotype` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`sample_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples_sampling`
--

LOCK TABLES `samples_sampling` WRITE;
/*!40000 ALTER TABLE `samples_sampling` DISABLE KEYS */;
INSERT INTO `samples_sampling` VALUES (1,1,'TEST01orig',1,'TEST01submit',1,NULL,3,2,'isolate','strain','isolation host associated','isolation non-=host-associated',2,3,'storage condition','seropositive definiton','serotype'),(3,1,'',1,'',2,NULL,0,1,'','','','',0,0,'','',''),(4,1,'',1,'',1,NULL,0,2,'isolate','','','',0,0,'','','');
/*!40000 ALTER TABLE `samples_sampling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `samples_sequencing`
--

DROP TABLE IF EXISTS `samples_sequencing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samples_sequencing` (
  `sample_id` int unsigned NOT NULL,
  `sequencing_instrument_id` int unsigned DEFAULT NULL,
  `assembly_method_id` int unsigned DEFAULT NULL,
  `coverage` mediumint unsigned DEFAULT NULL,
  PRIMARY KEY (`sample_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `samples_sequencing`
--

LOCK TABLES `samples_sequencing` WRITE;
/*!40000 ALTER TABLE `samples_sequencing` DISABLE KEYS */;
INSERT INTO `samples_sequencing` VALUES (1,15,3,591),(3,19,0,NULL),(4,8,0,NULL);
/*!40000 ALTER TABLE `samples_sequencing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sampling_strategies`
--

DROP TABLE IF EXISTS `sampling_strategies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sampling_strategies` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
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
-- Table structure for table `seqfile_extensions`
--

DROP TABLE IF EXISTS `seqfile_extensions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seqfile_extensions` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `item_key` char(200) NOT NULL,
  `item_value` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_key` (`item_key`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seqfile_extensions`
--

LOCK TABLES `seqfile_extensions` WRITE;
/*!40000 ALTER TABLE `seqfile_extensions` DISABLE KEYS */;
INSERT INTO `seqfile_extensions` VALUES (1,'fasta','fasta'),(2,'bam','bam'),(3,'sam','sam'),(4,'fastq','fastq');
/*!40000 ALTER TABLE `seqfile_extensions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seqfiles`
--

DROP TABLE IF EXISTS `seqfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seqfiles` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sample_id` int unsigned NOT NULL,
  `file_type_id` int unsigned DEFAULT NULL,
  `is_assembly` bit(1) DEFAULT NULL,
  `is_forward_read` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seqfiles`
--

LOCK TABLES `seqfiles` WRITE;
/*!40000 ALTER TABLE `seqfiles` DISABLE KEYS */;
INSERT INTO `seqfiles` VALUES (1,1,1,_binary '',NULL),(4,4,1,_binary '',NULL);
/*!40000 ALTER TABLE `seqfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sequencing_instruments`
--

DROP TABLE IF EXISTS `sequencing_instruments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sequencing_instruments` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `platform_id` int unsigned DEFAULT NULL,
  `label` char(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sequencing_instruments`
--

LOCK TABLES `sequencing_instruments` WRITE;
/*!40000 ALTER TABLE `sequencing_instruments` DISABLE KEYS */;
INSERT INTO `sequencing_instruments` VALUES (1,1,'454 GS'),(2,1,'454 GS 20'),(3,1,'454 GS FLX'),(4,1,'454 GS FLX+'),(5,1,'454 GS FLX Titanium'),(6,1,'454 GS Junior'),(7,2,'AB 5500 Genetic Analyzer'),(8,2,'AB 5500xl Genetic Analyzer'),(9,2,'AB 5500x-Wl Genetic Analyzer'),(10,2,'AB SOLiD 3 Plus System'),(11,2,'AB SOLiD 4 System'),(12,2,'AB SOLiD 4hq System'),(13,2,'AB SOLiD PI System'),(14,2,'AB SOLiD System'),(15,2,'AB SOLiD System 2.0'),(16,2,'AB SOLiD System 3.0'),(17,3,'BGISEQ-500'),(18,4,'AB 310 Genetic A:nalyzer'),(19,4,'AB 3130 Genetic Analyzer'),(20,4,'AB 3130xL Genetic Analyzer'),(21,4,'AB 3500 Genetic Analyzer'),(22,4,'AB 3500xL Genetic Analyzer'),(23,4,'AB 3730 Genetic Analyzer'),(24,4,'AB 3730xL Genetic Analyzer'),(25,5,'Complete Genomics'),(26,6,'Helicos HeliScope'),(27,7,'HiSeq X Five'),(28,7,'HiSeq X Ten'),(29,7,'Illumina Genome Analyzer'),(30,7,'Illumina Genome Analyzer II'),(31,7,'Illumina Genome Analyzer IIx'),(32,7,'Illumina HiScanSQ'),(33,7,'Illumina HiSeq 1000'),(34,7,'Illumina HiSeq 1500'),(35,7,'Illumina HiSeq 2000'),(36,7,'Illumina HiSeq 2500'),(37,7,'Illumina HiSeq 3000'),(38,7,'Illumina HiSeq 4000'),(39,7,'Illumina iSeq 100'),(40,7,'Illumina NovaSeq 6000'),(41,7,'Illumina MiniSeq'),(42,7,'Illumina MiSeq'),(43,7,'NextSeq 500'),(44,7,'NextSeq 550'),(45,8,'Ion Torrent Proton'),(46,8,'Ion Torrent S5 XL'),(47,8,'Ion Torrent S5'),(48,9,'GridION'),(49,9,'MinION'),(50,9,'PromethION'),(51,10,'PacBio RS II'),(52,10,'PacBio Sequel'),(53,10,'PacBio Sequel II');
/*!40000 ALTER TABLE `sequencing_instruments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sequencing_platforms`
--

DROP TABLE IF EXISTS `sequencing_platforms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sequencing_platforms` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sequencing_platforms`
--

LOCK TABLES `sequencing_platforms` WRITE;
/*!40000 ALTER TABLE `sequencing_platforms` DISABLE KEYS */;
INSERT INTO `sequencing_platforms` VALUES (1,'LS454',1),(2,'ABI_SOLID',2),(3,'BGISEQ',3),(4,'CAPILLARY',4),(5,'COMPLETE_GENOMICS',5),(6,'HELICOS',6),(7,'ILLUMINA',7),(8,'ION_TORRENT',8),(9,'OXFORD_NANOPORE',9),(10,'PACBIO_SMRT',10);
/*!40000 ALTER TABLE `sequencing_platforms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sequencing_technologies`
--

DROP TABLE IF EXISTS `sequencing_technologies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sequencing_technologies` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
  `indx` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sequencing_technologies`
--

LOCK TABLES `sequencing_technologies` WRITE;
/*!40000 ALTER TABLE `sequencing_technologies` DISABLE KEYS */;
INSERT INTO `sequencing_technologies` VALUES (1,'Illumina Miseq',1);
/*!40000 ALTER TABLE `sequencing_technologies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specimen_sources`
--

DROP TABLE IF EXISTS `specimen_sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specimen_sources` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `label` char(200) DEFAULT NULL,
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
INSERT INTO `specimen_sources` VALUES (1,'Sputum',1),(2,'Alveolar lavage fluid',2),(3,'Oro-pharyngeal swab',3),(4,'Blood',4),(5,'Tracheal swab',5),(6,'Urine',6),(7,'Stool',7),(8,'Cloakal swab',8),(9,'Organ',9),(10,'Feces',10),(11,'Other',11);
/*!40000 ALTER TABLE `specimen_sources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_assembly_methods`
--

DROP TABLE IF EXISTS `view_assembly_methods`;
/*!50001 DROP VIEW IF EXISTS `view_assembly_methods`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_assembly_methods` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_authors`
--

DROP TABLE IF EXISTS `view_authors`;
/*!50001 DROP VIEW IF EXISTS `view_authors`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_authors` AS SELECT 
 1 AS `id`,
 1 AS `first_name`,
 1 AS `middle_name`,
 1 AS `last_name`,
 1 AS `full_name`,
 1 AS `abbreviated_middle_name`*/;
SET character_set_client = @saved_cs_client;

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
 1 AS `full_name`,
 1 AS `abbreviated_middle_name`,
 1 AS `order_index`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_authors_in_groups_condensed`
--

DROP TABLE IF EXISTS `view_authors_in_groups_condensed`;
/*!50001 DROP VIEW IF EXISTS `view_authors_in_groups_condensed`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_authors_in_groups_condensed` AS SELECT 
 1 AS `group_id`,
 1 AS `group_name`,
 1 AS `members_count`,
 1 AS `full_names`,
 1 AS `abbreviated_middle_names`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_continents`
--

DROP TABLE IF EXISTS `view_continents`;
/*!50001 DROP VIEW IF EXISTS `view_continents`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_continents` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_countries`
--

DROP TABLE IF EXISTS `view_countries`;
/*!50001 DROP VIEW IF EXISTS `view_countries`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_countries` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_hosts`
--

DROP TABLE IF EXISTS `view_hosts`;
/*!50001 DROP VIEW IF EXISTS `view_hosts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_hosts` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `latin`,
 1 AS `display_label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_institutions`
--

DROP TABLE IF EXISTS `view_institutions`;
/*!50001 DROP VIEW IF EXISTS `view_institutions`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_institutions` AS SELECT 
 1 AS `id`,
 1 AS `name`,
 1 AS `address`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_passage_details`
--

DROP TABLE IF EXISTS `view_passage_details`;
/*!50001 DROP VIEW IF EXISTS `view_passage_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_passage_details` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_patient_statuses`
--

DROP TABLE IF EXISTS `view_patient_statuses`;
/*!50001 DROP VIEW IF EXISTS `view_patient_statuses`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_patient_statuses` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_reference_genomes`
--

DROP TABLE IF EXISTS `view_reference_genomes`;
/*!50001 DROP VIEW IF EXISTS `view_reference_genomes`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_reference_genomes` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_base`
--

DROP TABLE IF EXISTS `view_samples_base`;
/*!50001 DROP VIEW IF EXISTS `view_samples_base`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_base` AS SELECT 
 1 AS `sample_id`,
 1 AS `sample_name`,
 1 AS `continent_id`,
 1 AS `country_id`,
 1 AS `region`,
 1 AS `locality`,
 1 AS `geo_loc_latitude`,
 1 AS `geo_loc_longitude`,
 1 AS `additional_location_info`,
 1 AS `collection_year`,
 1 AS `collection_month`,
 1 AS `collection_day`,
 1 AS `collector_id`,
 1 AS `library_id`,
 1 AS `library_layout_paired`,
 1 AS `library_strategy_id`,
 1 AS `library_source_id`,
 1 AS `library_selection_id`,
 1 AS `library_design_description`,
 1 AS `library_preparation_date`,
 1 AS `host_id`,
 1 AS `host_subject_id`,
 1 AS `additional_host_info`,
 1 AS `patient_gender`,
 1 AS `patient_age`,
 1 AS `patient_status_id`,
 1 AS `last_vaccinated`,
 1 AS `ppe`,
 1 AS `host_habitat_id`,
 1 AS `host_behaviour_id`,
 1 AS `host_description`,
 1 AS `gravidity`,
 1 AS `originating_lab_id`,
 1 AS `originating_lab_sample_name`,
 1 AS `submitting_lab_id`,
 1 AS `submitting_lab_sample_name`,
 1 AS `author_group_id`,
 1 AS `receipt_date`,
 1 AS `sampling_strategy_id`,
 1 AS `passage_details_id`,
 1 AS `isolate`,
 1 AS `strain`,
 1 AS `isolation_source_host_associated`,
 1 AS `isolation_source_non_host_associated`,
 1 AS `sample_capture_status_id`,
 1 AS `specimen_source_id`,
 1 AS `sample_storage_conditions`,
 1 AS `definition_for_seropositive_sample`,
 1 AS `serotype`,
 1 AS `subject_exposure`,
 1 AS `subject_exposure_duration`,
 1 AS `type_exposure`,
 1 AS `hospitalization`,
 1 AS `ilness_duration`,
 1 AS `ilness_symptoms`,
 1 AS `host_disease_outcome_id`,
 1 AS `host_health_state_id`,
 1 AS `treatment`,
 1 AS `outbreak`,
 1 AS `sequencing_instrument_id`,
 1 AS `assembly_method_id`,
 1 AS `coverage`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_colleciton`
--

DROP TABLE IF EXISTS `view_samples_colleciton`;
/*!50001 DROP VIEW IF EXISTS `view_samples_colleciton`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_colleciton` AS SELECT 
 1 AS `sample_id`,
 1 AS `collection_year`,
 1 AS `collection_month`,
 1 AS `collection_day`,
 1 AS `collection_date`,
 1 AS `collector_abbreviated_middle_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_collection`
--

DROP TABLE IF EXISTS `view_samples_collection`;
/*!50001 DROP VIEW IF EXISTS `view_samples_collection`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_collection` AS SELECT 
 1 AS `sample_id`,
 1 AS `collection_year`,
 1 AS `collection_month`,
 1 AS `collection_day`,
 1 AS `collection_date`,
 1 AS `collector_abbreviated_middle_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_details`
--

DROP TABLE IF EXISTS `view_samples_details`;
/*!50001 DROP VIEW IF EXISTS `view_samples_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_details` AS SELECT 
 1 AS `sample_id`,
 1 AS `sample_name`,
 1 AS `location`,
 1 AS `additional_location_info`,
 1 AS `geo_loc_latitude`,
 1 AS `geo_loc_longitude`,
 1 AS `collection_date`,
 1 AS `collector_name`,
 1 AS `library_id`,
 1 AS `library_layout`,
 1 AS `library_strategy`,
 1 AS `library_source`,
 1 AS `library_selection`,
 1 AS `library_design_description`,
 1 AS `host_name`,
 1 AS `host_subject_id`,
 1 AS `additional_host_info`,
 1 AS `patient_age`,
 1 AS `patient_gender`,
 1 AS `patient_status`,
 1 AS `last_vaccinated`,
 1 AS `host_habitat`,
 1 AS `host_behaviour`,
 1 AS `host_decription`,
 1 AS `host_gravidity`,
 1 AS `originating_lab_name`,
 1 AS `submitting_lab_name`,
 1 AS `passage_details`,
 1 AS `sampling_strategy`,
 1 AS `author_group_name`,
 1 AS `authors_list`,
 1 AS `isolate`,
 1 AS `strain`,
 1 AS `sample_capture_status`,
 1 AS `specimen_source`,
 1 AS `subject_exposure`,
 1 AS `subject_exposure_duration`,
 1 AS `type_exposure`,
 1 AS `hospitalization`,
 1 AS `ilness_duration`,
 1 AS `ilness_symptoms`,
 1 AS `host_disease_outcome`,
 1 AS `treatment`,
 1 AS `outbreak`,
 1 AS `sequencing_instrument`,
 1 AS `sequencing_platform`,
 1 AS `assembly_method`,
 1 AS `coverage`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_display`
--

DROP TABLE IF EXISTS `view_samples_display`;
/*!50001 DROP VIEW IF EXISTS `view_samples_display`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_display` AS SELECT 
 1 AS `sample_id`,
 1 AS `sample_name`,
 1 AS `collection_date`,
 1 AS `group_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_ena`
--

DROP TABLE IF EXISTS `view_samples_ena`;
/*!50001 DROP VIEW IF EXISTS `view_samples_ena`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_ena` AS SELECT 
 1 AS `sample_id`,
 1 AS `sample_name`,
 1 AS `virus identifier`,
 1 AS `subject exposure`,
 1 AS `subject exposure duration`,
 1 AS `type exposure`,
 1 AS `personal protective equipment`,
 1 AS `hospitalisation`,
 1 AS `ilness duration`,
 1 AS `ilness symptoms`,
 1 AS `collection date`,
 1 AS `geographic location (country and/or sea)`,
 1 AS `geographic location (latitude)`,
 1 AS `geographic location (longitude)`,
 1 AS `geographic location (region and locality)`,
 1 AS `sample capture status`,
 1 AS `host disease outcome`,
 1 AS `host common name`,
 1 AS `host subject id`,
 1 AS `host age`,
 1 AS `host sex`,
 1 AS `host health state`,
 1 AS `host scientific name`,
 1 AS `collector name`,
 1 AS `collecting institution`,
 1 AS `sample storage conditions`,
 1 AS `definition for seropositive sample`,
 1 AS `serotype (required for a seropositive sample)`,
 1 AS `isolate`,
 1 AS `strain`,
 1 AS `host habitat`,
 1 AS `isolation source host associated`,
 1 AS `host description`,
 1 AS `gravidity`,
 1 AS `host behaviour`,
 1 AS `isolation source non-host-associated`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_ena_experiment`
--

DROP TABLE IF EXISTS `view_samples_ena_experiment`;
/*!50001 DROP VIEW IF EXISTS `view_samples_ena_experiment`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_ena_experiment` AS SELECT 
 1 AS `sample_id`,
 1 AS `sample_name`,
 1 AS `library_name`,
 1 AS `library_strategy`,
 1 AS `library_source`,
 1 AS `library_selection`,
 1 AS `library_design_description`,
 1 AS `is_paired`,
 1 AS `library_preparation_date`,
 1 AS `sequencing_platform`,
 1 AS `sequencing_instrument`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_gisaid`
--

DROP TABLE IF EXISTS `view_samples_gisaid`;
/*!50001 DROP VIEW IF EXISTS `view_samples_gisaid`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_gisaid` AS SELECT 
 1 AS `sample_id`,
 1 AS `sample_name`,
 1 AS `passage_details`,
 1 AS `collection_date`,
 1 AS `location`,
 1 AS `continent`,
 1 AS `country`,
 1 AS `region`,
 1 AS `locality`,
 1 AS `additional_location_info`,
 1 AS `host`,
 1 AS `additional_host_info`,
 1 AS `sampling_strategy`,
 1 AS `patient_gender`,
 1 AS `patient_age`,
 1 AS `patient_status`,
 1 AS `specimen_source`,
 1 AS `outbreak`,
 1 AS `last_vaccinated`,
 1 AS `treatment`,
 1 AS `sequencing_technology`,
 1 AS `assembly_method`,
 1 AS `coverage`,
 1 AS `originating_lab_name`,
 1 AS `originating_lab_address`,
 1 AS `originating_lab_sample_name`,
 1 AS `submitting_lab_name`,
 1 AS `submitting_lab_address`,
 1 AS `submitting_lab_sample_name`,
 1 AS `authors_list`,
 1 AS `seqfilename`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_health_status`
--

DROP TABLE IF EXISTS `view_samples_health_status`;
/*!50001 DROP VIEW IF EXISTS `view_samples_health_status`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_health_status` AS SELECT 
 1 AS `sample_id`,
 1 AS `subject_exposure`,
 1 AS `subject_exposure_duration`,
 1 AS `type_exposure`,
 1 AS `hospitalization`,
 1 AS `ilness_duration`,
 1 AS `ilness_duration_days`,
 1 AS `ilness_symptoms`,
 1 AS `host_disease_outcome`,
 1 AS `host_health_state`,
 1 AS `treatment`,
 1 AS `outbreak`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_host`
--

DROP TABLE IF EXISTS `view_samples_host`;
/*!50001 DROP VIEW IF EXISTS `view_samples_host`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_host` AS SELECT 
 1 AS `sample_id`,
 1 AS `host_common_name`,
 1 AS `host_scientific_name`,
 1 AS `host_name`,
 1 AS `host_subject_id`,
 1 AS `additional_host_info`,
 1 AS `patient_age`,
 1 AS `patient_gender`,
 1 AS `patient_gender_ena`,
 1 AS `patient_status`,
 1 AS `ppe`,
 1 AS `last_vaccinated`,
 1 AS `host_habitat`,
 1 AS `host_behaviour`,
 1 AS `host_description`,
 1 AS `host_gravidity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_library`
--

DROP TABLE IF EXISTS `view_samples_library`;
/*!50001 DROP VIEW IF EXISTS `view_samples_library`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_library` AS SELECT 
 1 AS `sample_id`,
 1 AS `library_id`,
 1 AS `layout_paired`,
 1 AS `library_layout`,
 1 AS `library_strategy`,
 1 AS `library_source`,
 1 AS `library_selection`,
 1 AS `library_design_description`,
 1 AS `library_preparation_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_location`
--

DROP TABLE IF EXISTS `view_samples_location`;
/*!50001 DROP VIEW IF EXISTS `view_samples_location`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_location` AS SELECT 
 1 AS `sample_id`,
 1 AS `location`,
 1 AS `continent`,
 1 AS `country`,
 1 AS `region`,
 1 AS `locality`,
 1 AS `additional_location_info`,
 1 AS `geo_loc_latitude`,
 1 AS `geo_loc_longitude`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_ncbi_sra`
--

DROP TABLE IF EXISTS `view_samples_ncbi_sra`;
/*!50001 DROP VIEW IF EXISTS `view_samples_ncbi_sra`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_ncbi_sra` AS SELECT 
 1 AS `sample_id`,
 1 AS `library_name`,
 1 AS `library_strategy`,
 1 AS `library_source`,
 1 AS `library_selection`,
 1 AS `library_layout`,
 1 AS `library_design_description`,
 1 AS `title`,
 1 AS `sequencing_platform`,
 1 AS `sequencing_instrument`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_sampling`
--

DROP TABLE IF EXISTS `view_samples_sampling`;
/*!50001 DROP VIEW IF EXISTS `view_samples_sampling`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_sampling` AS SELECT 
 1 AS `sample_id`,
 1 AS `originating_lab_name`,
 1 AS `originating_lab_address`,
 1 AS `originating_lab_sample_name`,
 1 AS `submitting_lab_name`,
 1 AS `submitting_lab_address`,
 1 AS `submitting_lab_sample_name`,
 1 AS `passage_details`,
 1 AS `sampling_strategy`,
 1 AS `author_group_name`,
 1 AS `authors_list`,
 1 AS `isolate`,
 1 AS `strain`,
 1 AS `isolation_source_host_associated`,
 1 AS `isolation_source_non_host_associated`,
 1 AS `sample_capture_status`,
 1 AS `specimen_source`,
 1 AS `sample_storage_conditions`,
 1 AS `definition_for_seropositive_sample`,
 1 AS `serotype`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_samples_sequencing`
--

DROP TABLE IF EXISTS `view_samples_sequencing`;
/*!50001 DROP VIEW IF EXISTS `view_samples_sequencing`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_samples_sequencing` AS SELECT 
 1 AS `sample_id`,
 1 AS `sequencing_instrument`,
 1 AS `sequencing_platform`,
 1 AS `assembly_method`,
 1 AS `coverage`,
 1 AS `coverage_x`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_sampling_strategies`
--

DROP TABLE IF EXISTS `view_sampling_strategies`;
/*!50001 DROP VIEW IF EXISTS `view_sampling_strategies`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_sampling_strategies` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_seqfiles`
--

DROP TABLE IF EXISTS `view_seqfiles`;
/*!50001 DROP VIEW IF EXISTS `view_seqfiles`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_seqfiles` AS SELECT 
 1 AS `sample_id`,
 1 AS `file_type`,
 1 AS `file_extension`,
 1 AS `is_assembly`,
 1 AS `is_forward_read`,
 1 AS `filename`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_sequencing_technologies`
--

DROP TABLE IF EXISTS `view_sequencing_technologies`;
/*!50001 DROP VIEW IF EXISTS `view_sequencing_technologies`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_sequencing_technologies` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_specimen_sources`
--

DROP TABLE IF EXISTS `view_specimen_sources`;
/*!50001 DROP VIEW IF EXISTS `view_specimen_sources`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_specimen_sources` AS SELECT 
 1 AS `id`,
 1 AS `label`,
 1 AS `indx`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `virusnames`
--

DROP TABLE IF EXISTS `virusnames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `virusnames` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `item_key` char(200) NOT NULL,
  `item_value` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_key` (`item_key`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `virusnames`
--

LOCK TABLES `virusnames` WRITE;
/*!40000 ALTER TABLE `virusnames` DISABLE KEYS */;
INSERT INTO `virusnames` VALUES (1,'gisaid','{{location}}_PV_{{sample_name}}{{collection_year}}');
/*!40000 ALTER TABLE `virusnames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `view_assembly_methods`
--

/*!50001 DROP VIEW IF EXISTS `view_assembly_methods`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_assembly_methods` AS select `assembly_methods`.`id` AS `id`,`assembly_methods`.`label` AS `label`,`assembly_methods`.`indx` AS `indx` from `assembly_methods` where (`assembly_methods`.`indx` <> 0) order by `assembly_methods`.`indx`,`assembly_methods`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_authors`
--

/*!50001 DROP VIEW IF EXISTS `view_authors`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_authors` AS select `authors`.`id` AS `id`,`authors`.`first_name` AS `first_name`,`authors`.`middle_name` AS `middle_name`,`authors`.`last_name` AS `last_name`,concat(`authors`.`first_name`,' ',if(((`authors`.`middle_name` = '') or (`authors`.`middle_name` is null)),'',concat(`authors`.`middle_name`,' ')),`authors`.`last_name`) AS `full_name`,concat(`authors`.`first_name`,' ',if(((`authors`.`middle_name` = '') or (`authors`.`middle_name` is null)),'',concat(left(`authors`.`middle_name`,1),'. ')),`authors`.`last_name`) AS `abbreviated_middle_name` from `authors` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

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
/*!50001 VIEW `view_authors_in_groups` AS select `groups`.`id` AS `group_id`,`groups`.`name` AS `group_name`,`authors`.`id` AS `author_id`,`authors`.`first_name` AS `first_name`,`authors`.`middle_name` AS `middle_name`,`authors`.`last_name` AS `last_name`,`authors`.`full_name` AS `full_name`,`authors`.`abbreviated_middle_name` AS `abbreviated_middle_name`,`aig`.`order_index` AS `order_index` from ((`author_groups` `groups` left join `authors_in_group` `aig` on((`aig`.`author_group_id` = `groups`.`id`))) left join `view_authors` `authors` on((`aig`.`author_id` = `authors`.`id`))) where (`aig`.`order_index` > 0) order by `groups`.`id`,`aig`.`order_index` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_authors_in_groups_condensed`
--

/*!50001 DROP VIEW IF EXISTS `view_authors_in_groups_condensed`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_authors_in_groups_condensed` AS select `view_authors_in_groups`.`group_id` AS `group_id`,`view_authors_in_groups`.`group_name` AS `group_name`,count(`view_authors_in_groups`.`group_id`) AS `members_count`,group_concat(`view_authors_in_groups`.`full_name` order by `view_authors_in_groups`.`order_index` ASC separator ', ') AS `full_names`,group_concat(`view_authors_in_groups`.`abbreviated_middle_name` order by `view_authors_in_groups`.`order_index` ASC separator ', ') AS `abbreviated_middle_names` from `view_authors_in_groups` group by `view_authors_in_groups`.`group_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_continents`
--

/*!50001 DROP VIEW IF EXISTS `view_continents`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_continents` AS select `continents`.`id` AS `id`,`continents`.`label` AS `label`,`continents`.`indx` AS `indx` from `continents` where (`continents`.`indx` <> 0) order by `continents`.`indx`,`continents`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_countries`
--

/*!50001 DROP VIEW IF EXISTS `view_countries`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_countries` AS select `countries`.`id` AS `id`,`countries`.`label` AS `label`,`countries`.`indx` AS `indx` from `countries` where (`countries`.`indx` <> 0) order by `countries`.`indx`,`countries`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_hosts`
--

/*!50001 DROP VIEW IF EXISTS `view_hosts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_hosts` AS select `hosts`.`id` AS `id`,`hosts`.`label` AS `label`,`hosts`.`latin` AS `latin`,concat(`hosts`.`label`,' (',`hosts`.`latin`,')') AS `display_label`,`hosts`.`indx` AS `indx` from `hosts` where (`hosts`.`id` <> 0) order by `hosts`.`indx`,`hosts`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_institutions`
--

/*!50001 DROP VIEW IF EXISTS `view_institutions`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_institutions` AS select `institutions`.`id` AS `id`,`institutions`.`name` AS `name`,concat(`institutions`.`street_address`,', ',`institutions`.`city`,' ',`institutions`.`postal_code`,', ',`institutions`.`county`,', ',`institutions`.`country`) AS `address` from `institutions` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_passage_details`
--

/*!50001 DROP VIEW IF EXISTS `view_passage_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_passage_details` AS select `passage_details`.`id` AS `id`,`passage_details`.`label` AS `label`,`passage_details`.`indx` AS `indx` from `passage_details` where (`passage_details`.`indx` <> 0) order by `passage_details`.`indx`,`passage_details`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_patient_statuses`
--

/*!50001 DROP VIEW IF EXISTS `view_patient_statuses`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_patient_statuses` AS select `patient_statuses`.`id` AS `id`,`patient_statuses`.`label` AS `label`,`patient_statuses`.`indx` AS `indx` from `patient_statuses` where (`patient_statuses`.`indx` <> 0) order by `patient_statuses`.`indx`,`patient_statuses`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_reference_genomes`
--

/*!50001 DROP VIEW IF EXISTS `view_reference_genomes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_reference_genomes` AS select `reference_genomes`.`id` AS `id`,`reference_genomes`.`label` AS `label`,`reference_genomes`.`indx` AS `indx` from `reference_genomes` where (`reference_genomes`.`indx` <> 0) order by `reference_genomes`.`indx`,`reference_genomes`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_base`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_base`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_base` AS select `samples`.`id` AS `sample_id`,`samples`.`name` AS `sample_name`,`location`.`continent_id` AS `continent_id`,`location`.`country_id` AS `country_id`,`location`.`region` AS `region`,`location`.`locality` AS `locality`,`location`.`geo_loc_latitude` AS `geo_loc_latitude`,`location`.`geo_loc_longitude` AS `geo_loc_longitude`,`location`.`additional_info` AS `additional_location_info`,`collection`.`year` AS `collection_year`,`collection`.`month` AS `collection_month`,`collection`.`day` AS `collection_day`,`collection`.`collector_id` AS `collector_id`,`library`.`lib_id` AS `library_id`,`library`.`layout_paired` AS `library_layout_paired`,`library`.`strategy_id` AS `library_strategy_id`,`library`.`source_id` AS `library_source_id`,`library`.`selection_id` AS `library_selection_id`,`library`.`design_description` AS `library_design_description`,`library`.`preparation_date` AS `library_preparation_date`,`host`.`host_id` AS `host_id`,`host`.`host_subject_id` AS `host_subject_id`,`host`.`additional_host_info` AS `additional_host_info`,`host`.`patient_gender` AS `patient_gender`,`host`.`patient_age` AS `patient_age`,`host`.`patient_status_id` AS `patient_status_id`,`host`.`last_vaccinated` AS `last_vaccinated`,`host`.`ppe` AS `ppe`,`host`.`host_habitat_id` AS `host_habitat_id`,`host`.`host_behaviour_id` AS `host_behaviour_id`,`host`.`host_description` AS `host_description`,`host`.`gravidity` AS `gravidity`,`sampling`.`originating_lab_id` AS `originating_lab_id`,`sampling`.`originating_lab_sample_name` AS `originating_lab_sample_name`,`sampling`.`submitting_lab_id` AS `submitting_lab_id`,`sampling`.`submitting_lab_sample_name` AS `submitting_lab_sample_name`,`sampling`.`author_group_id` AS `author_group_id`,`sampling`.`receipt_date` AS `receipt_date`,`sampling`.`sampling_strategy_id` AS `sampling_strategy_id`,`sampling`.`passage_details_id` AS `passage_details_id`,`sampling`.`isolate` AS `isolate`,`sampling`.`strain` AS `strain`,`sampling`.`isolation_source_host_associated` AS `isolation_source_host_associated`,`sampling`.`isolation_source_non_host_associated` AS `isolation_source_non_host_associated`,`sampling`.`sample_capture_status_id` AS `sample_capture_status_id`,`sampling`.`specimen_source_id` AS `specimen_source_id`,`sampling`.`sample_storage_conditions` AS `sample_storage_conditions`,`sampling`.`definition_for_seropositive_sample` AS `definition_for_seropositive_sample`,`sampling`.`serotype` AS `serotype`,`health`.`subject_exposure` AS `subject_exposure`,`health`.`subject_exposure_duration` AS `subject_exposure_duration`,`health`.`type_exposure` AS `type_exposure`,`health`.`hospitalization` AS `hospitalization`,`health`.`ilness_duration` AS `ilness_duration`,`health`.`ilness_symptoms` AS `ilness_symptoms`,`health`.`host_disease_outcome_id` AS `host_disease_outcome_id`,`health`.`host_health_state_id` AS `host_health_state_id`,`health`.`treatment` AS `treatment`,`health`.`outbreak` AS `outbreak`,`sequencing`.`sequencing_instrument_id` AS `sequencing_instrument_id`,`sequencing`.`assembly_method_id` AS `assembly_method_id`,`sequencing`.`coverage` AS `coverage` from (((((((`samples` left join `samples_location` `location` on((`samples`.`id` = `location`.`sample_id`))) left join `samples_collection` `collection` on((`samples`.`id` = `collection`.`sample_id`))) left join `samples_library` `library` on((`samples`.`id` = `library`.`sample_id`))) left join `samples_host` `host` on((`samples`.`id` = `host`.`sample_id`))) left join `samples_sampling` `sampling` on((`samples`.`id` = `sampling`.`sample_id`))) left join `samples_health_status` `health` on((`samples`.`id` = `health`.`sample_id`))) left join `samples_sequencing` `sequencing` on((`samples`.`id` = `sequencing`.`sample_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_colleciton`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_colleciton`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_colleciton` AS select `coll`.`sample_id` AS `sample_id`,`coll`.`year` AS `collection_year`,`coll`.`month` AS `collection_month`,`coll`.`day` AS `collection_day`,concat(`coll`.`year`,if(((`coll`.`month` > 0) and (`coll`.`month` is not null)),concat('-',lpad(`coll`.`month`,2,0),if(((`coll`.`day` > 0) and (`coll`.`day` is not null)),concat('-',lpad(`coll`.`day`,2,0)),'')),'')) AS `collection_date`,`authors`.`abbreviated_middle_name` AS `collector_abbreviated_middle_name` from (`samples_collection` `coll` left join `view_authors` `authors` on((`coll`.`collector_id` = `authors`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_collection`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_collection`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_collection` AS select `coll`.`sample_id` AS `sample_id`,`coll`.`year` AS `collection_year`,`coll`.`month` AS `collection_month`,`coll`.`day` AS `collection_day`,concat(`coll`.`year`,if(((`coll`.`month` > 0) and (`coll`.`month` is not null)),concat('-',lpad(`coll`.`month`,2,0),if(((`coll`.`day` > 0) and (`coll`.`day` is not null)),concat('-',lpad(`coll`.`day`,2,0)),'')),'')) AS `collection_date`,`authors`.`abbreviated_middle_name` AS `collector_abbreviated_middle_name` from (`samples_collection` `coll` left join `view_authors` `authors` on((`coll`.`collector_id` = `authors`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_details`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_details` AS select `samples`.`sample_id` AS `sample_id`,`samples`.`sample_name` AS `sample_name`,`location`.`location` AS `location`,`location`.`additional_location_info` AS `additional_location_info`,if((`location`.`geo_loc_latitude` is null),'',concat(`location`.`geo_loc_latitude`,' DD')) AS `geo_loc_latitude`,if((`location`.`geo_loc_longitude` is null),'',concat(`location`.`geo_loc_longitude`,' DD')) AS `geo_loc_longitude`,`coll`.`collection_date` AS `collection_date`,`coll`.`collector_abbreviated_middle_name` AS `collector_name`,`library`.`library_id` AS `library_id`,`library`.`library_layout` AS `library_layout`,`library`.`library_strategy` AS `library_strategy`,`library`.`library_source` AS `library_source`,`library`.`library_selection` AS `library_selection`,`library`.`library_design_description` AS `library_design_description`,`host`.`host_name` AS `host_name`,`host`.`host_subject_id` AS `host_subject_id`,`host`.`additional_host_info` AS `additional_host_info`,if((`host`.`patient_age` is null),'',concat(`host`.`patient_age`,' years')) AS `patient_age`,`host`.`patient_gender` AS `patient_gender`,`host`.`patient_status` AS `patient_status`,`host`.`last_vaccinated` AS `last_vaccinated`,`host`.`host_habitat` AS `host_habitat`,`host`.`host_behaviour` AS `host_behaviour`,`host`.`host_description` AS `host_decription`,`host`.`host_gravidity` AS `host_gravidity`,`sampling`.`originating_lab_name` AS `originating_lab_name`,`sampling`.`submitting_lab_name` AS `submitting_lab_name`,`sampling`.`passage_details` AS `passage_details`,`sampling`.`sampling_strategy` AS `sampling_strategy`,`sampling`.`author_group_name` AS `author_group_name`,`sampling`.`authors_list` AS `authors_list`,`sampling`.`isolate` AS `isolate`,`sampling`.`strain` AS `strain`,`sampling`.`sample_capture_status` AS `sample_capture_status`,`sampling`.`specimen_source` AS `specimen_source`,`health`.`subject_exposure` AS `subject_exposure`,`health`.`subject_exposure_duration` AS `subject_exposure_duration`,`health`.`type_exposure` AS `type_exposure`,`health`.`hospitalization` AS `hospitalization`,`health`.`ilness_duration_days` AS `ilness_duration`,`health`.`ilness_symptoms` AS `ilness_symptoms`,`health`.`host_disease_outcome` AS `host_disease_outcome`,`health`.`treatment` AS `treatment`,`health`.`outbreak` AS `outbreak`,`sequencing`.`sequencing_instrument` AS `sequencing_instrument`,`sequencing`.`sequencing_platform` AS `sequencing_platform`,`sequencing`.`assembly_method` AS `assembly_method`,`sequencing`.`coverage` AS `coverage` from (((((((`view_samples_base` `samples` left join `view_samples_location` `location` on((`samples`.`sample_id` = `location`.`sample_id`))) left join `view_samples_collection` `coll` on((`samples`.`sample_id` = `coll`.`sample_id`))) left join `view_samples_library` `library` on((`samples`.`sample_id` = `library`.`sample_id`))) left join `view_samples_host` `host` on((`samples`.`sample_id` = `host`.`sample_id`))) left join `view_samples_sampling` `sampling` on((`samples`.`sample_id` = `sampling`.`sample_id`))) left join `view_samples_health_status` `health` on((`samples`.`sample_id` = `health`.`sample_id`))) left join `view_samples_sequencing` `sequencing` on((`samples`.`sample_id` = `sequencing`.`sample_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_display`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_display`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_display` AS select `samples`.`sample_id` AS `sample_id`,`samples`.`sample_name` AS `sample_name`,`collection`.`collection_date` AS `collection_date`,`sampling`.`author_group_name` AS `group_name` from ((`view_samples_base` `samples` left join `view_samples_collection` `collection` on((`samples`.`sample_id` = `collection`.`sample_id`))) left join `view_samples_sampling` `sampling` on((`samples`.`sample_id` = `sampling`.`sample_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_ena`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_ena`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_ena` AS select `samples`.`sample_id` AS `sample_id`,`samples`.`sample_name` AS `sample_name`,`samples`.`sample_name` AS `virus identifier`,`health`.`subject_exposure` AS `subject exposure`,`health`.`subject_exposure_duration` AS `subject exposure duration`,`health`.`type_exposure` AS `type exposure`,`hosts`.`ppe` AS `personal protective equipment`,`health`.`hospitalization` AS `hospitalisation`,`health`.`ilness_duration_days` AS `ilness duration`,`health`.`ilness_symptoms` AS `ilness symptoms`,`collection`.`collection_date` AS `collection date`,`location`.`country` AS `geographic location (country and/or sea)`,`location`.`geo_loc_latitude` AS `geographic location (latitude)`,`location`.`geo_loc_longitude` AS `geographic location (longitude)`,concat(if((`location`.`region` is null),'',concat(`location`.`region`,', ')),`location`.`locality`) AS `geographic location (region and locality)`,`sampling`.`sample_capture_status` AS `sample capture status`,`health`.`host_disease_outcome` AS `host disease outcome`,`hosts`.`host_common_name` AS `host common name`,`hosts`.`host_subject_id` AS `host subject id`,`hosts`.`patient_age` AS `host age`,`hosts`.`patient_gender_ena` AS `host sex`,`health`.`host_health_state` AS `host health state`,`hosts`.`host_scientific_name` AS `host scientific name`,`collection`.`collector_abbreviated_middle_name` AS `collector name`,concat(`sampling`.`originating_lab_name`,', ',`sampling`.`originating_lab_address`) AS `collecting institution`,`sampling`.`sample_storage_conditions` AS `sample storage conditions`,`sampling`.`definition_for_seropositive_sample` AS `definition for seropositive sample`,`sampling`.`serotype` AS `serotype (required for a seropositive sample)`,`sampling`.`isolate` AS `isolate`,`sampling`.`strain` AS `strain`,`hosts`.`host_habitat` AS `host habitat`,`sampling`.`isolation_source_host_associated` AS `isolation source host associated`,`hosts`.`host_description` AS `host description`,`hosts`.`host_gravidity` AS `gravidity`,`hosts`.`host_behaviour` AS `host behaviour`,`sampling`.`isolation_source_non_host_associated` AS `isolation source non-host-associated` from (((((`view_samples_base` `samples` left join `view_samples_health_status` `health` on((`samples`.`sample_id` = `health`.`sample_id`))) left join `view_samples_host` `hosts` on((`samples`.`sample_id` = `hosts`.`sample_id`))) left join `view_samples_collection` `collection` on((`samples`.`sample_id` = `collection`.`sample_id`))) left join `view_samples_location` `location` on((`samples`.`sample_id` = `location`.`sample_id`))) left join `view_samples_sampling` `sampling` on((`samples`.`sample_id` = `sampling`.`sample_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_ena_experiment`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_ena_experiment`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_ena_experiment` AS select `samples`.`sample_id` AS `sample_id`,`samples`.`sample_name` AS `sample_name`,`library`.`library_id` AS `library_name`,`library`.`library_strategy` AS `library_strategy`,`library`.`library_source` AS `library_source`,`library`.`library_selection` AS `library_selection`,`library`.`library_design_description` AS `library_design_description`,`library`.`layout_paired` AS `is_paired`,`library`.`library_preparation_date` AS `library_preparation_date`,`sequencing`.`sequencing_platform` AS `sequencing_platform`,`sequencing`.`sequencing_instrument` AS `sequencing_instrument` from ((`view_samples_base` `samples` left join `view_samples_library` `library` on((`samples`.`sample_id` = `library`.`sample_id`))) left join `view_samples_sequencing` `sequencing` on((`samples`.`sample_id` = `sequencing`.`sample_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_gisaid`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_gisaid`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_gisaid` AS select `samples`.`sample_id` AS `sample_id`,`samples`.`sample_name` AS `sample_name`,`sampling`.`passage_details` AS `passage_details`,`collection`.`collection_date` AS `collection_date`,`location`.`location` AS `location`,`location`.`continent` AS `continent`,`location`.`country` AS `country`,`location`.`region` AS `region`,`location`.`locality` AS `locality`,`location`.`additional_location_info` AS `additional_location_info`,`hosts`.`host_common_name` AS `host`,`hosts`.`additional_host_info` AS `additional_host_info`,`sampling`.`sampling_strategy` AS `sampling_strategy`,`hosts`.`patient_gender` AS `patient_gender`,`hosts`.`patient_age` AS `patient_age`,`hosts`.`patient_status` AS `patient_status`,`sampling`.`specimen_source` AS `specimen_source`,`health`.`outbreak` AS `outbreak`,`hosts`.`last_vaccinated` AS `last_vaccinated`,`health`.`treatment` AS `treatment`,`sequencing`.`sequencing_instrument` AS `sequencing_technology`,`sequencing`.`assembly_method` AS `assembly_method`,`sequencing`.`coverage_x` AS `coverage`,`sampling`.`originating_lab_name` AS `originating_lab_name`,`sampling`.`originating_lab_address` AS `originating_lab_address`,`sampling`.`originating_lab_sample_name` AS `originating_lab_sample_name`,`sampling`.`submitting_lab_name` AS `submitting_lab_name`,`sampling`.`submitting_lab_address` AS `submitting_lab_address`,`sampling`.`submitting_lab_sample_name` AS `submitting_lab_sample_name`,`sampling`.`authors_list` AS `authors_list`,`seqfiles`.`filename` AS `seqfilename` from (((((((`view_samples_base` `samples` left join `view_samples_sampling` `sampling` on((`samples`.`sample_id` = `sampling`.`sample_id`))) left join `view_samples_collection` `collection` on((`samples`.`sample_id` = `collection`.`sample_id`))) left join `view_samples_location` `location` on((`samples`.`sample_id` = `location`.`sample_id`))) left join `view_samples_host` `hosts` on((`samples`.`sample_id` = `hosts`.`sample_id`))) left join `view_samples_health_status` `health` on((`samples`.`sample_id` = `health`.`sample_id`))) left join `view_samples_sequencing` `sequencing` on((`samples`.`sample_id` = `sequencing`.`sample_id`))) left join `view_seqfiles` `seqfiles` on((`samples`.`sample_id` = `seqfiles`.`sample_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_health_status`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_health_status`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_health_status` AS select `health`.`sample_id` AS `sample_id`,`health`.`subject_exposure` AS `subject_exposure`,`health`.`subject_exposure_duration` AS `subject_exposure_duration`,`health`.`type_exposure` AS `type_exposure`,if((`health`.`hospitalization` is null),'',if(((0 <> `health`.`hospitalization`) is true),'yes','no')) AS `hospitalization`,`health`.`ilness_duration` AS `ilness_duration`,if((`health`.`ilness_duration` is null),'',concat(`health`.`ilness_duration`,' days')) AS `ilness_duration_days`,`health`.`ilness_symptoms` AS `ilness_symptoms`,`outcome`.`label` AS `host_disease_outcome`,`health_states`.`label` AS `host_health_state`,`health`.`treatment` AS `treatment`,`health`.`outbreak` AS `outbreak` from ((`samples_health_status` `health` left join `host_health_states` `health_states` on((`health`.`host_health_state_id` = `health_states`.`id`))) left join `host_disease_outcome` `outcome` on((`health`.`host_disease_outcome_id` = `outcome`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_host`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_host`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_host` AS select `host`.`sample_id` AS `sample_id`,`hosts`.`label` AS `host_common_name`,`hosts`.`latin` AS `host_scientific_name`,concat(`hosts`.`label`,' (',`hosts`.`latin`,')') AS `host_name`,`host`.`host_subject_id` AS `host_subject_id`,`host`.`additional_host_info` AS `additional_host_info`,`host`.`patient_age` AS `patient_age`,if((`host`.`patient_gender` is null),'unknown',if(((0 <> `host`.`patient_gender`) is true),'Male','Female')) AS `patient_gender`,if((`host`.`patient_gender` is null),'not provided',if(((0 <> `host`.`patient_gender`) is true),'male','female')) AS `patient_gender_ena`,`patient_statuses`.`label` AS `patient_status`,`host`.`ppe` AS `ppe`,`host`.`last_vaccinated` AS `last_vaccinated`,`habitats`.`label` AS `host_habitat`,`behaviours`.`label` AS `host_behaviour`,`host`.`host_description` AS `host_description`,`host`.`gravidity` AS `host_gravidity` from ((((`samples_host` `host` left join `hosts` on((`host`.`host_id` = `hosts`.`id`))) left join `patient_statuses` on((`host`.`patient_status_id` = `patient_statuses`.`id`))) left join `host_habitats` `habitats` on((`host`.`host_habitat_id` = `habitats`.`id`))) left join `host_behaviours` `behaviours` on((`host`.`host_behaviour_id` = `behaviours`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_library`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_library`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_library` AS select `library`.`sample_id` AS `sample_id`,`library`.`lib_id` AS `library_id`,`library`.`layout_paired` AS `layout_paired`,if((`library`.`layout_paired` is null),'',if(((0 <> `library`.`layout_paired`) is true),'Paired-End','Single')) AS `library_layout`,`strategies`.`item_key` AS `library_strategy`,`sources`.`item_key` AS `library_source`,`selections`.`item_key` AS `library_selection`,`library`.`design_description` AS `library_design_description`,if((`library`.`preparation_date` is null),'',date_format(`library`.`preparation_date`,'%Y-%m-%d')) AS `library_preparation_date` from (((`samples_library` `library` left join `library_strategies` `strategies` on((`library`.`strategy_id` = `strategies`.`id`))) left join `library_sources` `sources` on((`library`.`source_id` = `sources`.`id`))) left join `library_selections` `selections` on((`library`.`selection_id` = `selections`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_location`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_location`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_location` AS select `location`.`sample_id` AS `sample_id`,concat(`continents`.`label`,' / ',`countries`.`label`,if((`location`.`region` is not null),concat(' / ',`location`.`region`),''),if((`location`.`locality` is not null),concat(' / ',`location`.`locality`),'')) AS `location`,`continents`.`label` AS `continent`,`countries`.`label` AS `country`,`location`.`region` AS `region`,`location`.`locality` AS `locality`,`location`.`additional_info` AS `additional_location_info`,`location`.`geo_loc_latitude` AS `geo_loc_latitude`,`location`.`geo_loc_longitude` AS `geo_loc_longitude` from ((`samples_location` `location` left join `continents` on((`location`.`continent_id` = `continents`.`id`))) left join `countries` on((`location`.`country_id` = `countries`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_ncbi_sra`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_ncbi_sra`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_ncbi_sra` AS select `samples`.`sample_id` AS `sample_id`,`library`.`library_id` AS `library_name`,`library`.`library_strategy` AS `library_strategy`,`library`.`library_source` AS `library_source`,`library`.`library_selection` AS `library_selection`,if((`library`.`layout_paired` is null),'',if(((0 <> `library`.`layout_paired`) is true),'Paired-End','Single')) AS `library_layout`,`library`.`library_design_description` AS `library_design_description`,concat(`library`.`library_strategy`,' of SARS-CoV-2: ',convert(if((`host`.`patient_age` is null),'',if((`host`.`patient_age` >= 18),'adult ','child ')) using utf8mb4),convert(`host`.`patient_gender_ena` using utf8mb4)) AS `title`,`sequencing`.`sequencing_platform` AS `sequencing_platform`,`sequencing`.`sequencing_instrument` AS `sequencing_instrument` from (((`view_samples_base` `samples` left join `view_samples_library` `library` on((`samples`.`sample_id` = `library`.`sample_id`))) left join `view_samples_sequencing` `sequencing` on((`samples`.`sample_id` = `sequencing`.`sample_id`))) left join `view_samples_host` `host` on((`samples`.`sample_id` = `host`.`sample_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_sampling`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_sampling`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_sampling` AS select `sampling`.`sample_id` AS `sample_id`,`originating_lab`.`name` AS `originating_lab_name`,`originating_lab`.`address` AS `originating_lab_address`,`sampling`.`originating_lab_sample_name` AS `originating_lab_sample_name`,`submitting_lab`.`name` AS `submitting_lab_name`,`submitting_lab`.`address` AS `submitting_lab_address`,`sampling`.`submitting_lab_sample_name` AS `submitting_lab_sample_name`,`passage_details`.`label` AS `passage_details`,`sampling_strategies`.`label` AS `sampling_strategy`,`author_groups`.`group_name` AS `author_group_name`,`author_groups`.`abbreviated_middle_names` AS `authors_list`,`sampling`.`isolate` AS `isolate`,`sampling`.`strain` AS `strain`,`sampling`.`isolation_source_host_associated` AS `isolation_source_host_associated`,`sampling`.`isolation_source_non_host_associated` AS `isolation_source_non_host_associated`,`capture_statuses`.`label` AS `sample_capture_status`,`specimen_sources`.`label` AS `specimen_source`,`sampling`.`sample_storage_conditions` AS `sample_storage_conditions`,`sampling`.`definition_for_seropositive_sample` AS `definition_for_seropositive_sample`,`sampling`.`serotype` AS `serotype` from (((((((`samples_sampling` `sampling` left join `view_institutions` `originating_lab` on((`sampling`.`originating_lab_id` = `originating_lab`.`id`))) left join `view_institutions` `submitting_lab` on((`sampling`.`submitting_lab_id` = `submitting_lab`.`id`))) left join `view_passage_details` `passage_details` on((`sampling`.`passage_details_id` = `passage_details`.`id`))) left join `view_sampling_strategies` `sampling_strategies` on((`sampling`.`sampling_strategy_id` = `sampling_strategies`.`id`))) left join `view_authors_in_groups_condensed` `author_groups` on((`sampling`.`author_group_id` = `author_groups`.`group_id`))) left join `sample_capture_status` `capture_statuses` on((`sampling`.`sample_capture_status_id` = `capture_statuses`.`id`))) left join `view_specimen_sources` `specimen_sources` on((`sampling`.`specimen_source_id` = `specimen_sources`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_samples_sequencing`
--

/*!50001 DROP VIEW IF EXISTS `view_samples_sequencing`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_samples_sequencing` AS select `sequencing`.`sample_id` AS `sample_id`,`instruments`.`label` AS `sequencing_instrument`,`platforms`.`label` AS `sequencing_platform`,`assembly`.`label` AS `assembly_method`,`sequencing`.`coverage` AS `coverage`,if((`sequencing`.`coverage` is null),'',concat(`sequencing`.`coverage`,'x')) AS `coverage_x` from (((`samples_sequencing` `sequencing` left join `assembly_methods` `assembly` on((`sequencing`.`assembly_method_id` = `assembly`.`id`))) left join `sequencing_instruments` `instruments` on((`sequencing`.`sequencing_instrument_id` = `instruments`.`id`))) left join `sequencing_platforms` `platforms` on((`instruments`.`platform_id` = `platforms`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_sampling_strategies`
--

/*!50001 DROP VIEW IF EXISTS `view_sampling_strategies`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_sampling_strategies` AS select `sampling_strategies`.`id` AS `id`,`sampling_strategies`.`label` AS `label`,`sampling_strategies`.`indx` AS `indx` from `sampling_strategies` where (`sampling_strategies`.`indx` <> 0) order by `sampling_strategies`.`indx`,`sampling_strategies`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_seqfiles`
--

/*!50001 DROP VIEW IF EXISTS `view_seqfiles`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_seqfiles` AS select `samples`.`sample_id` AS `sample_id`,`exts`.`item_key` AS `file_type`,`exts`.`item_value` AS `file_extension`,`seqfiles`.`is_assembly` AS `is_assembly`,`seqfiles`.`is_forward_read` AS `is_forward_read`,if(((0 <> `seqfiles`.`is_assembly`) is true),concat(`samples`.`sample_name`,'.',`exts`.`item_value`),'') AS `filename` from ((`seqfiles` left join `view_samples_base` `samples` on((`seqfiles`.`sample_id` = `samples`.`sample_id`))) left join `seqfile_extensions` `exts` on((`seqfiles`.`file_type_id` = `exts`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_sequencing_technologies`
--

/*!50001 DROP VIEW IF EXISTS `view_sequencing_technologies`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_sequencing_technologies` AS select `sequencing_technologies`.`id` AS `id`,`sequencing_technologies`.`label` AS `label`,`sequencing_technologies`.`indx` AS `indx` from `sequencing_technologies` where (`sequencing_technologies`.`indx` <> 0) order by `sequencing_technologies`.`indx`,`sequencing_technologies`.`label` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_specimen_sources`
--

/*!50001 DROP VIEW IF EXISTS `view_specimen_sources`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_specimen_sources` AS select `specimen_sources`.`id` AS `id`,`specimen_sources`.`label` AS `label`,`specimen_sources`.`indx` AS `indx` from `specimen_sources` where (`specimen_sources`.`indx` <> 0) order by `specimen_sources`.`indx`,`specimen_sources`.`label` */;
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

-- Dump completed on 2021-06-10  7:05:56
