SAMPLE_TITLE = {
    "general_name": "ena_sample_title",
    "label": "ENA sample title",
    "description": "A short title for the sample.",
    "_ena_requirement": "mandatory"}

ENA_STUDY = {
    "general_name": "ena_study",
    "label": "ENA study accession",
    "description": "Accession number of study where sample will be uploaded.",
    "_ena_requirement": "mandatory"}

EXPERIMENT_TITLE = {
    "general_name": "ena_experiment_title",
    "label": "ENA experiment title",
    "description": "Title of ENA experiment",
    "_ena_requirement": "mandatory"}

EXPERIMENT_ALIAS = {
    "general_name": "ena_experiment_alias",
    "label": "ENA experiment alias",
    "description": "Alias of ENA experiment.",
    "_ena_requirement": "mandatory",
    "_is_unique": True}

RUN_ALIAS = {
    "general_name": "ena_run_alias",
    "label": "ENA run alias",
    "description": "Alias of ENA run.",
    "_ena_requirement": "mandatory",
    "_is_unique": True}


PLATFORM = {
    "general_name": "platform",
    "label": "Platform",
    "type_": "select",
    "description": "See <a href='https://ena-docs.readthedocs.io/en/"\
        "latest/submit/reads/webin-cli.html#platform'>link</a>"\
        "for more details.",
    "_ena_requirement": "mandatory",
    "_options": ["LS454", "ILLUMINA", "PACBIO_SMRT", "ION_TORRENT",
                "CAPILLARY", "OXFORD_NANOPORE", "BGISEQ", "DNBSEQ"]}


INSTRUMENT = {
    "general_name": "instrument",
    "label": "Instrument",
    "type_": "select",
    "description": "See <a href='https://ena-docs.readthedocs.io/en/"\
        "latest/submit/reads/webin-cli.html#instrument'>link</a>"\
        "for more details.",
    "_ena_requirement": "mandatory",
    "_options": ["454 GS", "454 GS 20", "454 GS FLX", "454 GS FLX+",
    "454 GS FLX Titanium", "454 GS Junior", "HiSeq X Five", "HiSeq X Ten",
    "Illumina Genome Analyzer", "Illumina Genome Analyzer II",
    "Illumina Genome Analyzer IIx", "Illumina HiScanSQ", "Illumina HiSeq 1000",
    "Illumina HiSeq 1500", "Illumina HiSeq 2000", "Illumina HiSeq 2500",
    "Illumina HiSeq 3000", "Illumina HiSeq 4000", "Illumina iSeq 100",
    "Illumina MiSeq", "Illumina MiniSeq", "Illumina NovaSeq 6000",
    "NextSeq 500", "NextSeq 550", "PacBio RS", "PacBio RS II", "Sequel",
    "Ion Torrent PGM", "Ion Torrent Proton", "Ion Torrent S5",
    "Ion Torrent S5 XL", "AB 3730xL Genetic Analyzer",
    "AB 3730 Genetic Analyzer", "AB 3500xL Genetic Analyzer",
    "AB 3500 Genetic Analyzer", "AB 3130xL Genetic Analyzer",
    "AB 3130 Genetic Analyzer", "AB 310 Genetic Analyzer", "MinION", "GridION",
    "PromethION", "BGISEQ-500", "DNBSEQ-T7", "DNBSEQ-G400", "DNBSEQ-G50",
    "DNBSEQ-G400 FAST", "unspecified"]}

INSERT_SIZE = {
    "general_name": "insert_size",
    "label": "Insert size (bp)",
    "description": "Insert size of paired reads.",
    "_ena_requirement": "optional",
    "_pattern": "^[1-9][0-9]*$"}


LIBRARY_SOURCE = {
    "general_name": "library_source",
    "label": "Library source",
    "type_": "select",
    "description": "See <a href='https://ena-docs.readthedocs.io/en/"\
        "latest/submit/reads/webin-cli.html#source'>link</a>"\
        "for more details.",
    "_ena_requirement":  "mandatory",
    "_options": ["GENOMIC", "GENOMIC SINGLE CELL", "TRANSCRIPTOMIC",
    "TRANSCRIPTOMIC SINGLE CELL", "METAGENOMIC", "METATRANSCRIPTOMIC",
    "SYNTHETIC", "VIRAL RNA", "OTHER"]}

