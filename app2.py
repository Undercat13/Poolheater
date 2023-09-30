import PiRelay6
import time
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO

relays = [
PiRelay6.Relay("RELAY1"),
PiRelay6.Relay("RELAY2"),
PiRelay6.Relay("RELAY3"),
PiRelay6.Relay("RELAY4"),
PiRelay6.Relay("RELAY5"),
PiRelay6.Relay("RELAY6"),
PiRelay6.Relay("RELAY7"),
PiRelay6.Relay("RELAY8"),
PiRelay6.Relay("RELAY9"),
PiRelay6.Relay("RELAY10"),
PiRelay6.Relay("RELAY11"),
PiRelay6.Relay("RELAY12")]

relay_status = [0,0,0,0,0,0,0,0,0,0,0,0,0]

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    
    print ('Client hitting the index page.')
    return render_template('index.html')

@socketio.on('toggle_relay_event', namespace='/test')
def togle_relay_event(data):
	print("TOGGLING RELAY:", data)
	if (relay_status[data] == 0):
		relays[data].on()
		relay_status[data] = 1
	else:
		relays[data].off()
		relay_status[data] = 0
if __name__ == '__main__':
	print ('>> Starting the Flask Websocket server.')
	socketio.run(app, host="0.0.0.0")
