from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Predio import Predio
from utils.db import db

predios = Blueprint("predios", __name__)


@predios.route('/')
def index():
    predios = Predio.query.all()
    return render_template('index.html', predios = predios)


@predios.route('/new', methods=['POST'])
def add_predio():
    if request.method == 'POST':

        # receive data from the form
    
        nombrePropietario = request.form['nombrePropietario']
        direccionPredio = request.form['direccionPredio']
        areaPredio = request.form['areaPredio']
        tipoSuelo = request.form['tipoSuelo']
        valorPredio = request.form['valorPredio']
        distrito = request.form['distrito']

        # create a new Predio object
        new_predio = Predio(nombrePropietario, direccionPredio, areaPredio, tipoSuelo, valorPredio, distrito)

        # save the object into the database
        db.session.add(new_predio)
        db.session.commit()

        flash('Predio added successfully!')

        return redirect(url_for('predios.index'))


@predios.route("/update/<string:idPredio>", methods=["GET", "POST"])
def update(idPredio):
    # get predio by Id
    print(idPredio)
    predio = Predio.query.get(idPredio)

    if request.method == "POST":
        predio.nombrePropietario = request.form['nombrePropietario']
        predio.direccionPredio = request.form['direccionPredio']
        predio.areaPredio = request.form['areaPredio']
        predio.tipoSuelo = request.form['tipoSuelo']
        predio.valorPredio = request.form['valorPredio']
        predio.distrito = request.form['distrito']

        db.session.commit()

        flash('Predio updated successfully!')

        return redirect(url_for('predios.index'))

    return render_template("update.html", predio=predio)


@predios.route("/delete/<idPredio>", methods=["GET"])
def delete(idPredio):
    predio = Predio.query.get(idPredio)
    db.session.delete(predio)
    db.session.commit()

    flash('Predio deleted successfully!')

    return redirect(url_for('predios.index'))


@predios.route("/about")
def about():
    return render_template("about.html")
