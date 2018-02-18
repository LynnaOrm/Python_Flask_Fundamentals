from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)    

app.secret_key = "Secret"
                         
@app.route('/', methods =["GET","POST"])                                  
def places():

    return render_template('index.html')   

app.run(debug=True)