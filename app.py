from flask import Flask, render_template,request
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html')



@app.route('/index')
def run_script():
    file = open(r'C:\collegeSPIT\SEM5\AIML\face_recognition_attendance\face_recognition\AIML_project\attendance.py', 'r').read()
    exec(file)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)