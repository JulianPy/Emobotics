from flask import Blueprint, render_template

view = Blueprint('view', __name__)


@view.route('/')
def home():
    #return "<h1>Pagina principal (Bienvenida)</h1>"
    return render_template("principal.html")
