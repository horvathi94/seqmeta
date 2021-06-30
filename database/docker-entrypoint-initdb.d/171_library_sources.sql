SET @table_name := "library_sources";
CALL create_dict_table(@table_name);


CALL upsert_dict_table(@table_name, 1, "GENOMIC", "Genomic DNA (includes PCR products from genomic DNA)");
CALL upsert_dict_table(@table_name, 2, "TRANSCRIPTOMIC", "Transcription products or non genomic DNA (EST, cDNA, RT-PCR, screened libraries)");
CALL upsert_dict_table(@table_name, 3, "METAGENOMIC", "Mixed material from metagenome");
CALL upsert_dict_table(@table_name, 4, "METATRANSCRIPTOMIC", "Transcription products from community targets");
CALL upsert_dict_table(@table_name, 5, "SYNTHETIC", "Synthetic DNA");
CALL upsert_dict_table(@table_name, 6, "VIRAL RNA", "Viral RNA");
CALL upsert_dict_table(@table_name, 7, "GENOMIC SINGLE CELL", "");
CALL upsert_dict_table(@table_name, 8, "TRANSCRIPTOMIC SINGLE CELL", "");
CALL upsert_dict_table(@table_name, 9, "OTHER", "Other, unspecified, or unknown library source material (please include additional info in the `design description`)");
