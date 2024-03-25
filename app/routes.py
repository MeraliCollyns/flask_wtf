from flask import render_template, redirect, url_for
from app import app, db
from app.forms import DocumentForm
from app.models import OrganizationCell, Document


# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method=='POST':
#         # Handle POST Request here
#         return render_template('index.html')
#     return render_template('index.html')


@app.route("/", methods=["GET", "POST"])
def index():
    form = DocumentForm()
    form.komorka_organizacyjna.choices = [
        (cell.id, cell.nazwa_komorki) for cell in OrganizationCell.query.all()
    ]
    if form.validate_on_submit():
        document = Document(
            id=form.numer_dokumentu.data,
            nazwa_dokumentu=form.nazwa_dokumentu.data,
            id_komorki_organizacyjnej=form.komorka_organizacyjna.data,
        )
        db.session.add(document)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("index.html", form=form)
