import os
from flask import Blueprint, send_from_directory
from .pages.home import Home


home_bp = Blueprint("home_bp", __name__,
                    template_folder="templates",
                    static_folder="static")



@home_bp.route("/", methods=["GET"])
@home_bp.route("/index.html", methods=["GET"])
@home_bp.route("/home.html", methods=["GET"])
def home():
    return Home.render()



@home_bp.route("/favicon.ico")
def favicon():
    return send_from_directory("static/assets",
                               'favicon.ico', mimetype='image/x-icon')


from flask import jsonify
from application.src.seqfiles.seqfile_new import SeqFile
from application.src.seqfiles.seqfile_bunch_new import SeqFilesBunch
from application.src.seqfiles.types import SeqFileTypes
@home_bp.route("/test")
def tester():
#    seqfile = SeqFile(SeqFileTypes.CONSENSUS, 1)
#    test = seqfile.get_filename()

    bunch = SeqFilesBunch(1)
    test = bunch.consensus_file
    test = bunch.contigs_file

    return str(test)
    return jsonify(test)


