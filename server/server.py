from flask import Flask, send_from_directory, render_template, jsonify
from time import sleep
import threading
import os
import Adafruit_DHT as dht

#Set DATA pin
DHT = 4


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data')
def get_weather_data():
    return_data = {'Temperature': data._temperature, 'Humidity': data._humidity}
    return jsonify(return_data)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def collect_data(data):
    while True:
        h, t = dht.read_retry(dht.DHT22, DHT)
        #if h is not None and t is not None:
            #print("Temp={0:0.1f}*C  h={1:0.1f}%".format(t, h))
        #else:
            #print("Failed to retrieve data from humidity sensor")
        data._temperature = '{0:0.1f}*C'.format(t)
        data._humidity = '{0:0.1f}%'.format(h)
        sleep(5)


class Data:
    def __init__(self, _temperature, _humidity):
        self._temperature = _temperature
        self._humidity = _humidity


data = Data(0, 0)


if __name__ == "__main__":
    thread = threading.Thread(target=collect_data, args=(data,))
    thread.start()
    app.run(host='0.0.0.0', port=80)

