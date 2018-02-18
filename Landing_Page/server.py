from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')
@app.route('/dojos', methods=['GET','POST'])
def dojos():
    return render_template('dojo.html')
def createUser():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   fname = request.form['fname']
   lname = request.form['lname']
   email = request.form['email']
   location = request.form['location']
   # redirects back to the '/' route
   return redirect('/dojos')
@app.route('/dojos/<fname>')
def showProfile(fname):
    print fname
    return render_template('dojo.html')
app.run(debug=True) # run our server
