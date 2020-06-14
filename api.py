from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1)

@app.route("/hue")
def hue():
	hue = request.args.get('hue', default = 0, type = int)
	bus.write_byte(addr,hue)
	return "set hue to " + str(hue)

if __name__ == '__main__':
    app.run(debug=True)
