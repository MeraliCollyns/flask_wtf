from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
# testy
class Document(db.Model):
    __tablename__ = 'Document'

    id = db.Column(db.Integer, primary_key=True)
    nazwa_dokumentu = db.Column(db.String(100))
    id_komorki_organizacyjnej = db.Column(db.Integer, db.ForeignKey('OrganizationCell.id'))

# Model dla tabeli słownikowej
class OrganizationCell(db.Model):
    __tablename__ = 'OrganizationCell'
    id = db.Column(db.Integer, primary_key=True)
    nazwa_komorki = db.Column(db.String(100))

