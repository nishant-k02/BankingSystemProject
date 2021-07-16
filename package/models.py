from package import db


class Customer(db.Model):
    Sr_no = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=30), nullable=False, )
    Email_Id = db.Column(db.String(length=30), nullable=False, unique=True)
    Account_Number = db.Column(db.Integer(), nullable=False, unique=True)
    Balance = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.Sr_no'))

    def __repr__(self):
        return f'Customer {self.Name}'
