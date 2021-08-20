from dataclasses import dataclass, field as dfield
from . import requirements as rqs
from . import inputs as inps
from .sample_fields import SampleFields
from .options_list import _OPTIONS_LIST
from application.src.samples.samples import Samples
from application.src.defaults import DefaultValues
from application.src.seqfiles.db import SeqFile


import sys


@dataclass
class Field:

    handle: str = "";
    field_name: str = "";
    field_type: str = "";
    gisaid: int = None;
    ena: int = None;
    ncbi: int = None;
    db_key: str = "";
    class_name: str = "";
    edit_all: bool = False;
    min_val: str = None;
    max_val: str = None;
    step: int = None;
    min_date: str = None;
    max_date: str = None;
    prefix: str = "";
    description: str = "";
    file_type: str = "";
    requirements: list = dfield(default_factory=list);
    input: inps._InputBase = None;
    options: list = dfield(default_factory=list);

    handle_std: SampleFields = SampleFields.NONE;


    def __post_init__(self):
        self.handle_std = SampleFields(self.handle);
        self._parse_requirements();
        self.options = self.get_options_list();
        if self.field_type == "text":
            self.input = inps.InputText(self.prefix, self.db_key,
                                   maxlength=self.max_val);
        if self.field_type == "number":
            self.input = inps.InputNumber(self.prefix, self.db_key,
                min_val=self.min_val, max_val=self.max_val, step=self.step);
        if self.field_type == "date":
            self.input = inps.InputDate(self.prefix, self.db_key,
                            min_date=self.min_date, max_date=self.max_date);
        if self.field_type == "select":
            self.input = inps.InputSelect(self.prefix, self.db_key);
        if self.field_type == "seqfile":
            self.input = inps.InputSeqFile(self.prefix, self.db_key);


    def _parse_requirements(self) -> None:
        """Returns list of requirement levels from raw data."""
        for repo in rqs.RequirementRepos:
            rlevel = getattr(self, repo.value);
            if rlevel is None: continue;
            req = rqs.Requirement(repo.value,
                                  rqs.RequirementLevels(rlevel).value);
            self.requirements.append(req);


    def get_options_list(self):
        """Returns a list of all possible options for the handle."""
        func = _OPTIONS_LIST.get(self.handle_std, lambda: []);
        return func();


    def get_value(self, sample_id: int=0):
        """Returns the value that will be assigned to the fields."""
        if self.field_type == "seqfile":
            ftype = self.db_key.replace("_file", "");
            return SeqFile.fetch_filename(sample_id, ftype=ftype);

        if sample_id != 0:
            sampd = Samples.fetch_entry_edit(id=sample_id, id_key="sample_id");
            return sampd[self.db_key];

        defs = DefaultValues.fetch();
        if self.db_key in defs and defs[self.db_key] is not None:
            return defs[self.db_key];

        if self.field_type in ["select", "radio"]:
            return 0;

        return "";


