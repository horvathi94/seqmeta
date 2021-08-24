import os
from ..base.tempfile import TempFile


class EnaManifestRun(TempFile):

    tempfilename = "last_generated_ena_runs_manifest.txt";
    attachment_prefix = "ena";
    extension = "txt";
    zip_dir = "reads";

    @classmethod
    def zip_file_manifest(cls, name: str) -> str:
        return os.path.join(cls.zip_dir, name+"_manifest.txt");


    @classmethod
    def write(cls, sample):
        with open(cls.get_tempfile(), "w") as wf:
            wf.write("STUDY\t\t<copy study name here!>\n");
            wf.write(f"SAMPLE\t\t{sample['sample_alias']}\n");
            wf.write(f"NAME\t\t{sample['sample_alias']}\n");
            wf.write(f"INSTRUMENT\t\t{sample['instrument_model']}\n");
            wf.write(f"INSERT_SIZE\t\t{sample['insert_size']}\n");
            wf.write(f"LIBRARY_SOURCE\t\t{sample['library_source']}\n");
            wf.write(f"LIBRARY_SELECTION\t\t{sample['library_selection']}\n");
            wf.write(f"LIBRARY_STRATEGY\t\t{sample['library_strategy']}\n");
            wf.write(f"FASTQ\t\t{sample['forward_file_name']}\n");
            wf.write(f"FASTQ\t\t{sample['reverse_file_name']}\n");
