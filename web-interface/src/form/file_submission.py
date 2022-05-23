def fetch_files(raw: dict, sample_name: str, sid: int, ftype: str) -> list:

    all_field = []
    single_field = []

    for field_name in raw:

        field, index, file_type = field_name.split("+")
        if file_type != ftype: continue
        index = int(index)


        if field == "uploadedfiles":

            for upfile in raw.getlist(field_name):
                if upfile.filename == "": continue

                sname = upfile.filename.split(".")[0].split("_")[0]
                if sname != sample_name: continue

                all_field.append(upfile)

        else:

            if index != sid: continue

            for upfile in raw.getlist(field_name):
                if upfile.filename == "": continue

                single_field.append(upfile)

    if len(single_field) > 0:
        return single_field

    return all_field
