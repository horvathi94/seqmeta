import os.path
from datetime import datetime

class TempFile:

    save_dir = "/temp"
    tempfilename= "tmp"
    attachment_prefix = "prefix"
    extension = "txt"

    samples_temp_dir = "/uploads/samples/temp"


    @classmethod
    def get_tempfile(cls):
        return os.path.join(cls.save_dir, cls.tempfilename)


    @classmethod
    def get_attachment_filename(cls):
        return cls.attachement_prefix+str(datetime.now())+"."+cls.extension


    @classmethod
    def get_sample_temp_file(cls, filename: str) -> "os.path":
        if not os.path.exists(cls.files_temp_dir):
            os.makedirs(cls.files_temp_dir)
        return os.path.join(cls.files_temp_dir, filename)
