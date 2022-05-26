from datetime import datetime
from .xml import XML
from xml.dom import Node


class ReceiptXML(XML):


    def __init__(self, fname: str="receipt", create: bool=True):
        super().__init__(root="RECEIPT", fname=fname, create=create)


    @property
    def receipt_tag(self) -> "minidom.Element":
        return self.root.getElementsByTagName("RECEIPT")[0]


    def get_date(self) -> datetime:
        date = self.receipt_tag.getAttribute("receiptDate")
        return datetime.fromisoformat(date)


    def get_success(self) -> bool:
        if self.receipt_tag.getAttribute("success") == "true": return True
        return False


    def get_samples(self) -> list:
        samples = []
        nodes = self.root.getElementsByTagName("SAMPLE")
        for n in nodes:
            ext = n.getElementsByTagName("EXT_ID")[0]
            sample = {
                "accession": n.getAttribute("accession"),
                "alias": n.getAttribute("alias"),
                "status": n.getAttribute("status"),
                "biosample": ext.getAttribute("accession")
            }
            samples.append(sample)
        return samples


    def get_messages(self) -> list:
        nodes = self.root.getElementsByTagName("MESSAGES")[0]
        messages = []
        for m in nodes.childNodes:
            if m.nodeType is not Node.ELEMENT_NODE:
                continue
            msg = {
                "type": m.tagName,
                "content": m.firstChild.nodeValue
            }
            messages.append(msg)
        return messages
