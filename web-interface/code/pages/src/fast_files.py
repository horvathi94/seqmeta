import os
from Bio import SeqIO

class FastFile:

    main_dir = "/samples";

    def __init__(self, sample_name):

        self.sample_name = sample_name;


    def get_filenames(self):

        filenames = [];

        for ext in self.extensions:
            file_name = self.sample_name + "." + ext;
            the_file = os.path.join(self.main_dir, self.path, file_name);
            if os.path.isfile(the_file): filenames.append(file_name);

        return filenames;



class Fasta(FastFile):

    extensions = ["fasta", "fa"];
    path = "fasta";

    def __init__(self, sample_name):

        super().__init__(sample_name);
        self.has_fasta = False;
        self.fasta_filename = "";
        self.check_fasta_file();


    def check_fasta_file(self):

        files = self.get_filenames();
        if len(files) == 1:
            self.has_fasta = True;
            self.fasta_filename = files[0];
        else:
            self.has_fasta = False;
            self.fasta_filename = "";


    def get_fasta_file(self):

        if self.has_fasta:
            return os.path.join(self.main_dir, self.path, self.fasta_filename);
        return None;


    def read_fasta(self):

        sequences = [];
        if not self.has_fasta:
            return sequences;

        for req in SeqIO.parse(self.get_fasta_file(), "fasta"):
            sequences.append(req);

        return sequences;



if __name__ == "__main__":

    test = Fasta("412332");
    test.read_fasta();

    print(test.sequence)
