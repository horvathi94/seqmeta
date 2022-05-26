import os
import subprocess
from typing import List
from .ena.submission import SubmissionXML
from .ena.sample_set import SampleSetXML


def get_webin_login():
    login = {"user": None, "pass": None}
    if "WEBIN_CLI_USER" in os.environ:
        login["user"] = os.environ["WEBIN_CLI_USER"]
    if "WEBIN_CLI_PASSWORD" in os.environ:
        login["pass"] = os.environ["WEBIN_CLI_PASSWORD"]
    return login



import requests
def submit(submission_file, samples_file, mode="test") -> str:
    login = get_webin_login()

    url = "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
    if mode == "test":
        url = "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"


    submission_xml = open(submission_file, "rb")
    samples_xml = open(samples_file, "rb")

    files = {
        "SUBMISSION": submission_xml,
        "SAMPLE": samples_xml,
    }

    result = requests.post(url,
                           files=files,
                           auth=(login["user"], login["pass"]))

    print(f"\n\nRaw: {result.__dict__}")
    return result



def samples(samples: List["Sample"]):

    sub_xml = SubmissionXML(action="VALIDATE")
    sub_xml.write()

    sample_set_xml = SampleSetXML()
    for s in samples:
        sample_set_xml.add_sample(s)
    sample_set_xml.write()

    result = submit(sub_xml.file, sample_set_xml.file, mode="test")
    return result.content
