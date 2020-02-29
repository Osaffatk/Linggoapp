from flask import Flask, render_template , request
from flask_socketio import SocketIO, send

# Opens server for users to add notes together
app = Flask(__name__)
app.config ['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route("/")

# tells flask to use home template

@app.route("/home")
def home():
    return render_template('home.html')

# This is used to send the message to every user on the video call 

@socketio.on('message')
def handleMessage(msg):
    print('Message:' + msg)
    send(msg, broadcast=True)

# Runs the server

if __name__ == "__main__":
    socketio.run(app)
    app.run(debug=True)