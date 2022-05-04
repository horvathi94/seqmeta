import pathlib
import pickle


class PickleFile:

    BASE_PATH = pathlib.Path("/home/seqmeta/uploads/samples/")


    @classmethod
    def check_extension(cls, fname: str) -> bool:
        if fname.split(".")[-1] == cls.extension: return True
        return False


    @property
    def filename(self) -> str:
        return self.name + "." + self.extension


    @property
    def path(self) -> str:
        return pathlib.Path(self.BASE_PATH, self.template_name)


    @property
    def file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.filename)


    def save(self, create_path: bool=False) -> None:
        path = pathlib.Path(self.path)
        if create_path: path.mkdir(parents=True, exist_ok=True)
        if not path.is_dir: return
        with open(self.file, "wb") as f:
            pickle.dump(self, f)


    @staticmethod
    def load_pickle(pickle_file: pathlib.Path) -> object:
        if not pathlib.Path(pickle_file).is_file(): return
        with open(pickle_file, "rb") as f:
            obj = pickle.load(f)
        return obj


    @classmethod
    def list_names(cls) -> list:
        return []


    @classmethod
    def list_all(cls) -> list:
        items = []
        for name in cls.list_names():
            items.append(cls.load(name))
        return items
