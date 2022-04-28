from dataclasses import dataclass

@dataclass
class Taxonomy:

    taxonomy_id: str = None
    scientific_name: str = None
    common_name: str = None

    def update(self, taxon: dict) -> None:
        for key, val in taxon.items():
            if not hasattr(self, key): continue
            setattr(self, key, val)


    @property
    def display_string(self) -> str:
        return f"{self.scientific_name} ({self.taxonomy_id})"
