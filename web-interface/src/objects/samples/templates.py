import pathlib
import pickle
from typing import List
from .template import Template
from werkzeug.utils import secure_filename


class PickleList:

    path = None
    extension = None


    @classmethod
    def load_pickle(cls, pickle_file: pathlib.Path) -> object:
        if not pathlib.Path(pickle_file).is_file(): return
        with open(pickle_file, "rb") as f:
            data = pickle.load(f)
        return data


    @property
    def files(self) -> list:
        return list(self.path.glob(f"*{self.extension}"))


    def load(self) -> List[object]:
        return [self.load_pickle(f) for f in self.files]


    def load_names(self) -> List[str]:
        names = []
        for f in self.files:
            t = self.load_pickle(f)
            names.append(t.name)
        return names


    @classmethod
    def name_picklefile(cls, name: str) -> str:
        return pathlib.Path(cls.path, f"{name}{cls.extension}")


    def load_by_name(self, name: str) -> object:
        return self.load_pickle(self.name_picklefile(name))


    def save(self, obj: object) -> None:
        with open(self.name_picklefile(obj.name), "wb") as f:
            pickle.dump(obj, f)



class TemplatesList(PickleList):

    path = pathlib.Path("/home/seqmeta/uploads/samples/")
    extension = ".template"


class SamplesList(PickleList):

    path = pathlib.Path("/home/seqmeta/uploads/samples/")
    extension = ".sample"


    @classmethod
    def load_pickle(cls, pickle_file: pathlib.Path) -> object:
        if not pathlib.Path(pickle_file).is_file(): return
        with open(pickle_file, "rb") as f:
            sample = pickle.load(f)
        sample._load_template()
        return sample
