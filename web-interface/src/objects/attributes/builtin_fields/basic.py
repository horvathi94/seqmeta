SAMPLE_NAME = {
    "general_name": "sample_name",
    "label": "Sample name",
    "description": "Unique name of sample",
    "is_unique": True,
    "is_fixed": True,
    "_gisaid_requirement": "mandatory",
    "_ena_requirement": "mandatory"}

SAMPLE_DESCRIPTION = {
    "general_name": "short_description",
    "label": "Short description",
    "description": "A short description of the sample for easier " \
        "identification (this will not be part of any submission).",
    "is_fixed": True}


ALL_FIELDS = [SAMPLE_NAME, SAMPLE_DESCRIPTION]
