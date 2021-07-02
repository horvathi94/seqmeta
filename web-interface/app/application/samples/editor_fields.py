from application.src.authors import Authors, AuthorGroups



FIELDS_LIST = [

    "sample_name",
    "sample_comment",
    "sample_title",
    "sample_description",
    "collection_year",
    "collection_month",
    "collection_day",
    "collector_name",

];


DLIST = {

    "collector_name": Authors.fetch_list_labeled(
        replace_key="abbreviated_middle_name"),

}


