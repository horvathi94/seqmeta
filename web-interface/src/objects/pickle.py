import pathlib
import pickle


class PickleFile:

    @classmethod
    def filename(cls, name: str) -> str:
        return name + "." + cls.extension


    @classmethod
    def path(cls, name: str) -> str:
        return pathlib.Path(cls.path_base, name)


    @classmethod
    def file(cls, name: str) -> pathlib.Path:
        return pathlib.Path(cls.path(name), cls.filename(name))


    def save(self, create_path: bool=False) -> None:
        path = self.path(self.name)
        if create_path: path.mkdir(parents=True, exist_ok=True)
        if not path.is_dir: return
        with open(self.file(self.name), "wb") as f:
            pickle.dump(self, f)


    @staticmethod
    def load_pickle(pickle_file: pathlib.Path) -> object:
        if not pathlib.Path(pickle_file).is_file(): return
        with open(pickle_file, "rb") as f:
            obj = pickle.load(f)
        return obj


    @classmethod
    def load(cls, name: str) -> None:
        return cls.load_pickle(cls.file(name))


    @classmethod
    def list_names(cls) -> list:
        return []


    @classmethod
    def list_all(cls) -> list:
        items = []
        for n in cls.list_names():
            items.append(cls.load_pickle(cls.file(n)))
        return items
