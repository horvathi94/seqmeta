import pathlib
import pickle


class PickleFile:

    @classmethod
    def create_filename(cls, fname: str) -> str:
        return fname + "." + cls.extension


    @classmethod
    def create_file(cls, fname: str) -> pathlib.Path:
        return pathlib.Path(cls.path, fname)


    @property
    def filename(self) -> str:
        return self.create_filename(self.name)


    @property
    def file(self) -> pathlib.Path:
        return self.create_file(self.filename)


    def save(self, overwrite: str=None) -> None:
        with open(self.file, "wb") as f:
            pickle.dump(self, f)
        if overwrite is None: return
        old_filename = self.create_filename(overwrite)
        old_file = self.create_file(old_filename)
        old_file.unlink()


    @classmethod
    def load_pickle(cls, pickle_file: pathlib.Path) -> object:
        if not pathlib.Path(pickle_file).is_file(): return
        with open(pickle_file, "rb") as f:
            obj = pickle.load(f)
        return obj


    @classmethod
    def load(cls, name: str) -> None:
        filename = cls.create_filename(name)
        file = cls.create_file(filename)
        return cls.load_pickle(file)


    @classmethod
    def list_all(cls) -> list:
        items = []
        for f in list(cls.path.glob("*."+cls.extension)):
            items.append(cls.load_pickle(f))
        return items

