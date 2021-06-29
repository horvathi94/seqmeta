SET @table_name := "sequencing_platforms";
CALL create_basic_table(@table_name);


CALL upsert_basic_table(@table_name, "LS454", 1);
CALL upsert_basic_table(@table_name, "ABI_SOLID", 2);
CALL upsert_basic_table(@table_name, "BGISEQ", 3);
CALL upsert_basic_table(@table_name, "CAPILLARY", 4);
CALL upsert_basic_table(@table_name, "COMPLETE_GENOMICS", 5);
CALL upsert_basic_table(@table_name, "HELICOS", 6);
CALL upsert_basic_table(@table_name, "ILLUMINA", 7);
CALL upsert_basic_table(@table_name, "ION_TORRENT", 8);
CALL upsert_basic_table(@table_name, "OXFORD_NANOPORE", 9);
CALL upsert_basic_table(@table_name, "PACBIO_SMRT", 10);




CREATE TABLE IF NOT EXISTS `sequencing_instruments` (
	id						INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	platform_id		INT UNSIGNED,
	label					CHAR(200) UNIQUE
);


INSERT INTO `sequencing_instruments` (label, platform_id) VALUES
	("454 GS", 1),
	("454 GS 20", 1),
	("454 GS FLX", 1),
	("454 GS FLX+", 1),
	("454 GS FLX Titanium", 1),
	("454 GS Junior", 1),
	("AB 5500 Genetic Analyzer", 2),
	("AB 5500xl Genetic Analyzer", 2),
	("AB 5500x-Wl Genetic Analyzer", 2),
	("AB SOLiD 3 Plus System", 2),
	("AB SOLiD 4 System", 2),
	("AB SOLiD 4hq System", 2),
	("AB SOLiD PI System", 2),
	("AB SOLiD System", 2),
	("AB SOLiD System 2.0", 2),
	("AB SOLiD System 3.0", 2),
	("BGISEQ-500", 3),
	("AB 310 Genetic A:nalyzer", 4),
	("AB 3130 Genetic Analyzer", 4),
	("AB 3130xL Genetic Analyzer", 4),
	("AB 3500 Genetic Analyzer", 4),
	("AB 3500xL Genetic Analyzer", 4),
	("AB 3730 Genetic Analyzer", 4),
	("AB 3730xL Genetic Analyzer", 4),
	("Complete Genomics", 5),
	("Helicos HeliScope", 6),
	("HiSeq X Five", 7),
	("HiSeq X Ten", 7),
	("Illumina Genome Analyzer", 7),
	("Illumina Genome Analyzer II", 7),
	("Illumina Genome Analyzer IIx", 7),
	("Illumina HiScanSQ", 7),
	("Illumina HiSeq 1000", 7),
	("Illumina HiSeq 1500", 7),
	("Illumina HiSeq 2000", 7),
	("Illumina HiSeq 2500", 7),
	("Illumina HiSeq 3000", 7),
	("Illumina HiSeq 4000", 7),
	("Illumina iSeq 100", 7),
	("Illumina NovaSeq 6000", 7),
	("Illumina MiniSeq", 7),
	("Illumina MiSeq", 7),
	("NextSeq 500", 7),
	("NextSeq 550", 7),
	("Ion Torrent Proton", 8),
	("Ion Torrent S5 XL", 8),
	("Ion Torrent S5", 8),
	("GridION", 9),
	("MinION", 9),
	("PromethION", 9),
	("PacBio RS II", 10),
	("PacBio Sequel", 10),
	("PacBio Sequel II", 10);
