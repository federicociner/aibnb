
from app import db





class listing(db.Model):

    """This class represents the bucketlist table."""



    __tablename__ = 'bucketlists'



    listing_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(500))

    country = db.Column(db.String(64))

    summary = db.Column(db.String(1024))

    price = db.Column(db.Integer)

    has_availability = db.Column(db.Integer)

    availability_30 = db.Column(db.Integer)

    availability_60 = db.Column(db.Integer)

    availability_90 = db.Column(db.Integer)

    availability_365 = db.Column(db.Integer)

    number_of_reviews = db.Column(db.Integer)



    def __init__(self, name):

        """initialize with name."""

        self.name = name



    def save(self):

        db.session.add(self)

        db.session.commit()


