from typing import List

def parse(raw: dict, main_key: str) -> List[dict]:
    cleaned = {}
    for item, value in raw.items():
        mk, index, attr_name = item.split("+")
        if mk != main_key: continue
        if index not in cleaned: cleaned[index] = {}
        cleaned[index][attr_name] = value
    return list(cleaned.values())
