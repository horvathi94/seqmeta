from typing import List
from .attr_field import AttributeField


# Basic fields
sample_name = AttributeField("sample_name", "Sample name",
    description="Unique name of sample", is_unique=True, is_fixed=True)
sample_name.set_mandatory()
sample_description = AttributeField("short_description", "Short description",
    description="A short description of the sample for easier " \
        "identification (this will not be part of any submission).",
        is_fixed=True)


# GISAID fields
virus_name = AttributeField("virus_name", "GISAID virus name",
    description="Visrus name of the sample.",
    gisaid_name="Virus name", gisaid_requirement="mandatory",
    gisaid_header="covv_virus_name")
gisaid_submitter = AttributeField("gisaid_submitter", "GISAID submitter",
    description="Username of person submitting to GISAID.",
    gisaid_name="Submitter", gisaid_requirement="mandatory",
    gisaid_header="submitter")
gisaid_filename = AttributeField("gisaid_filename", "GISAID filename",
    description="Name of file to be uploaded to GISAID.",
    gisaid_name="FASTA filename", gisaid_requirement="mandatory",
    gisaid_header="fn", default="sequences")


# ENA fields
ena_sample_title = AttributeField("ena_sample_title", "ENA sample title",
    description="A short title for the sample.", ena_requirement="mandatory")
ena_study = AttributeField("ena_study", "ENA study accession",
    description="Accession number of study where sample will be uploaded.",
    ena_requirement="mandatory")
ena_exp_title = AttributeField("ena_experiment_title", "ENA experiment title",
    description="Title of ENA experiment", ena_requirement="mandatory")
ena_exp_alias = AttributeField("ena_experiment_alias", "ENA experiment alias",
    description="Alias of ENA experiment.", ena_requirement="mandatory",
    is_unique=True)
ena_run_alias = AttributeField("ena_run_alias", "ENA run alias",
    description="Alias of ENA run.", ena_requirement="mandatory",
    is_unique=True)
platform = AttributeField("platform", "Platform", type_="select",
    description="See <a href='https://ena-docs.readthedocs.io/en/"\
        "latest/submit/reads/webin-cli.html#platform'>link</a>"\
        "for more details.", ena_requirement="mandatory")
platform.options = ["LS454", "ILLUMINA", "PACBIO_SMRT", "ION_TORRENT",
                  "CAPILLARY", "OXFORD_NANOPORE", "BGISEQ", "DNBSEQ"]
instrument = AttributeField("instrument", "Instrument", type_="select",
    description="See <a href='https://ena-docs.readthedocs.io/en/"\
        "latest/submit/reads/webin-cli.html#instrument'>link</a>"\
        "for more details.", ena_requirement="mandatory")
instrument.options = ["454 GS", "454 GS 20", "454 GS FLX", "454 GS FLX+",
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
    "DNBSEQ-G400 FAST", "unspecified"]
insert_size = AttributeField("insert_size", "Insert size (bp)",
    description="Insert size of paired reads.", ena_requirement="optional")
insert_size.pattern="^[1-9][0-9]*$"

lib_source = AttributeField("library_source", "Library source", type_="select",
    description="See <a href='https://ena-docs.readthedocs.io/en/"\
        "latest/submit/reads/webin-cli.html#source'>link</a>"\
        "for more details.", ena_requirement = "mandatory")
lib_source.options = ["GENOMIC", "GENOMIC SINGLE CELL", "TRANSCRIPTOMIC",
    "TRANSCRIPTOMIC SINGLE CELL", "METAGENOMIC", "METATRANSCRIPTOMIC",
    "SYNTHETIC", "VIRAL RNA", "OTHER"]
lib_selection = AttributeField("library_selection", "Library selection",
    type_="select", description="See <a href='"\
        "https://ena-docs.readthedocs.io/en/latest/submit/reads/"\
        "webin-cli.html#selection'>link</a> for more details.",
    ena_requirement = "mandatory")
lib_selection.options = ["RANDOM", "PCR", "RANDOM PCR", "RT-PCR", "HMPR", "MF",
    "repeat fractionation", "size fractionation", "MSLL", "cDNA",
    "cDNA_randomPriming", "cDNA_oligo_dT", "PolyA", "Oligo-dT", "Inverse rRNA",
    "Inverse rRNA selection", "ChIP", "ChIP-Seq", "MNase", "DNase",
    "Hybrid Selection", "Reduced Representation", "Restriction Digest",
    "5-methylcytidine antibody", "MBD2 protein methyl-CpG binding domain",
    "CAGE", "RACE", "MDA", "padlock probes capture method", "other",
    "unspecified"]
lib_strategy = AttributeField("library_strategy", "Library strategy",
    type_ = "select", description = "See <a href='"\
    "https://ena-docs.readthedocs.io/en/latest/submit/reads/"\
    "webin-cli.html#strategy'>link</a> for more details.",
    ena_requirement = "mandatory")
lib_strategy.options = ["WGS","WGA","WXS","RNA-Seq","ssRNA-seq","miRNA-Seq",
    "ncRNA-Seq","FL-cDNA","EST","Hi-C","ATAC-seq","WCS","RAD-Seq","CLONE",
    "POOLCLONE","AMPLICON","CLONEEND","FINISHING","ChIP-Seq","MNase-Seq",
    "DNase-Hypersensitivity","Bisulfite-Seq","CTS","MRE-Seq","MeDIP-Seq",
    "MBD-Seq","Tn-Seq","VALIDATION","FAIRE-seq","SELEX","RIP-Seq","ChIA-PET",
    "Synthetic-Long-Read","Targeted-Capture",
    "Tethered Chromatin Conformation Capture","OTHER"]
lib_const_protocol = AttributeField("library_construction_protocol",
    "Library construction protocol",
    description="Free text library description", ena_requirement="mandatory")
lib_prep_date = AttributeField("library_preparation_date",
    "Library preparation date", type_="date",
    description="Date when the sequencing library was prepared.",
    ena_requirement="recommended")


def list_fields(which: str) -> List[AttributeField]:
    if which == "empty":
        return [AttributeField("", "")]
    if which == "basic":
        return [sample_name, sample_description]
    if which == "gisaid_assembly":
        return [virus_name, gisaid_submitter, gisaid_filename]
    if which == "ena_read":
        return [ena_sample_title, ena_study, ena_exp_title, ena_exp_alias,
                platform, instrument, insert_size, lib_source,
                lib_selection, lib_strategy, lib_const_protocol, lib_prep_date]
