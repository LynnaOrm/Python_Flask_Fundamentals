from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)    
app.secret_key = "Secret"
                         
@app.route('/')                                  
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')   

@app.route("/add2", methods=["POST"])
def button():
    session['count'] += 1
    return redirect('/')

app.run(debug=True) 
