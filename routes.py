import os
from App import db
from App import app,bcrypt
from flask import render_template, request, redirect, url_for, flash
from models import Food, User
from flask_login import login_user, current_user, logout_user, login_required
from forms import LoginForm
from werkzeug.urls import url_parse

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


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/user")
    form = LoginForm()
    if form.validate_on_submit():
        # Kiem tra user co trong db hay khong
        # Thong tin user lay tu form: form.username.data
        user = User.query.filter_by(username=form.username.data).first()
        # user ton tai
        if user is not None:
            # Kiem tra password co khop không
            password_ok =bcrypt.check_password_hash(user.password ,form.password.data) 
        # user khong ton tai
        if user is None or not password_ok:
            flash("Invalid username or password")
            return redirect("/login")

        flash("Login of user {}".format(form.username.data))
        # su dung flask_login (login_user)
        login_user(user)
        # Xu ly next
        next_page = request.args.get("next")
        if next_page is not None:
            flash("Next page {}".format(next_page))
            if url_parse(next_page).netloc != "":
                flash("netloc: " + url_parse(next_page).netloc)
                next_page = "/user"
        else:
            next_page = "/user"
        return redirect(next_page)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")


# User-------------------------------
@app.route("/user", methods=["GET"])
def viewUser():
    if current_user.is_anonymous:
        return redirect("/login")
    data_user = User.query.all()
    data_food = Food.query.all()
    if current_user.role == 0:
        return render_template("qlfood.html", data=data_food)
    else:
        return render_template("qluser.html", data=data_user)


@app.route("/insertUser", methods=["POST"])
def insertUser():
    
    if request.method == "POST":
        
        username = request.form["username"]
        data= User.query.filter_by(username=username).first()
        if data is None:
            password = request.form["password"]
            role = request.form["role"]

            my_data = User(username, password, role)
            db.session.add(my_data)
            db.session.commit()

            flash("Employee Inserted Successfully")
            return redirect(url_for("viewUser"))
        else:
            flash("User is empty")
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
@app.route("/food", methods=["GET"])
def viewFood():
    if current_user.is_anonymous:
        return redirect("/login")
    data_user = Food.query.filter_by(category="food").all()
    return render_template("qlfood.html", data=data_user)


@app.route("/insertFood", methods=["POST"])
def insertFood():

    if request.method == "POST":

        foodname = request.form["foodname"]
        price = request.form["price"]
        description = request.form["description"]
        category = request.form["category"]

        # image ===============================================================
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        image = os.path.splitext(uploaded_file.filename)[0] + ""
        my_data = Food(foodname, price, description, image, category)
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

        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        my_data.image = os.path.splitext(uploaded_file.filename)[0] + ""

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
@app.route("/drink", methods=["GET"])
def viewDrink():
    if current_user.is_anonymous:
        return redirect("/login")
    data_user = Food.query.filter_by(category="drink").all()
    return render_template("qldrink.html", data=data_user)


@app.route("/insertDrink", methods=["POST"])
def insertDrink():

    if request.method == "POST":
        foodname = request.form["foodname"]
        price = request.form["price"]
        description = request.form["description"]
        category = request.form["category"]

        # image ===============================================================
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        image = os.path.splitext(uploaded_file.filename)[0] + ""
        my_data = Food(foodname, price, description, image, category)
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

        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        my_data.image = os.path.splitext(uploaded_file.filename)[0] + ""

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
