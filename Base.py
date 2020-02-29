from flask import Flask, render_template , request
#from flask.extpymongo import PyMongo
#I was unable to connect the text area to a db and associate each input with a UUID
# OpenCV would be used to view the webcam and there is a google hangout api avalible which would be used to enable a hangouts connection

app = Flask(__name__)

@app.route("/")


@app.route("/home")
def home():
    return render_template('home.html')
  


if __name__ == "__main__":
    app.run(debug=True)