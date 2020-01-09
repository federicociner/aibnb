import math
from flask import Blueprint, render_template, session, request, jsonify

from rest.views.search import address_service

address = Blueprint('address', __name__)


@address.route('address', methods=["GET"])
def index():
    country = request.args.get('country')
    state = request.args.get('state')
    page = request.args.get('page')
    count = request.args.get('count')

    results, row_count = address_service.search(country, state, page, count)
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
