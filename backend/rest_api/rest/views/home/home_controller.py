from flask import Blueprint, render_template, session, request

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static_home'
)


@home.route('/')
def index():

    return render_template('index.html')


@home.route('/search?country=<string:country_name>', methods=["GET"])
def search(country_name):
    return '{"result": "wooooooooo"}'





