from collections import OrderedDict

def parse_form_list(form_data, main_key):

    res = [];

    for key in form_data:

        splits = key.split("+");

        if splits[0] != main_key:
            continue;

        indx = int(splits[1]);
        prop = splits[2];

        is_registered = False;
        for od in res:
            if od["id"] == indx:
                curr_od = od;
                is_registered = True;

        if not is_registered:
            curr_od = OrderedDict();
            curr_od["id"] = indx;

        curr_od[prop] = form_data[key];

        if not is_registered:
            res.append(curr_od);

    return res;

