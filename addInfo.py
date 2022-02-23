from flask import Blueprint, render_template, request, flash




addInfo = Blueprint('Add', __name__)


@addInfo.route('/ingresar', methods=['GET', 'POST'])
def add_new():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        usuario = request.form.get('usuario')
        correo = request.form.get('email')
        from .model import User
        from . import db
        if nombre == "":
            flash("Escriba nombre", category='error')
        elif apellido == "":
            flash("Escriba apellido", category='error')
        elif usuario == "":
            flash("Escriba usuario", category='error')
        elif correo == "":
            flash("Escriba correo", category='error')
        else:
            # Creamos la base de datos o en su defecto, añadimos
            # datos a a base de Datos

            nuevo_usuario = User(nombre=nombre,
                                 apellido=apellido,
                                 usuario=usuario,
                                 email=correo)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash("Usuarios agregados exitosamente", category='success')


    return render_template("registrar.html")
    #return "<h1>Ingresar nuevos Usuarios</h1>"


#@rutaIngreso.route('/ingresar2')
#def agregarInfo2():
#    return "<p>Jojo<\p>"