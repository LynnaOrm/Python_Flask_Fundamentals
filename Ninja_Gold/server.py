from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)    

app.secret_key = "Secret"
                         
@app.route('/')                                
def index():
    if "totalCoins" not in session:
       session["totalCoins"] = 0;

    if "log" not in session:
        session["log"] =[];

    loglength = len(session["log"])
    revList = list(reversed(session["log"]))

    return render_template('index.html', totalCoins = session['totalCoins'], log=revList, loglength = loglength)

@app.route('/process_money', methods=["POST"])
def process_money():
    if request.form["place"] == "Farm":
        FarmMoney = random.randrange(10,21)
        session["totalCoins"] += FarmMoney
        myStr = "Found" + str(FarmMoney) + "gold at the farm"

    if request.form["place"] == "Cave":
        CaveMoney = random.randrange(10,21)
        session["totalCoins"] += CaveMoney
        myStr = "Found" + str(CaveMoney) + "gold at the cave"
       

    if request.form["place"] == "House":
        HouseMoney = random.randrange(10,21)
        session["totalCoins"] += HouseMoney
        myStr = "Found" + str(HouseMoney) + "gold at the House"
        

    if request.form["place"] == "Casino":
        CasinoMoney = random.randrange(10,21)
        session["totalCoins"] += CasinoMoney
        myStr = "Found" + str(CasinoMoney) + "gold at the Casino"
        

    
    return redirect('/')

    
app.run(debug=True)
