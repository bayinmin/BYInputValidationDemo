from flask import Flask, render_template, request, make_response
import boto3, botocore
import random

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/welcome', methods=["POST"])
# def process_welcome():
#     username = request.form['username'];
#     idnum = request.form['idnum']
#     return "welcome " + username + "<br/> Your Id is " + idnum

# Let Fix this
@app.route('/welcome', methods=["POST"])
def process_welcome():
    username = request.form['username'];
    idnum = request.form['idnum']
    # validate the username
    if len(username) < 1 or not(username.isalpha()):
        return "Yo, you should put valid username"
    # validate the password
    if len(idnum) < 1 or not(idnum.isdigit()):
        return "Yo, you should put valid identification number"

    return "welcome " + username + "<br/> Your Id is " + idnum

if __name__== '__main__':
	app.run(debug=True)



