from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    my_projects =['Hiking The Enchantments','Electric Daisey Carnival','CRSSD Festival','La Push WA']
    return render_template('projects.html', projects=my_projects)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)
