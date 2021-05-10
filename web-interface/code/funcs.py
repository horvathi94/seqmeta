from collections import OrderedDict

def form_to_dict_list(raw_form, main_key):

    raw_data = raw_form.to_dict();
    data = [];

    for key in raw_data:

        splits = key.split("[");
        entry_keys = [split.strip("]") for split in splits];

        if entry_keys[0] != main_key:
            continue;

        entry_id = int(entry_keys[1]);
        is_registered = False;
        for item in data:
            if item["id"] == entry_id:
                curr = item;
                is_registered = True;

        if not is_registered:
            curr = OrderedDict();
            curr["id"] = entry_id;
            data.append(curr);

        prop_key = entry_keys[2].replace("-", "_");
        curr[prop_key] = raw_data[key];

    return data;


def compare_ordereddicts(od1, od2):

    for item1, item2 in zip(od1.items(), od2.items()):
        if item1 != item2:
            return False;

    return True;
