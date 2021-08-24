from flask import render_template
from application.src.pages.page import Page
from . import basic_options as bopt
from . import virusname_templates as vnt


class MiscEditor(Page):

    styles = [{"filename": "info.css"},
              {"filename": "misc.css", "prefix": "misc"}];
    scripts = [{"filename": "add_hosts.js", "prefix":"misc"}];


    @classmethod
    def render_page(cls) -> "HTML":
        html = bopt.HostsEditor.render();
        html+= bopt.AssemblyMethodsEditor.render();
        html+= bopt.SamplingStrategiesEditor.render();
        html+= bopt.SpecimenSourcesEditor.render();
        html+= bopt.CollectionDevicesEditor.render();
        html+= bopt.HostAnatomicalMaterialsEditor.render();
        html+= bopt.HostBodyProductsEditor.render();
        html+= bopt.PurposesOfSamplingEditor.render();
        html+= bopt.PurposesOfSequencingEditor.render();
        html+= vnt.GisaidVirusnameEditor.render();
        html+= vnt.EnaVirusnameEditor.render();
        return html;

