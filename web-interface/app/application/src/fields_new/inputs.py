from dataclasses import dataclass


@dataclass
class _InputBase:

    prefix: str;
    db_key: str;
    name_single: str = "";
    multi_all: str = "";
    multi_template: str = "";
    defaults: str = "";
    classes: str = "";
    onchange: str = "";
    value: str = "";

    def __post_init__(self):
        self.name_single = self.prefix + "+" + self.db_key;
        self.multi_all = self.prefix + "-" + self.db_key + "-all";
        self.multi_template = self.prefix + "+0+" +self.db_key;


    def replace_id_in_template_name(self, sample_id: int=0) -> None:
        self.multi_template = \
            self.multi_template.replace("+0+", "+"+str(sample_id)+"+");



@dataclass
class InputText(_InputBase):

    maxlength: int = None;

    def __post_init__(self):
        super().__post_init__();
        self.maxlength = 0 if self.maxlength is None else self.maxlength;



@dataclass
class InputNumber(_InputBase):

    min_val: float = None;
    max_val: float = None;
    step: float = None;

    def __post_init__(self):
        super().__post_init__();
        self.min_val = "" if self.min_val is None else float(self.min_val);
        self.max_val = "" if self.max_val is None else float(self.max_val);
        self.step = 1 if self.step is None else float(self.step);



@dataclass
class InputDate(_InputBase):

    min_date: "date" = None;
    max_date: "date" = None;

    def __post_init__(self):
        super().__post_init__();
        self.min_date = "" if self.min_date is None \
            else self.min_date.strftime("%Y-%m-%d");
        self.max_date = "" if self.max_date is None \
            else self.max_date.strftime("%Y-%m-%d");



@dataclass
class InputSeqFile(_InputBase):

    def __post_init__(self):
        super().__post_init__();
        self.file_type = self.db_key;


@dataclass
class InputSelect(_InputBase):

    value: int = 0;


@dataclass
class InputRadio(_InputBase):

    value: int = 0;
