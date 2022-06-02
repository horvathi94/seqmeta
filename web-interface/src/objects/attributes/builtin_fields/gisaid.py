VIRUS_NAME = {
    "general_name": "virus_name",
    "label": "GISAID virus name",
    "description": "Visrus name of the sample.",
    "gisaid_name": "Virus name",
    "_gisaid_requirement": "mandatory",
    "gisaid_header": "covv_virus_name"}

SUBMITTER = {
    "general_name": "gisaid_submitter",
    "label": "GISAID submitter",
    "description": "Username of person submitting to GISAID.",
    "gisaid_name": "Submitter",
    "_gisaid_requirement": "mandatory",
    "gisaid_header": "submitter"}

FILENAME = {
    "general_name": "gisaid_filename",
    "label": "GISAID filename",
    "description": "Name of file to be uploaded to GISAID.",
    "gisaid_name": "FASTA filename",
    "_gisaid_requirement": "mandatory",
    "gisaid_header": "fn",
    "default": "sequences"}

ALL_FIELDS = [VIRUS_NAME, SUBMITTER, FILENAME]
