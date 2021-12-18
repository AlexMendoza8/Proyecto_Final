from app.db import db, BaseModelMixin


class Appointment(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    apnt_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, phone_number, lastname, email, apnt_date):
        self.name = name
        self.phone_number = phone_number
        self.lastname = lastname
        self.email = email
        self.apnt_date = apnt_date

    def __repr__(self):
        return f'Appointment({self.name})'
    def __str__(self):
        return f'{self.name}'
