from .base import _EnaManifestBase



class EnaManifestRun(_EnaManifestBase):

    zip_dir = "reads";



    @classmethod
    def write(cls, sample: dict, read_names: list) -> None:
        with open(cls.get_tempfile(), "w") as wf:
            wf.write("STUDY\t\t<copy study name here!>\n");
            wf.write(f"SAMPLE\t\t{sample['sample_alias']}\n");
            wf.write(f"NAME\t\t{sample['sample_alias']}\n");
            wf.write(f"INSTRUMENT\t\t{sample['instrument_model']}\n");
            wf.write(f"INSERT_SIZE\t\t{sample['insert_size']}\n");
            wf.write(f"LIBRARY_SOURCE\t\t{sample['library_source']}\n");
            wf.write(f"LIBRARY_SELECTION\t\t{sample['library_selection']}\n");
            wf.write(f"LIBRARY_STRATEGY\t\t{sample['library_strategy']}\n");
            for r in read_names:
                wf.write(f"FASTQ\t\t{r}\n");
