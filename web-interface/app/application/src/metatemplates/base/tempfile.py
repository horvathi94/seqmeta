import os.path
from datetime import datetime

class TempFile:

    save_dir = "/temp";
    tempfilename= "tmp";
    attachment_prefix = "prefix";
    extension = "txt";

    @classmethod
    def get_tempfile(cls):
        return os.path.join(cls.save_dir, cls.tempfilename);

    @classmethod
    def get_attachment_filename(cls):
        return cls.attachement_prefix+str(datetime.now())+"."+cls.extension;
