from .xml import XML
from xml.dom import minidom


class RunSetXML(XML):


    def __init__(self, fname="runs"):
        super().__init__(root="RUNS_SET", fname=fname)


    def file_xml(self, seqfile: "SeqFile") -> minidom.Element:
        attrs = {
            "filename": str(seqfile.file),
            "filetype": seqfile.filetype,
            "checksum_method": "MD5",
            "checksum": seqfile.md5_checksum()
            }
        file = self.create_element("FILE", attrs=attrs)
        return file


    def data_block_xml(self, sample: "Sample") -> minidom.Element:
        dblock = self.create_element("DATA_BLOCK")
        files = self.create_element("FILES")
        for seqfile in sample.load_read_files():
            files.appendChild(self.file_xml(seqfile))
        dblock.appendChild(files)
        return dblock


    def run_xml(self, sample: "Sample") -> minidom.Element:
        run = self.create_element("RUN", attrs={"alias": "sample.run_name"})
        exp = self.create_element("EXPERIMENT_REF",
            attrs={"refname":
                   sample.get_attribute_value("ena_experiment_name")})
        run.appendChild(exp)
        run.appendChild(self.data_block_xml(sample))
        return run


    def add_sample(self, sample: "Sample") -> None:
        run_xml = self.run_xml(sample)
        self.append_element(run_xml)
