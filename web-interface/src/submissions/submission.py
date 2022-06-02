from .gisaid import GisaidSubmission
from .ena import EnaSubmission


def Factory(repo: str, template_name: str, snames: list) -> "RepoSubmission":

    repo_subs = {
        "gisaid": GisaidSubmission,
        "ena": EnaSubmission,
    }

    repo_sub = repo_subs[repo]
    return repo_sub(template_name, snames)
