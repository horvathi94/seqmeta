from flask import render_template

class WorkflowPage:

    html_source = "";

    @classmethod
    def show(cls) -> "HTML":
        """Returns HTML page with workflow."""
        html = render_template("head.html");
        html+= render_template(f"workflow/{cls.html_source}");
        html+= render_template("footer.html");
        return html



class WorkflowBasic(WorkflowPage):

    html_source = "basic.html";



class WorkflowGISAID(WorkflowPage):

    html_source = "gisaid.html";



class WorkflowENA(WorkflowPage):

    html_source = "ena.html";



class WorkflowNCBI(WorkflowPage):

    html_source = "ncbi.html";
