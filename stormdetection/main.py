import simplekml
from flask import Flask, request,jsonify
from boto import connect_s3
import random
import json
app = Flask(__name__)


@app.route('/')
def root_path():
    kml = simplekml.Kml()
#parse the incomming json element and pass them in place of coords below
   # jsondata = json.load(urllib2.urlopen('url'))

    #print(jsondata[#coordinates])
    kml.newpoint(name="StationName", coords=[(18.432314, -33.988862)])  # lon, lat, optional height
    print(kml.kml())
    s3conn = connect_s3(anon=True)
    bucket = s3conn.get_bucket('noaa-nexrad-level2', validate=False)
    return kml.savekmz("file.kml")




if __name__ == '__main__':
    app.run(debug=True)