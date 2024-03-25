from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Formularz WTForms
class DocumentForm(FlaskForm):
    numer_dokumentu = IntegerField('Numer Dokumentu')
    nazwa_dokumentu = StringField('Nazwa Dokumentu')
    komorka_organizacyjna = SelectField('Komórka Organizacyjna', coerce=int)
    submit_button = SubmitField('Zapisz')