from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.urls import url_parse
from pathlib import Path
import os

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Sign in")
    recaptcha = RecaptchaField()

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeckacdAAAAAHSQu1A2h2ZXnXSrcoAFwIOvyi3d'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeckacdAAAAADOPi7qaBle16terydNyysELh9E1'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Nghiaoi123@localhost/qlloteria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
UPLOAD_FOLDER = 'static/images'


#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

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
        self.password = password
        self.role = role

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/")
@app.route("/menu", methods=['GET','POST'])
def Index():
    if request.method == "POST":
        key = request.form["key"]
        data = Food.query.filter(Food.foodname.like('%'+key+'%')).all()    
    else:
        data = Food.query.all()
    if len(data)<1:
        flash('No result')
    return render_template("menu.html", data = data)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/user')
    role = -1
    form = LoginForm()
    if form.validate_on_submit():
        # Kiem tra user co trong db hay khong
        # Thong tin user lay tu form: form.username.data
        user = User.query.filter_by(username=form.username.data).first()
        # user ton tai
        if user is not None:
            #Kiem tra password co khop không 
            password_ok = user.password == form.password.data
        # user khong ton tai
        if user is None or not password_ok:
            flash('Invalid username or password')
            return redirect('/login')
        
        flash('Login of user {}'.format(form.username.data))
        #su dung flask_login (login_user)
        login_user(user)
        # Xu ly next
        next_page = request.args.get('next')
        if next_page is not None:
            flash('Next page {}'.format(next_page))
            if url_parse(next_page).netloc != '':
                flash('netloc: ' + url_parse(next_page).netloc)
                next_page = '/user'
        else:
            next_page = '/user'
        return redirect(next_page)
    return render_template('login.html', form = form, role = role )

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

# User-------------------------------
@app.route("/user", methods=['GET'])
def viewUser():
    if current_user.is_anonymous:
        return redirect('/login')
    data_user=User.query.all()
    if current_user.role == 0:
        return render_template("qlfood.html", data =data_user)
    else:
        return render_template("qluser.html", data =data_user)

@app.route("/insertUser", methods=["POST"])
def insertUser():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        my_data = User(username, password, role)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for("viewUser"))


@app.route("/updateUser", methods=["GET", "POST"])
def updateUser():

    if request.method == "POST":
        my_data = User.query.get(request.form.get("id"))

        my_data.username = request.form["username"]
        my_data.password = request.form["password"]
        my_data.role = request.form["role"]

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for("viewUser"))


@app.route("/deleteUser/<id>/", methods=["GET", "POST"])
def deleteUser(id):
    my_data = User.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for("viewUser"))

# Food ---------------------------------
@app.route("/food", methods=['GET'])
def viewFood():
    if current_user.is_anonymous:
        return redirect('/login')
    data_user=Food.query.filter_by(category='food').all()
    return render_template("qlfood.html", data =data_user)

@app.route("/insertFood", methods=["POST"])
def insertFood():

    if request.method == "POST":

        foodname = request.form["foodname"]
        price = request.form["price"]
        description = request.form["description"]
        category = request.form["category"]

         #image ===============================================================
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file.filename))
        image = os.path.splitext(uploaded_file.filename)[0]+''
        my_data = Food(foodname, price, description,image,category)
        db.session.add(my_data)
        db.session.commit()

        flash("Food Inserted Successfully")

        return redirect(url_for("viewFood"))


@app.route("/updateFood", methods=["GET", "POST"])
def updateFood():

    if request.method == "POST":
        my_data = Food.query.get(request.form.get("id"))
   
        my_data.foodname = request.form["foodname"]
        my_data.price = request.form["price"]
        my_data.description = request.form["description"]
        my_data.category = request.form["category"]

        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file.filename))
        my_data.image = os.path.splitext(uploaded_file.filename)[0]+''

        db.session.commit()

        flash("Food Inserted Successfully")

        return redirect(url_for("viewFood"))


@app.route("/deleteFood/<id>/", methods=["GET", "POST"])
def deleteFood(id):
    my_data = Food.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Food Deleted Successfully")

    return redirect(url_for("viewFood"))


# Drink --------------------------------------
@app.route("/drink", methods=['GET'])
def viewDrink():
    if current_user.is_anonymous:
        return redirect('/login')
    data_user=Food.query.filter_by(category='drink').all()
    return render_template("qldrink.html", data =data_user)

@app.route("/insertDrink", methods=["POST"])
def insertDrink():

    if request.method == "POST":

        foodname = request.form["foodname"]
        price = request.form["price"]
        description = request.form["description"]
        category = request.form["category"]

         #image ===============================================================
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file.filename))
        image = os.path.splitext(uploaded_file.filename)[0]+''
        my_data = Food(foodname, price, description,image,category)
        db.session.add(my_data)
        db.session.commit()

        flash("Drink Inserted Successfully")

        return redirect(url_for("viewDrink"))


@app.route("/updateDrink", methods=["GET", "POST"])
def updateDrink():

    if request.method == "POST":
        my_data = Food.query.get(request.form.get("id"))
   
        my_data.foodname = request.form["foodname"]
        my_data.price = request.form["price"]
        my_data.description = request.form["description"]
        my_data.category = request.form["category"]

        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file.filename))
        my_data.image = os.path.splitext(uploaded_file.filename)[0]+''

        db.session.commit()


        flash("Drink Inserted Successfully")

        return redirect(url_for("viewDrink"))


@app.route("/deleteDrink/<id>/", methods=["GET", "POST"])
def deleteDrink(id):
    my_data = Food.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Drink Deleted Successfully")

    return redirect(url_for("viewDrink"))



if __name__ == "__main__":
    app.run(debug=True)
