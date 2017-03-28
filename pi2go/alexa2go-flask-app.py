from flask import Flask
import pi2go
import time

speed = 60

pi2go.init()
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello world'

@app.route('/forward')
def forward():
	print("Forward!")
	pi2go.forward(speed)
	time.sleep(1)	# for 1 second.
	pi2go.stop()
	return 'Robot moved forward!'

@app.route('/left')
def left():
	print("Left!")
	pi2go.spinLeft(speed)
	time.sleep(1)	# for 1 second.
	pi2go.stop()
	return 'Robot turned left!'

@app.route('/right')
def right():
	print("Right!")
	pi2go.spinRight(speed)
	time.sleep(1)	# for 1 second.
	pi2go.stop()
	return 'Robot turned right!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
