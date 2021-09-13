from .base import _EnaManifestBase

import sys


class EnaManifestAssembly(_EnaManifestBase):

    zip_dir = "assemblies";
    level = "";
    assembly_methods_key = "";


    @classmethod
    def manifest_in_zip(cls, name: str) -> str:
        fname = f"{name}_{cls.level}_manifest.txt";
        return cls.in_zip(fname);


    @classmethod
    def write(cls, sample):
        filename = f"{cls.level}_filename";
        with open(cls.get_tempfile(), "w") as wf:
            wf.write("STUDY\t\t<copy study name here!>\n");
            wf.write(f"SAMPLE\t\t{sample['sample_name']}\n");
            wf.write(f"ASSEMBLYNAME\t\t{sample['sample_name']}_{cls.level}\n");
            wf.write(f"ASSEMBLY_TYPE\t\tCOVID-19 outbreak\n");
            wf.write(f"COVERAGE\t\t{sample['COVERAGE']}\n");
            wf.write(f"PROGRAM\t\t{sample[cls.assembly_method_key]}\n");
            wf.write(f"PLATFORM\t\t{sample['PLATFORM']}\n");
            if sample["DESCRIPTION"] != "":
                wf.write(f"DESCRIPTION\t\t{sample['DESCRIPTION']}\n");
            wf.write(f"RUN_REF\t\t<RUN_REF>\n");
            wf.write(f"FASTA\t\t{sample[filename]}.gz\n");



class EnaContigs(EnaManifestAssembly):

    level = "contigs";
    assembly_method_key = "contigs_assembly_method";


class EnaScaffolds(EnaManifestAssembly):

    level = "scaffolds";
    assembly_method_key = "scaffolds_assembly_method";
