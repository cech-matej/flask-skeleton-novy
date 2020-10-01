"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import LogUserForm, secti, masoform, ocform
from ..data.database import db
from ..data.models import LogUser, Stock
from math import pow
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/ocformular', methods=['GET','POST'])
def ocapp():
    form = ocform()
    if form.validate_on_submit():
        if form.obrazec.data=="1":
            prom=str(pow(form.a.data, 2))
            return  render_template("public/ocvystup.tmpl", prom=prom)
    return render_template("public/ocformular.tmpl", form=form)

@blueprint.route('/simple_chart')
def chart():
    legend = 'Monthly data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('public/graf.tmpl', legend=legend, labels=labels, values=values)

@blueprint.route('/vloz_radek')
def vloz_radek():
    text = "asdfsdfgd"
    Stock.create(firma='Autocont', firma_zkratka='xxx',\
                        jmenovita_hodnota=100, posledni_cena=101)
    return 'OK'

@blueprint.route('/vypis_table')
def vypis_table():
    pole=Stock.vypis_spolecny_radek()
    return render_template('public/vypis_tabulky.tmpl', pole=pole)
