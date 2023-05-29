from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint('application', "views")


@views.route("/")
def home():
    return render_template("index.html", name ="TEST1")

# @views.route("/profile")
# def profile():
#     return render_template("profile.html")

# @views.route("/json")
# def get_json():
#     return jsonify({'name':'tim', 'age':10})

# @views.route("/data")
# def get_data():
#     data = request.json
#     return jsonify(data)

# @views.route("go-to-home")
# def go_to_home():
#     return redirect(url_for("views.home"))