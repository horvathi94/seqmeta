from seqmeta.objects.sample import Sample



class RepoSubmission:


    path = "/home/seqmeta/uploads/samples/"


    def __init__(self, template_name: str, sample_names: list):
        self.template_name = template_name
        self.sample_names = sample_names
        self.samples = [Sample.load(s, self.template_name) \
                        for s in self.sample_names]


    def generate(self) -> any:
        return
