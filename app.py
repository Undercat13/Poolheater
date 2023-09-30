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

relays_status = [0,0,0,0,0,0,0,0,0,0,0,0,0]
status = []

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def toggle_status(num):
	if(relays_status[num] == 0):
		relays_status[num] = 1
		relays[num].on()
	else:
		relays_status[num] = 0
		relays[num].off()

def relay_switch(data):
	if (data == 0):
		print("data = 1 Low")
		relays_status[1] = 0
		relays[1].off()
		relays_status[2] = 0
		relays[2].off()
		relays_status[3] = 0
		relays[3].off()
		toggle_status(data)
	elif (data == 1):
		print("data = 2 Med")
		relays_status[0] = 0
		relays[0].off()
		relays_status[2] = 0
		relays[2].off()
		relays_status[3] = 0
		relays[3].off()
		toggle_status(data)
	elif (data == 2):
		print("data = 3 High")
		relays_status[0] = 0
		relays[0].off()
		relays_status[1] = 0
		relays[1].off()
		relays_status[3] = 0
		relays[3].off()
		toggle_status(data)
	elif (data == 3):
		print("data = 4 Quick clean")
		relays_status[0] = 0
		relays[0].off()
		relays_status[1] = 0
		relays[1].off()
		relays_status[2] = 0
		relays[2].off()
		toggle_status(data)
	elif (data == 4):
		print("data = 5 heater on")
		toggle_status(data)
	elif (data == 5):
		print("data = 6 temp up")
		toggle_status(data)
		time.sleep(.5)
		toggle_status(data)
	elif (data == 6):
		print("data = 7 temp down")
		toggle_status(data)
		time.sleep(.5)
		toggle_status(data)
	elif (data == 7):
		print("data = 8 blower on")
		toggle_status(data)
	elif (data == 8):
		print("data = 9 light on")
		toggle_status(data)
	elif (data == 9):
		print("data = 10 valve 1")
		toggle_status(data)
		time.sleep(.5)
		toggle_status(data)
	elif (data == 10):
		print("data = 11 valve 2")
		toggle_status(data)
		time.sleep(.5)
		toggle_status(data)
	elif (data == 11):
		print("data = 12 valve 3")
		toggle_status(data)
		time.sleep(.5)
		toggle_status(data)
	else:
		print("erronous data")

@app.route('/')
def index():
    print('Client hitting the index page.')
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def connect():
	print("client connected")
	socketio.emit('relays_status', relays_status, namespace = '/test')

@socketio.on('client_event', namespace='/test')
def client_event(data):
	print("CLIENT DATA:", data)
	if(data == 12):
		#quickstart
		relay_switch(3)
		if(relays_status[4] != 1):
			print("turning on heater")
			relay_switch(4)
		
	elif(data == 13):
		#off
		if(relays_status[3] == 1):
			relay_switch(3)
			relays_status[3] = 0
		if(relays_status[4] == 1):
			relay_switch(4)
			relays_status[4] = 0
		if(relays_status[7] == 1):
			relay_switch(7)
			relays_status[7] = 0
		if(relays_status[8] == 1):
			relay_switch(8)
			relays_status[8] = 0
		
	else:
		relay_switch(data)

	socketio.emit('relays_status', relays_status, namespace = '/test')
	
	
if __name__ == '__main__':
	print ('>> Startdatag the Flask Websocket server.')
	socketio.run(app, host="0.0.0.0", allow_unsafe_werkzeug=True)