LIBRARY_SELECTION = {
    "general_name": "library_selection",
    "label": "Library selection",
    "type_": "select",
    "description": "See <a href='"\
        "https://ena-docs.readthedocs.io/en/latest/submit/reads/"\
        "webin-cli.html#selection'>link</a> for more details.",
    "_ena_requirement": "mandatory",
    "_options": ["RANDOM", "PCR", "RANDOM PCR", "RT-PCR", "HMPR", "MF",
    "repeat fractionation", "size fractionation", "MSLL", "cDNA",
    "cDNA_randomPriming", "cDNA_oligo_dT", "PolyA", "Oligo-dT", "Inverse rRNA",
    "Inverse rRNA selection", "ChIP", "ChIP-Seq", "MNase", "DNase",
    "Hybrid Selection", "Reduced Representation", "Restriction Digest",
    "5-methylcytidine antibody", "MBD2 protein methyl-CpG binding domain",
    "CAGE", "RACE", "MDA", "padlock probes capture method", "other",
    "unspecified"]}

LIBRARY_STRATEGY = {
    "general_name": "library_strategy",
    "label": "Library strategy",
    "type_": "select",
    "description": "See <a href='"\
        "https://ena-docs.readthedocs.io/en/latest/submit/reads/"\
        "webin-cli.html#strategy'>link</a> for more details.",
    "_ena_requirement": "mandatory",
    "_options": ["WGS","WGA","WXS","RNA-Seq","ssRNA-seq","miRNA-Seq",
    "ncRNA-Seq","FL-cDNA","EST","Hi-C","ATAC-seq","WCS","RAD-Seq","CLONE",
    "POOLCLONE","AMPLICON","CLONEEND","FINISHING","ChIP-Seq","MNase-Seq",
    "DNase-Hypersensitivity","Bisulfite-Seq","CTS","MRE-Seq","MeDIP-Seq",
    "MBD-Seq","Tn-Seq","VALIDATION","FAIRE-seq","SELEX","RIP-Seq","ChIA-PET",
    "Synthetic-Long-Read","Targeted-Capture",
    "Tethered Chromatin Conformation Capture","OTHER"]}

LIBRARY_LAYOUT = {
    "general_name": "library_layout",
    "label": "Library layout",
    "type_": "select",
    "description": "Library layout single or paired end reads.",
    "_ena_requirement": "mandatory",
    "_options": ["single", "paired"]}


LIBRARY_CONSTRUCTION_PROTOCOL = {
    "general_name": "library_construction_protocol",
    "label": "Library construction protocol",
    "description": "Free text library description",
    "_ena_requirement": "mandatory"}

LIBRARY_PREPARATION_DATE = {
    "general_name": "library_preparation_date",
    "label": "Library preparation date",
    "type_": "date",
    "description": "Date when the sequencing library was prepared.",
    "_ena_requirement": "recommended"}


SAMPLE_ACCESSION = {
    "general_name": "ena_sample_accession",
    "label": "ENA sample accession",
    "description": "Accession number given to the sample by ENA. "\
        "Fills out automatically at sucessful submission.",}


EXPERIMENT_ACCESSION = {
    "general_name": "ena_experiment_accession",
    "label": "ENA experiment accession",
    "description": "Accession number given to the experiment by ENA. "\
        "Fills out automatically at sucessful submission.",}


RUN_ACCESSION = {
    "general_name": "ena_run_accession",
    "label": "ENA run accession",
    "description": "Accession number given to the run by ENA. "\
        "Fills out automatically at sucessful submission.",}


ALL_FIELDS = [SAMPLE_TITLE, ENA_STUDY, EXPERIMENT_TITLE, EXPERIMENT_ALIAS,
              RUN_ALIAS, PLATFORM, INSTRUMENT, INSERT_SIZE,
              LIBRARY_SOURCE, LIBRARY_SELECTION, LIBRARY_STRATEGY,
              LIBRARY_LAYOUT,
              LIBRARY_CONSTRUCTION_PROTOCOL, LIBRARY_PREPARATION_DATE,
              SAMPLE_ACCESSION, EXPERIMENT_ACCESSION, RUN_ACCESSION]
