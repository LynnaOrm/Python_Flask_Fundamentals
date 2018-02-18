from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/submit', methods=['POST'])
def user():
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   return render_template('submit.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)
