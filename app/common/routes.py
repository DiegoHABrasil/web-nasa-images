from flask import Blueprint, render_template

import requests
bp_data = Blueprint("bp_data", __name__)

URL = "https://api.nasa.gov/planetary/apod?"
API_KEY = "api_key=dNjYpwHMsTa8sAJ5GtGrsrHDXq45zpsowTGsW6ud"

@bp_data.route("/data")
def data():

    return render_template("data.html", data=data)
    #return f"<h3>{data}</h3>"

def request_api(date):

    url = URL + API_KEY + date
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data

    else:
        data = {"status": "erro"}

