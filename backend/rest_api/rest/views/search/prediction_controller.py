import math
from flask import Blueprint, render_template, session, request, jsonify

from rest.views.search import prediction_service

prediction = Blueprint('prediction', __name__)


@prediction.route('prediction', methods=["GET"])
def index():
    listing_id = request.args.get('listing_id')
    prediction_type = request.args.get('prediction_type')
    page = request.args.get('page')
    count = request.args.get('count')

    results, row_count = prediction_service.search(listing_id, prediction_type, page, count)
    if page is not None and count is not None:
        return jsonify(
            data=results,
            total_page_count=int(math.ceil(float(row_count)/float(count))),
            total_count=int(row_count),
            current_page=int(page)
        )
    else:
        return jsonify(
            data=results
        )
