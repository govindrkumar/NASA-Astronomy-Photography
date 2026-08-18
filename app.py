from flask import Flask
from flask import render_template
import requests as rq
from datetime import datetime, timedelta
from functionstex import connection, calculatedate
app = Flask(__name__)


# calculating date timeline to make sure it doesnt generate 20 random pieces of dictionary data
api_key = os.environ.get("api_key")
startdate, enddate = calculatedate()

siteconnection = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={startdate}&end_date={enddate}"
response = rq.get(siteconnection)

photos = response.json()


@app.route('/')
def get_space_data():

    startdate, enddate = calculatedate()
    api_key = os.environ.get("api_key")
    api_site = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={startdate}&end_date={enddate}"

    nasadata = connection(api_site)
    return render_template('index.html', photos=nasadata[:20])


@app.route('/photo/<int:photo_id>')
def clickdata(photo_id):
    selec_photo = photos[photo_id]
    return render_template('photoexpl.html', photo=selec_photo)
