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
    file = open(r'D:/AI_ML/AIML_project-main/attendance.py', 'r').read()
    exec(file)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)