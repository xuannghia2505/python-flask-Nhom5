from App import db, login , bcrypt
from flask_login import UserMixin

#Creating model table for our CRUD database
class Food(db.Model):
    foodid = db.Column(db.Integer, primary_key=True)
    foodname = db.Column(db.String(100))
    price = db.Column(db.String(100))
    description = db.Column(db.String(500))
    image = db.Column(db.String(100))
    category = db.Column(db.String(100))

    def __init__(self, foodname, price, description, image, category):
        self.foodname = foodname
        self.price = price
        self.description = description
        self.image = image
        self.category = category

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role = db.Column(db.Integer)
    
    def get_id(self):
        return self.id
    def is_active(self): 
        return True
    def __init__(self, username, password, role):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.role = role

@login.user_loader
def load_user(id):
    return User.query.get(int(id))