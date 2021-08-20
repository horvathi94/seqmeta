from dataclasses import dataclass


@dataclass
class _InputBase:

    prefix: str;
    db_key: str;
    name_single: str = "";
    multi_all: str = "";
    multi_template: str = "";
    defaults: str = "";
    class_name: str = "";
    onchange: str = "";
    value: str = "";

    def __post_init__(self):
        self.name_single = self.prefix + "+" + self.db_key;
        self.multi_all = self.prefix + "-" + self.db_key + "-all";
        self.multi_template = self.prefix + "+0+" +self.db_key;


@dataclass
class InputText(_InputBase):

    maxlength: str = None;

    def __post_init__(self):
        self.maxlength = "" if self.maxlength is None else self.maxlength;



@dataclass
class InputNumber(_InputBase):

    min_val: float = None;
    max_val: float = None;
    step: float = None;

    def __post_init__(self):
        self.min_val = "" if self.min_val is None else float(self.min_val);
        self.max_val = "" if self.max_val is None else float(self.max_val);
        self.step = 1 if self.step is None else float(self.step);



@dataclass
class InputDate(_InputBase):

    min_date: "date" = None;
    max_date: "date" = None;

    def __post_init__(self):
        self.min_date = "" if self.min_date is None else strftime("%Y-%m-%d");
        self.max_date = "" if self.max_date is None else strftime("%Y-%m-%d");



@dataclass
class InputSeqFile(_InputBase):

    def __post_init__(self):
        self.file_type = self.db_key;


@dataclass
class InputSelect(_InputBase):

    value: int = 0;

