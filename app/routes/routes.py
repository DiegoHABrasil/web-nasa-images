from flask import Blueprint, render_template, request, redirect, url_for
# from app import logger
# from app import app
import requests

bp_data = Blueprint("bp_data", __name__)

URL = "https://api.nasa.gov/planetary/apod?"
API_KEY = "api_key=dNjYpwHMsTa8sAJ5GtGrsrHDXq45zpsowTGsW6ud"

# api_key = app.config['API_KEY']

@bp_data.route("/data", methods=['GET'])
def images_data():

    data = 'asdjasd'

    data = request.form.get("data")

    return render_template("images_request.html", data=data)
    #return f"<h3>{data}</h3>"


@bp_data.route("/api-data", methods=['GET', 'POST'])
def request_api():

    search_date =  request.form.get('inDate')

    url = URL + API_KEY + "&date=" + search_date
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return render_template("images_view.html", **data)


    else:
        data = {"status": "NOK"}
        # return redirect(url_for('images_data', data=data))
        return data

    return data