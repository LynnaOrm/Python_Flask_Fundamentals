from flask import Flask, request, render_template, redirect, url_for
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninjas')
def ninjas():
    return render_template('ninja_turtles.html')

#Ninja Turtles
#blue= Leonardo
#orange= Michelangelo
#red= Raphael
#purple= Donatello

@app.route('/ninjas/<color>')
def ninjaColors(color):
    if color == 'blue':
        color = url_for('static', filename='Ninja_photos/leonardo.jpg')
        return render_template("ninja_colors.html", color = color)

    elif color == 'orange':
        color = url_for('static', filename='Ninja_photos/michelangelo.jpg')
        return render_template("ninja_colors.html", color = color)

    elif color == 'red':
        color = url_for('static', filename='Ninja_photos/raphael.jpg')
        return render_template("ninja_colors.html", color = color)

    elif color == 'purple':
        color = url_for('static', filename='Ninja_photos/donatello.jpg')
        return render_template("ninja_colors.html", color = color)
    else:
        color = url_for('static',filename='Ninja_photos/notapril.jpg')
        return render_template("ninja_colors.html", color = color)


app.run(debug=True)