import os
from ..base.tempfile import TempFile


class EnaManifestAssembly(TempFile):

    tempfilename = "last_generated_ena_assmebly_manifest.txt";
    attachment_prefix = "ena";
    extension = "txt";

    zip_dir = "assemblies";
    level = "";

    @classmethod
    def manifest_in_zip(cls, name: str) -> str:
        fname = f"{name}_{cls.level}_manifest.txt";
        return os.path.join(cls.zip_dir, fname);


    @classmethod
    def write(cls, sample):
        filename = f"{cls.level}_filename";
        with open(cls.get_tempfile(), "w") as wf:
            wf.write("STUDY\t\t<copy study name here!>\n");
            wf.write(f"SAMPLE\t\t{sample['sample_name']}\n");
            wf.write(f"ASSEMBLYNAME\t\t{sample['sample_name']}_{cls.level}\n");
            wf.write(f"ASSEMBLY_TYPE\t\tCOVID-19 outbreak\n");
            wf.write(f"COVERAGE\t\t{sample['COVERAGE']}\n");
            wf.write(f"PROGRAM\t\t{sample['PROGRAM']}\n");
            wf.write(f"PLATFORM\t\t{sample['PLATFORM']}\n");
            wf.write(f"DESCRIPTION\t\t{sample['DESCRIPTION']}\n");
            wf.write(f"RUN_REF\t\t<RUN_REF>\n");
            wf.write(f"FASTA\t\t{sample[filename]}.gz\n");


class EnaContigs(EnaManifestAssembly):

    level = "contigs";


class EnaScaffolds(EnaManifestAssembly):

    level = "scaffolds";
