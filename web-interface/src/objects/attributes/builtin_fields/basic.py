SAMPLE_NAME = {
    "general_name": "sample_name",
    "label": "Sample name",
    "description": "Unique name of sample",
    "_is_unique": True,
    "must_be_unique": True,
    "is_mandatory": True,
    "has_fixed_name": True}

SAMPLE_DESCRIPTION = {
    "general_name": "short_description",
    "label": "Short description",
    "description": "A short description of the sample for easier " \
        "identification (this will not be part of any submission).",
    "has_fixed_name": True,
    "is_mandatory": True}


ALL_FIELDS = [SAMPLE_NAME, SAMPLE_DESCRIPTION]
