from flask import Flask, session, render_template, request, redirect, url_for
import sys, database

application = Flask(__name__)

# application.secret_key = "lkjds#2-1j@dsp!ldaskfj"


@application.route("/")
def hello():
    return render_template("hello.html")



@application.route("/delivery")
def delivery():
    return render_template("deliveryman.html")

@application.route("/receiver")
def receiver():
    return render_template("receiver.html")


@application.route("/upload_done", methods=["POST"])
def upload_done():
    phoneNum = request.form['recvPhone']
    database.save(phoneNum)
    print(phoneNum)
    return render_template('after.html', data=phoneNum)


@application.route("/receive_done")
def receive_done():
    return render_template("after2.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')
