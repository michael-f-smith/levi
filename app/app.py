import requests
from flask import Flask, Response, request, render_template
from picamera2 import Picamera2
import cv2

# Roomba adapter
from pyroombaadapter import PyRoombaAdapter
import math

# Adapter setup
PORT = "/dev/ttyUSB0"
adapter = PyRoombaAdapter(PORT)
adapter.change_mode_to_safe() # Needed for movement
print(f"Mode: {adapter.request_oi_mode()}")


### You can donate at https://www.buymeacoffee.com/mmshilleh 
# https://www.instructables.com/How-to-Stream-Video-From-Raspberry-Pi-to-Local-USB/
app = Flask(__name__)

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
camera.start()

def generate_frames():
    while True:
        frame = camera.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form["my_button"] == "button1":
            # Action for button 1
            message = "Button 1 was clicked! Moving forward"
            adapter.move(0.2, math.radians(0.0))
        elif request.form["my_button"] == "button2":
            # Action for button 2
            message = "Button 2 was clicked! Yawing left"
            adapter.move(0, math.radians(20))
        elif request.form["my_button"] == "button3":
            # Action for button 3
            message = "Button 3 was clicked! Stopping"
            adapter.move(0, math.radians(0.0))
        elif request.form["my_button"] == "button4":
            # Action for button 4
            message = "Button 4 was clicked! Yawing right"
            adapter.move(0, math.radians(-20))
        elif request.form["my_button"] == "button5":
            # Action for button 4
            message = "Button 5 was clicked! Moving backward"
            adapter.move(-0.2, math.radians(0.0))
        elif request.form["my_button"] == "button6":
            message = "Button 6 was clicked! Sending home"
            adapter.start_seek_dock()
        elif request.form["my_button"] == "button7":
            message = "Button 7 was clicked! Starting spot clean"
            adapter.start_spot_cleaning()
        elif request.form["my_button"] == "button8":
            adapter.change_mode_to_safe()
            message = "Button 8 was clicked. Changing mode to safe. Mode:" + str(adapter.request_oi_mode())
        else:
            message = "No button clicked."
        return render_template("index.html", message=message)
    return render_template("index.html", message="")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
