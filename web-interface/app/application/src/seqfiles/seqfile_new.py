import os
from dataclasses import dataclass
from application.src.db.interface import DBInterface
from application.src.db.cursor import Cursor
from .types import AssemblyLevels, SeqFileTypes


import sys

class SeqFileException(Exception):

    def __init__(self, msg=""):
        self.msg = f"SeqFile failed: {msg}";
        super().__init__(self.msg);



@dataclass
class SeqFile:

    seqtype: SeqFileTypes;
    sample_id: int = 0;
    sample_name: str = None;
    file_extension_id: int = None;
    file_extension: str = None;
    assembly_method_id: int = None;
    assembly_method: str = None;
    file_data: str = None;


    def __post_init__(self):
        print(f"Post init: {self}", file=sys.stderr)
        if self.sample_id != 0:
            self._init_from_database();


    def is_assembly(self) -> bool:
        return SeqFileTypes.is_assembly(self.seqtype);


    def get_assembly_level(self) -> int:
        return SeqFileTypes.get_assembly_level(self.seqtype).value;


    def is_forward_read(self) -> bool:
        return SeqFileTypes.is_forward_read(self.seqtype);


    def _init_from_database(self) -> None:
        fields = ["sample_name",
                  "file_extension_id", "file_extension",
                  "assembly_method_id", "assembly_method"];

        where = f"WHERE `sample_id` = {self.sample_id}";
        where+= f" AND is_assembly IS {self.is_assembly()}";
        if self.seqtype in SeqFileTypes.list_assemblies():
            where+= f" AND assembly_level = {self.get_assembly_level()}";
        if self.seqtype in SeqFileTypes.list_reads():
            where+= f" AND is_forward_read IS {self.is_forward_read()}";

        raw ,= Cursor.select("view_seqfiles", fields=fields, clauses=where);
        if "id" in raw and raw["id"] == 0: return;
        self.sample_name = raw["sample_name"];
        self.file_extension_id = raw["file_extension_id"];
        self.file_extension = raw["file_extension"];
        self.assembly_method_id = raw["assembly_method_id"];
        self.assembly_method = raw["assembly_method"];


    def get_path(self) -> "os.path":
        path = SeqFileTypes.get_path(self.seqtype);
        if path is None: raise SeqFileException("could not get path.");
        return path;


    def get_filename(self) -> str:
        if self.sample_name is None:
            raise SeqFileException("sample_name is not defined.");
        if self.file_extension is None:
            raise SeqFileException("file_extension is not defined.");
        spec = SeqFileTypes.get_filename_extension(self.seqtype);
        if spec is None:
            raise SeqFileException("could not get spec string.");
        return f"{self.sample_name}_{spec}.{self.file_extension}";


    def get_file(self) -> "os.path":
        return os.path.join(self.get_path(), self.get_filename());


    def check_exists(self) -> bool:
        try:
            file = self.get_file();
        except:
            return False;
        return os.path.exists(file);


    def get_list_display(self) -> dict:
        try:
            filename = self.get_filename();
        except:
            filename = "No file was found.";
        return {"exists": self.check_exists(),
                "filename": filename};


    def get_details_display(self) -> dict:
        d = self.get_list_display();
        d["is_assembly"] = self.is_assembly();
        d["assembly_level"] = self.get_assembly_level();
        d["assembly_method"] = self.assembly_method;
        return d;


    def get_display_name(self) -> str:
        try:
            disp = self.get_filename();
        except:
            disp = "No file found";
        return disp;



    def save_file(self) -> None:
        try:
            file = self.get_file();
        except:
            raise Exception("Failed to save file data.");
        self.file_data.save(file);


    def save(self):
        pass
