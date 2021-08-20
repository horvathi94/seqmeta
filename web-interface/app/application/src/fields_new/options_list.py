from .sample_fields import SampleFields as SF
from application.src.authors import Authors, AuthorGroups
from application.src import misc


_OPTIONS_LIST = {

    SF.COLLECTOR_NAME: Authors.fetch_select_list,
    SF.LOC_CONTINENT: misc.Continents.fetch_list,

};



