from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Float)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    weight = db.Column(db.Float)

class CustomerDemand(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    demand = db.Column(db.Integer)

class TimeWindow(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    day = db.Column(db.String(10), primary_key=True)
    start_hour = db.Column(db.Integer)
    end_hour = db.Column(db.Integer)

class Distance(db.Model):
    from_id = db.Column(db.Integer, primary_key=True)
    to_id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float)
    travel_time = db.Column(db.Float)

class Deadline(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    deadline = db.Column(db.String(25))
