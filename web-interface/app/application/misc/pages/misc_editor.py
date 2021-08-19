from flask import render_template
from . import basic_options as bopt
from . import virusname_templates as vnt


class MiscEditor:

    styles = [{"filename": "info.css"},
              {"filename": "misc.css", "prefix": "misc"}];
    scripts = [{"filename": "add_hosts.js", "prefix":"misc"}];


    @classmethod
    def show(cls) -> "HTML":
        """Returns the misc editor pages."""

        html = render_template("head.html", styles=cls.styles);
        html+= bopt.HostsEditor.render();
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
        html+= render_template("footer.html", scripts=cls.scripts);
        return html;

