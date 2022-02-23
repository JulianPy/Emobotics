from flask import Blueprint, render_template, request, flash

searchInfo = Blueprint('Search', __name__)


@searchInfo.route('/buscar', methods=['GET', 'POST'])
def search():
    from .model import User
    from . import db
    if request.method == 'POST':
        # Extraigo lo que hay en el campo y lo guardo en la variable entrada
        entrada = request.form['busqueda']
        #suario = request.form.get('usuario').first()
        user = User.query.filter_by(usuario=entrada)
        #print(user)
        if user:
            flash('usuario encontrado. Felicidades', category='success')
        else:
            flash('No se encontró a alguien con ese usuario', category='error')
        print(entrada)
    else:
        pass
        #usuario = request.form.get('usuario').first()
        #user = User.query.filter_by(usuario=usuario)
        #if user:
        #    flash('usuario encontrado', category='success')
        #else:
        #    flash('No se encontró a alguien con ese usuario', category='error')
    #return "<h1>Buscar un Usuario</h1>"
    return render_template("buscar.html")