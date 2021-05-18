from collections import OrderedDict


def record_to_ordereddict(record, column_names):
    od = OrderedDict();
    for i, col in enumerate(column_names):
        od[col] = record[i];
    return od;


def parse_records(records, column_names):
    parsed = [];
    for record in records:
        parsed.append(record_to_ordereddict(record, column_names));
    return parsed;


def create_empty_ordereddict(describe):

    empty_od = OrderedDict();
    empty_od["id"] = 0;

    for col in describe:
        if str(col[0]) == "id":
            continue;

        dtype = "text";
        val = "";
        if "int" in str(col[1]):
            dtype = "int";
            val = 0;
        elif "decimal" in str(col[1]):
            dtype = "float"
            val = 0;

        if col[4] != None:
            if dtype == "int":
                val = int(col[4]);
            elif dtype == "float":
                val = float(col[4]);
            elif dtype == "text":
                val = str(col[4]);

        empty_od[str(col[0])] = val;

    return empty_od;


def clean_value(value):
    if isinstance(value, str):
        value = value.strip();
    return value;
