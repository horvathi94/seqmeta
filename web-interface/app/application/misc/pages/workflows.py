from application.src.pages.page import Page
from flask import render_template

class WorkflowPage(Page):

    html_source = "";

    @classmethod
    def render_page(cls) -> "HTML":
        return render_template(f"workflow/{cls.html_source}");



class WorkflowBasic(WorkflowPage):

    html_source = "basic.html";



class WorkflowGISAID(WorkflowPage):

    html_source = "gisaid.html";



class WorkflowENA(WorkflowPage):

    html_source = "ena.html";



class WorkflowNCBI(WorkflowPage):

    html_source = "ncbi.html";
