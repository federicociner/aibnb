import math
from flask import Blueprint, render_template, session, request, jsonify

from rest.views.search import listing_service

listing = Blueprint('listing', __name__)


@listing.route('listing', methods=["GET"])
def index():
    return "listing"

@listing.route('getListings')
def get_listings():
    print('yes')
    country = request.args.get('country')
    state = request.args.get('state')
    neighborhood = request.args.get('neighborhood')
    page = request.args.get('page')
    count = request.args.get('count')
    start_at = request.args.get('start_at')
    end_at = request.args.get('end_at')
    listing_id = request.args.get('listing_id')

    results, row_count = listing_service.search(country, neighborhood, page, count, start_at, end_at, listing_id)
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
@listing.route('getAllStates')
def get_states():
    country = request.args.get('country')
    results, row_count = listing_service.getStates(country)

    return jsonify(data=results)

@listing.route('getAllNeighborhoods')
def get_neighborhoods():
    print('yes')
    state = request.args.get('state')
    results, row_count = listing_service.getNeighborhoods(state)

    return jsonify(data=results)

@listing.route('getListingsById')
def get_listings_by_id():
    listing_id = request.args.get('listing_id')
    results, row_count = listing_service.getListingById(listing_id)
    return jsonify(data=results)

@listing.route('getAllListings')
def get_all_listings():
    country = request.args.get('country')
    state = request.args.get('state')
    neighborhood = request.args.get('neighborhood')
    baths = request.args.get('baths')
    beds = request.args.get('beds')
    date = request.args.get('date')

    results, row_count = listing_service.getAllListings(country, state, neighborhood, beds, baths, date)
    return jsonify(data=results)

