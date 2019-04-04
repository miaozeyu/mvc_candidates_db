from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from math import ceil
import hashlib
import json

from data_provider_service import DataProviderService

db_engine = 'mysql+mysqldb://root:@localhost/hrdb'

PAGE_SIZE = 2

DATA_PROVIDER = DataProviderService(db_engine)

def candidate(serialize = True):
    candidates = DATA_PROVIDER.get_candidate(serialize=serialize)
    # page starts at 1
    page = request.args.get("page")

    if page:
        nr_of_pages = int(ceil(float(len(candidates)) / PAGE_SIZE))
        converted_page = int(page)
        if converted_page > nr_of_pages or converted_page <= 0:
                return make_response("", 404)

        from_idx = converted_page * PAGE_SIZE - 2   # page=1 from_idx=0; page=2 from_idx=2; page=3 from_idx=4
        stop_idx = from_idx + PAGE_SIZE             # page=1 stop_idx=2; page=2 stop_idx=4; page=3 stop_idx=6

        candidates = candidates[from_idx:stop_idx]

    if serialize:
        data = {"candidates": candidates, "total": len(candidates)}
        json_data = json.dumps(data)
        response = make_response(jsonify(data), 200)
        response.headers["ETag"] = str(hashlib.sha256(json_data.encode('utf-8')).hexdigest())
        response.headers["Cache-Control"] = "private, max - age=300"
        return response
    else:
        return candidates


def candidate_by_id(id):
    current_candidate = DATA_PROVIDER.get_candidate(id, serialize=True)
    if current_candidate:
        return jsonify({"candidate": current_candidate})
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)

def initialize_database():
    DATA_PROVIDER.init_database()


def fill_database():
    DATA_PROVIDER.fill_database()


def delete_candidate(id):
    if DATA_PROVIDER.delete_candidate(id):
        return make_response('', 204)
    else:
        return make_response('', 404)

def add_candidate():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    new_candidate_id = DATA_PROVIDER.add_candidate(first_name=first_name,
                                                   last_name=last_name,
                                                   email=email,
                                                   phone=phone)

    return jsonify({
        "id": new_candidate_id,
        "url": url_for("candidate_by_id", id=new_candidate_id)
    })


def update_candidate(id):
    new_candidate = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "phone": request.form["phone"]
    }
    updated_candidate = DATA_PROVIDER.update_candidate(id, new_candidate)
    if not update_candidate:
        return make_response('', 204)
    else:
        return jsonify({"candidate": updated_candidate})


def build_message(key, message):
    return {key:message}

























