from application.src.pages.page import Page
from .misc_options import hosts, assembly_methods, sampling_strategies, \
    specimen_sources, collection_devices, anatomical_materials, body_products,\
    purposes_sampling, purposes_sequencing
from . import virusname_templates as vnt


class MiscEditor(Page):

    styles = [{"filename": "info.css"},
              {"filename": "misc.css", "prefix": "misc"}];
    scripts = [{"filename": "add_hosts.js", "prefix":"misc"}];


    @classmethod
    def render_page(cls) -> "HTML":
        html = hosts.Editor.render();
        html+= assembly_methods.Editor.render();
        html+= sampling_strategies.Editor.render();
        html+= specimen_sources.Editor.render();
        html+= collection_devices.Editor.render();
        html+= anatomical_materials.Editor.render();
        html+= body_products.Editor.render();
        html+= purposes_sampling.Editor.render();
        html+= purposes_sequencing.Editor.render();
        html+= vnt.GisaidVirusnameEditor.render();
        html+= vnt.EnaVirusnameEditor.render();
        return html;

