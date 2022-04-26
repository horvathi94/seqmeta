import pathlib
import pickle
from dataclasses import dataclass, field, asdict
from typing import List
from .attribute import Attribute


@dataclass
class Template:

    path: pathlib.Path = pathlib.Path("/home/seqmeta/uploads/samples/")
#    id: int = None
    name: str = None
    short_description: str = None
    attributes: List[Attribute] = field(default_factory=lambda: [])


#    def __post_init__(self):
#        if self.id is not None: self.id = int(self.id)


    def add_attribute(self, a: Attribute) -> None:
        self.attributes.append(a)


    def asdict(self) -> dict:
        return asdict(self)


    def asjson(self) -> dict:
        return {
            "name": self.name,
            "attributes": [a.asjson() for a in self.attributes]
        }

    @property
    def attribute_count(self) -> int:
        return len(self.attributes)


    @property
    def filename(self) -> str:
        return self.name + ".template"


    @filename.setter
    def filename(self, fname: str) -> None:
        self.name = pathlib.Path(fname).stem


    @property
    def pickle_file(self) -> pathlib.PurePath:
        return pathlib.PurePath(self.path, self.filename)


    def save(self) -> None:
        with open(self.pickle_file, "wb") as f:
            pickle.dump(self, f)


    def load(self) -> None:
        t = load_pickle(self.pickle_file)
        print(t)
        for a in t.attributes:
            self.add_attribute(a)



def load_pickle(pickle_file: pathlib.Path) -> Template:
    if not pathlib.Path(pickle_file).is_file(): return
    with open(pickle_file, "rb") as f:
        t = pickle.load(f)
    return t


def list_templates() -> List[Template]:
    template_files = list(Template.path.glob("*.template"))
    return [load_pickle(tf) for tf in template_files]
