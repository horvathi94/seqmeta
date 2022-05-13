from .seqfiles import SeqFile
from .attributes.samplefile import SeqFileType


class SeqFileBunch:


    def __init__(self):
        _seqfiles = {sft: [] for sft in SeqFileType}


    def add_seqfile(self, seqfile: SeqFile) -> None:
        self._seqfiles[seqfile.type_].append(seqfile)


    def fetch_files(self):
        pass
