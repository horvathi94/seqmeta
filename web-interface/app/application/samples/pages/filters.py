from enum import Enum


class GisaidSubmission(Enum):

    NONE = 0;
    SUBMITTED = 1;
    NOT_SUBMITTED = 2;


class HasConsensus(Enum):

    NONE = 0;
    HAS_FILE = 1;
    NO_FILE = 2;
