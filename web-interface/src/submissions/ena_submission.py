import os
import requests
import subprocess
from typing import List
from .ena.submission import SubmissionXML
from .ena.sample_set import SampleSetXML
from .ena.experiment import ExperimentSetXML
from .ena.run import RunSetXML
from .ena.xml import XML
from .ena.receipt import ReceiptXML


# TODO: production url in get_url


class EnaSubmission:


    def __init__(self):
        self.webin_user = None
        if "WEBIN_CLI_USER" in os.environ:
            self.webin_user = os.environ["WEBIN_CLI_USER"]
        self.webin_pass = None
        if "WEBIN_CLI_PASSWORD" in os.environ:
            self.webin_pass = os.environ["WEBIN_CLI_PASSWORD"]


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


    def submit_samples(self, samples: List["Sample"]) -> ReceiptXML:
        sub_xml = SubmissionXML(action="VALIDATE")
        sub_xml.write()

        samples_xml = SampleSetXML()
        for s in samples: samples_xml.add_sample(s)
        samples_xml.write()

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


    def submit_experiments(self, samples: List["Sample"]) -> any:
        sub_xml = SubmissionXML(action="VALIDATE")
        sub_xml.write()

        experiments_xml = ExperimentSetXML()
        runs_xml = RunSetXML()
        for sample in samples:
            experiments_xml.add_sample(sample)
            runs_xml.add_sample(sample)

#        print(experiments_xml.xml_string)
        print(runs_xml.xml_string)


        return experiments_xml.xml_string
