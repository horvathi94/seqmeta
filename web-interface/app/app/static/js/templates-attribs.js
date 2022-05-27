function newAttrObj(e){return(obj=Object.create(ATTRIBUTE)).general_name=e,obj}function get_gisaid_assembly_fields(){return(virus_name=newAttrObj("gisaid_virusname")).label="GISAID virus name",virus_name.description="Virus name of the sample.",virus_name.gisaid_requirement="mandatory",virus_name.gisaid_name="Virus name",virus_name.gisaid_header="covv_virus_name",(submitter=newAttrObj("gisaid_submitter")).label="GISAID submitter",submitter.description="Username of person who will submit data to GISAID.",submitter.gisaid_requirement="mandatory",submitter.gisaid_name="Submitter",submitter.gisaid_header="submitter",(file=newAttrObj("gisaid_filename")).label="GISAID filename",file.description="Name of file which will be uploaded.",file.gisaid_requirement="mandatory",file.gisaid_name="FASTA filename",file.gisaid_header="fn",file.default="sequences",[virus_name,submitter,file]}function get_ena_read_fields(){return(title=newAttrObj("ena_title")).label="Sample title",title.description="Title of the sample.",title.ena_requirement="mandatory",(study=newAttrObj("ena_study")).label="ENA study accession",study.description="Accession of study to which to upload the sample.",study.ena_requirement="mandatory",(platform=newAttrObj("platform")).label="Platform",platform.type_="select",platform.description="Not needed if INSTRUMENT is provided. See <a href='https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#platform'>link</a> for more details.",platform.ena_requirement="optional",platform.options=["LS454","ILLUMINA","PACBIO_SMRT","ION_TORRENT","CAPILLARY","OXFORD_NANOPORE","BGISEQ","DNBSEQ"],(instrument=newAttrObj("instrument")).label="Instrument",instrument.type_="select",instrument.description="See <a href='https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#instrument'>link</a> for more details.",instrument.ena_requirement="optional",instrument.options=["454 GS","454 GS 20","454 GS FLX","454 GS FLX+","454 GS FLX Titanium","454 GS Junior","HiSeq X Five","HiSeq X Ten","Illumina Genome Analyzer","Illumina Genome Analyzer II","Illumina Genome Analyzer IIx","Illumina HiScanSQ","Illumina HiSeq 1000","Illumina HiSeq 1500","Illumina HiSeq 2000","Illumina HiSeq 2500","Illumina HiSeq 3000","Illumina HiSeq 4000","Illumina iSeq 100","Illumina MiSeq","Illumina MiniSeq","Illumina NovaSeq 6000","NextSeq 500","NextSeq 550","PacBio RS","PacBio RS II","Sequel","Ion Torrent PGM","Ion Torrent Proton","Ion Torrent S5","Ion Torrent S5 XL","AB 3730xL Genetic Analyzer","AB 3730 Genetic Analyzer","AB 3500xL Genetic Analyzer","AB 3500 Genetic Analyzer","AB 3130xL Genetic Analyzer","AB 3130 Genetic Analyzer","AB 310 Genetic Analyzer","MinION","GridION","PromethION","BGISEQ-500","DNBSEQ-T7","DNBSEQ-G400","DNBSEQ-G50","DNBSEQ-G400 FAST","unspecified"],(insert_size=newAttrObj("insert_size")).label="Insert size",insert_size.description="Insert size for paired reads.",insert_size.ena_requirement="optional",insert_size.pattern="(^[1-9][0-9]*$)",(library_name=newAttrObj("library_name")).label="Library name",library_name.description="Library name.",library_name.ena_requirement="optional",(library_source=newAttrObj("library_source")).label="Library source",library_source.type_="select",library_source.description="See <a href='https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#source'>link</a> for more details.",library_source.ena_requirement="mandatory",library_source.options=["GENOMIC","GENOMIC SINGLE CELL","TRANSCRIPTOMIC","TRANSCRIPTOMIC SINGLE CELL","METAGENOMIC","METATRANSCRIPTOMIC","SYNTHETIC","VIRAL RNA","OTHER"],(library_selection=newAttrObj("library_selection")).label="Library selection",library_selection.type_="select",library_selection.description="See <a href='https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#selection'>link</a> for more details.",library_selection.ena_requirement="mandatory",library_selection.options=["RANDOM","PCR","RANDOM PCR","RT-PCR","HMPR","MF","repeat fractionation","size fractionation","MSLL","cDNA","cDNA_randomPriming","cDNA_oligo_dT","PolyA","Oligo-dT","Inverse rRNA","Inverse rRNA selection","ChIP","ChIP-Seq","MNase","DNase","Hybrid Selection","Reduced Representation","Restriction Digest","5-methylcytidine antibody","MBD2 protein methyl-CpG binding domain","CAGE","RACE","MDA","padlock probes capture method","other","unspecified"],(library_strategy=newAttrObj("library_strategy")).label="Library strategy",library_strategy.type_="select",library_strategy.description="See <a href='https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html#strategy'>link</a> for more details.",library_strategy.ena_requirement="mandatory",library_strategy.options=["WGS","WGA","WXS","RNA-Seq","ssRNA-seq","miRNA-Seq","ncRNA-Seq","FL-cDNA","EST","Hi-C","ATAC-seq","WCS","RAD-Seq","CLONE","POOLCLONE","AMPLICON","CLONEEND","FINISHING","ChIP-Seq","MNase-Seq","DNase-Hypersensitivity","Bisulfite-Seq","CTS","MRE-Seq","MeDIP-Seq","MBD-Seq","Tn-Seq","VALIDATION","FAIRE-seq","SELEX","RIP-Seq","ChIA-PET","Synthetic-Long-Read","Targeted-Capture","Tethered Chromatin Conformation Capture","OTHER"],(experiment_description=newAttrObj("library_construction_protocol")).label="Experiment description",experiment_description.description="Free text library description.",experiment_description.ena_requirement="optional",(experiment_name=newAttrObj("ena_experiment_name")).label="Unique name of experiment.",experiment_name.description="Unique name of the experiment",experiment_name.ena_requirement="mandatory",(lib_prep_date=newAttrObj("library_preparation_date")).label="Library preparation date.",lib_prep_date.description="Date when the sequencing library was prepared.",lib_prep_date.ena_requirement="optional",[title,study,experiment_name,platform,instrument,insert_size,library_name,library_source,library_selection,library_strategy,experiment_description]}ATTRIBUTE={general_name:"",label:"",type_:"text",description:"",ena_requirement:"exclude",ena_name:"",ena_units:[],gisaid_requirement:"exclude",gisaid_name:"",gisaid_header:"",pattern:"",options:[],default:""};