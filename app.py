from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_socketio import SocketIO
import boto3
import os
from io import StringIO
import io
from PIL import Image
import time
import pandas as pd 
from dotenv import load_dotenv
import json
import re 

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/', methods=['GET', 'POST'])
def index_get():
    return render_template("base.html")

@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    return render_template('doctor.html')

@app.route('/patient', methods=['GET', 'POST'])
def patient():
    return render_template('patient.html')

@app.route("/chat_doctor", methods=['POST'])
def chat_doctor():
    # receive question from user 
    question = request.get_json().get("message")
    message = {"answer": "I received you message. I will reply to you soon."}
    return (message)

@app.route("/chat_patient", methods=['POST'])
def chat_patient():
    # receive question from user 
    question = request.get_json().get("message")
    message = {"answer": "I received you message. I will reply to you soon."}
    return (message)

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    socketio.run(app, host='0.0.0.0', port=8080)
