from .seqfile_new import SeqFile
from .types import SeqFileTypes
from application.src.samples.samples import Samples


class SeqFilesBunch:

    def __init__(self, sample_id: int):
        self.sample_id = sample_id;
        self.sample = Samples.fetch("view_samples_base", self.sample_id);
        self.consensus_file = SeqFile(SeqFileTypes.CONSENSUS, sample_id);
        self.contigs_file = SeqFile(SeqFileTypes.CONTIGS, sample_id);
        self.scaffolds_file = SeqFile(SeqFileTypes.SCAFFOLDS, sample_id);


    def get_list_display(self) -> dict:
        disp = {};
        disp["consensus"] = self.consensus_file.get_list_display();
        return disp;


    def get_details_display(self) -> dict:
        disp = {};
        disp["consensus"]  = self.consensus_file.get_details_display();
        disp["contigs"]  = self.contigs_file.get_details_display();
        disp["scaffolds"]  = self.scaffolds_file.get_details_display();
        return disp;


    def write_tempfiles_gisaid(self, out_file) -> None:
        if not self.consensus_file.check_exists():
            raise Exception("Consensus file not found for GISAID upload.");
        self.consensus_file.reformat_gisaid(out_file,
                                            self.sample["gisaid_virusname"]);


    def get_consensus_sequence(self) -> str:
        virusname = self.sample["gisaid_virusname"];
        return self.consensus_file.get_sequence(id=virusname);


    def get_display_sequence(self) -> str:
        virusname = self.sample["gisaid_virusname"];
        return self.consensus_file.get_display_sequence(virusname);

