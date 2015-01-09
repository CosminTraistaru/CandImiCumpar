import threading
import random
import time
import flask.ext.whooshalchemy

from app import app, db


class Categorie(db.Model):
    __tablename__ = 'categorie'
    idCategorie = db.Column(db.Integer, autoincrement=True, primary_key=True)
    NumeCategorie = db.Column(db.Text)


class Magazin(db.Model):
    __tablename__ = 'magazin'
    idMagazin = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Nume = db.Column(db.Text)
    LinkMagazin = db.Column(db.Text)
    Descriere = db.Column(db.Text)

    def __repr__(self):
        return "{magazin} ".format(magazin=self.Nume.title())


class Pret(db.Model):
    __tablename__ = 'pret'
    idProdus = db.Column(db.VARCHAR(40),
                         db.ForeignKey('produs.idProdus'))
    Pret = db.Column(db.DECIMAL(10, 4))
    Data = db.Column(db.Date, primary_key=True)

    def __repr__(self):
        return "{} {}".format(int(self.Pret), self.Data)


class Produs(db.Model):
    __searchable__ = ['NumeProdus']
    __tablename__ = 'produs'

    idProdus = db.Column(db.VARCHAR(40), primary_key=True)
    idCategorie = db.Column(db.Integer, default=0)
    idMagazin = db.Column(db.Integer, db.ForeignKey('magazin.idMagazin'))
    Magazin = db.relationship('Magazin', backref="produs")
    NumeProdus = db.Column(db.Text)
    LinkProdus = db.Column(db.Text)
    PozaProdus = db.Column(db.Text)
    # hash = db.Column(db.VARCHAR(40))
    Preturi = db.relationship('Pret', backref="produs", lazy='dynamic')

    def __str__(self):
        return "Produs: {nume_produs} \nLink Produs: {link_produs}".\
            format(nume_produs=self.NumeProdus, link_produs=self.LinkProdus)

    def preturi_dict(self):
        return [
            {'day': p.Data.strftime("%Y-%m-%d"),
             'value': int(p.Pret)}
            for p in self.Preturi.all()
        ]


def get_product_info(id_prod):
    produs = {}
    pr = Produs().query.get(id_prod)
    # import ipdb;ipdb.set_trace()
    produs['preturi'] = pr.preturi_dict()
    produs['nume'] = pr.NumeProdus
    produs['link'] = pr.LinkProdus
    produs['image'] = pr.PozaProdus
    produs['magazin'] = pr.Magazin
    return produs


