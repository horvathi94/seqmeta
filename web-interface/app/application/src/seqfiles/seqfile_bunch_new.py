from .seqfile_new import SeqFile
from .types import SeqFileTypes


class SeqFilesBunch:

    def __init__(self, sample_id: int):
        self.sample_id = sample_id;
        self.consensus_file = SeqFile(SeqFileTypes.CONSENSUS, sample_id);
        self.contigs_file = SeqFile(SeqFileTypes.CONTIGS, sample_id);
        self.scaffolds_file = SeqFile(SeqFileTypes.SCAFFOLDS, sample_id);


    def get_list_display(self):
        disp = {};
        disp["consensus"] = self.consensus_file.get_list_display();
        return disp;


    def get_details_display(self):
        disp = {};
        disp["consensus"]  = self.consensus_file.get_details_display();
        disp["contigs"]  = self.contigs_file.get_details_display();
        disp["scaffolds"]  = self.scaffolds_file.get_details_display();
        return disp;
