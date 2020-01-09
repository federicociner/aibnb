from flask import Flask, request, render_template, jsonify
from rest.error_handler import ErrorHandler
from rest.views.home.home_controller import home
from rest.views.search.listing_controller import listing
from rest.views.search.address_controller import address
from rest.views.search.prediction_controller import prediction
# from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'k234j2lkj34k23k3lkkjj32kll3'
app.config['SESSION_TYPE'] = 'filesystem'
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(listing, url_prefix='/listing/')
app.register_blueprint(address, url_prefix='/address/')
app.register_blueprint(prediction, url_prefix='/prediction/')

app.debug = True
# cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(ErrorHandler)
def handle_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
