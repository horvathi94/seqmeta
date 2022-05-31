from typing import List


def parse(raw: dict, main_key: str) -> List[dict]:
    cleaned = {}
    for item, value in raw.items():
        if len(item.split("+")) != 3: continue
        mk, index, attr_name = item.split("+")
        if mk != main_key: continue
        index = int(index)
        if index not in cleaned: cleaned[index] = {}
        cleaned[index][attr_name] = value
    return cleaned



def files_to_dict(raw: dict) -> list:
    cleaned = {}
    for field in raw.keys():
        field_name, index, file_type = field.split("+")
        if file_type not in cleaned:
            cleaned[file_type] = []
        field_dict = {"name": field_name, "index": int(index),
                      "data": raw.getlist(field)}
        cleaned[file_type].append(field_dict)
    return cleaned



def fetch_files(uploaded_files: dict, file_type: str,
                sample_name: str, sample_id: int) -> list:

    selected = uploaded_files[file_type]
    single_files = []
    multi_files = []

    for field in selected:

        # Look for files uploded to this specific field
        if field["name"] == "sample" and field["index"] == sample_id:
            multi_files = [f for f in field["data"] if f.filename]

        # Look for files uploaded to edit all field
        if field["name"] == "uploadedfiles":
            for f in field["data"]:
                if f.filename == "": continue
                sname = f.filename.split(".")[0].split("_")[0]
                if sname == sample_name:
                    single_files.append(f)

    if len(single_files) > 0:
        return single_files

    return multi_files
