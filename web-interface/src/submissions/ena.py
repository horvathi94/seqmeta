import os
from .repo_sub import RepoSubmission
from .ena_xmls.receipt import ReceiptXML
from .ena_xmls.submission import SubmissionXML
from .ena_xmls.sample_set import SampleSetXML
from .ena_xmls.experiment_set import ExperimentSetXML
from .ena_xmls.run_set import RunSetXML


class EnaSubmission(RepoSubmission):


    @property
    def webin_user(self) -> str:
        return os.environ["WEBIN_CLI_USER"]


    @property
    def webin_pass(self) -> str:
        return os.environ["WEBIN_CLI_PASSWORD"]


    def get_url(self, mode: str="test") -> str:
        if mode == "test":
            return "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
        return "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"


    def submit(self, files: dict, mode: str="test") -> ReceiptXML:
        result = requests.post(self.get_url(mode=mode), files=files,
                               auth=(self.webin_user, self.webin_pass))

        if result.status_code != 200:
            raise Exception(f"Failed: status code {result.status_code}")

        receipt = ReceiptXML(create=False)
        receipt.xml_string = result.content
        return receipt


    def submit_samples(self) -> ReceiptXML:
        sub_xml = SubmissionXML(action="VALIDATE")
        sub_xml.write()

        samples_xml = SampleSetXML()
        for s in self.samples:
            samples_xml.add_sample(s)
        samples_xml.write()
        print(samples_xml.xml_string)
        return samples_xml

        sub_file = open(sub_xml.file, "r")
        samples_file = open(samples_xml.file, "r")

        files = {
            "SUBMISSION": sub_file,
            "SAMPLE": samples_file,
        }

        try:
            receipt = self.submit(files=files, mode="test")
        except Exception as e:
            raise e
        finally:
            sub_file.close()
            samples_file.close()

        return receipt



    def submit_experiments(self) -> ReceiptXML:
        sub_xml = SubmissionXML(action="VALIDATE")
        sub_xml.write()

        experiments_xml = ExperimentSetXML()
        runs_xml = RunSetXML()
        for sample in self.samples:
            experiments_xml.add_sample(sample)
            runs_xml.add_sample(sample)

        print(experiments_xml.xml_string)
#        print(runs_xml.xml_string)


    def generate(self) -> any:
        #self.submit_samples()
        self.submit_experiments()

