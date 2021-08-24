from dataclasses import dataclass, replace, field as dfield
from . import requirements as rqs
from . import inputs as inps
from .sample_fields import SampleFields
from .options_list import _OPTIONS_LIST
from application.src.samples.samples import Samples
from application.src.defaults import DefaultValues
from application.src.seqfiles.db import DBSeqFile
from application.src.seqfiles.types import SeqFileTypes
from application.src.seqfiles.seqfile import SeqFile


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
    classes: list = dfield(default_factory=list);
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
                classes=self.classes, maxlength=self.max_val);
        if self.field_type == "number":
            self.input = inps.InputNumber(self.prefix, self.db_key,
                classes=self.classes,
                min_val=self.min_val, max_val=self.max_val, step=self.step);
        if self.field_type == "date":
            self.input = inps.InputDate(self.prefix, self.db_key,
                classes=self.classes,
                min_date=self.min_date, max_date=self.max_date);
        if self.field_type == "select":
            self.input = inps.InputSelect(self.prefix, self.db_key,
                                          classes=self.classes);
        if self.field_type == "radio":
            self.input = inps.InputRadio(self.prefix, self.db_key,
                                         classes=self.classes);
        if self.field_type == "seqfile":
            self.input = inps.InputSeqFile(self.prefix, self.db_key,
                                           classes=self.classes);
        if self.field_type == "seqfile_assembly":
            self.input = inps.InputSeqFile(self.prefix, self.db_key,
                                           classes=self.classes);


    def _parse_requirements(self) -> None:
        """Returns list of requirement levels from raw data."""
        for repo in rqs.RequirementRepos:
            rlevel = getattr(self, repo.value);
            if rlevel is None: continue;
            req = rqs.Requirement(repo.value,
                                  rqs.RequirementLevels(rlevel).name);
            self.requirements.append(req);


    def get_options_list(self):
        """Returns a list of all possible options for the handle."""
        func = _OPTIONS_LIST.get(self.handle_std, lambda: []);
        return func();


    def get_value(self, sample_id: int=0):
        """Returns the value that will be assigned to the fields."""
        if self.field_type == "seqfile":
            seqfile = SeqFile(sample_id, SeqFileTypes(self.db_key));
            return seqfile.fetch_filename();

        if self.field_type == "seqfile_assembly":
            if self.db_key == "consensus_assembly_method":
                sftype = SeqFileTypes.CONSENSUS_FILE;
            elif self.db_key == "contigs_assembly_method":
                sftype = SeqFileTypes.CONTIGS_FILE;
            elif self.db_key == "scaffolds_assembly_method":
                sftype = SeqFileTypes.SCAFFOLDS_FILE;
            seqfile = SeqFile(sample_id, sftype);
            return seqfile.assembly_method_id;

        if sample_id != 0:
            sampd = Samples.fetch_entry_edit(id=sample_id, id_key="sample_id");
            return sampd[self.db_key];

        defs = DefaultValues.fetch();
        if self.db_key in defs and defs[self.db_key] is not None:
            return defs[self.db_key];

        if self.field_type in ["select", "radio"]:
            return 0;

        return "";


    def get_value_from_sample(self, sample: "Sample"):
        """Returns the value that will be assigned to the field from sample."""
        if self.field_type == "seqfile":
            ftype = self.db_key.replace("_file", "");
            return SeqFile.fetch_filename(sample["sample_id"], ftype=ftype);

        if self.field_type == "seqfile_assembly":
            print(f"Value from sample: {1}", file=sys.stderr)
            return 1;
        return sample[self.db_key];


    def copy(self):
        return replace(self);

