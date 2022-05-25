import os
import subprocess
from typing import List
from seqmeta.objects.sample import Sample
from seqmeta.submissions import ena_meta as ena_metadata
from seqmeta.submissions import gisaid as gisaid_metadata



def gisaid(template_name: str, sample_names: List[str]) -> dict:
    samples = [Sample.load(name, template_name) for name in sample_names]
    md = gisaid_metadata.Metadata()
    md.add_samples(samples)
    md.write()
    return [s.asjson() for s in samples]


def ena(template_name: str, sample_names: List[str]) -> str:
    samples = [Sample.load(name, template_name) for name in sample_names]
    md = ena_metadata.Metadata()
    md.add_samples(samples)
    md.write()
    return md.xml


from seqmeta.submissions import ena_submission
def submit_to_ena(template_name: str, sample_names: List[str]) -> any:
    samples = [Sample.load(name, template_name) for name in sample_names]
    result = ena_submission.samples(samples)
    return result
#    result = subprocess.run(
#        ["java", "-jar", "/opt/webin-cli/webin-cli-4.4.0.jar", "-help"],
#        capture_output=True, text=True)
#    print(f"\n\nResult: {result}")

