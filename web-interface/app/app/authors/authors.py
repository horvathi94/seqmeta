from dataclasses import dataclass
from seqmeta.page import Page


@dataclass
class Authors(Page):

    def render_content(self) -> "html":
        return "List authors"
