from flask import Flask,jsonify
import ipldb as ipl
from mongoflask import MongoJSONEncoder

app=Flask(__name__)
app.json_encoder=MongoJSONEncoder

@app.route('/')
def welcome():
    return jsonify({"message":"Hello from Flask"})


@app.route('/ipl/teamlabels')
def team_labels():
    labels=ipl.get_team_labels()
    return jsonify({"label":labels})

@app.route('/ipl/teams')
def team_details():
    details=ipl.get_team_details()
    return jsonify({"details":details})


@app.route('/ipl/players')
def get_players():
    players=ipl.get_players()
    return jsonify({"Players":players})

@app.route('/ipl/teams/<teamname>')
def get_teamPlayers(teamname):
    teamplayers=ipl.get_team_players(teamname)
    return jsonify({"TEAM PLAYERS":teamplayers})

@app.route('/ipl/count/<teamname>')
def get_count(teamname):
    count=ipl.get_count(teamname)
    return jsonify({"Bowlers":count[0],"Wicket_Keeper":count[1],"All_Rounder":count[2],"Batsman":count[3]})

@app.route('/stats')
def get_iplstats():
    data=ipl.get_statIPL()
    if data[1]==0:
        minPrice=2000000
    else:
        minPrice=data[1]
    return jsonify({"Max Price":data[0],"Min Price":minPrice,"Total Price":data[2],"Average Price":data[3]})

@app.route('/ipl/stats/<teamname>')
def get_teamstats(teamname):
    data=ipl.get_statIPLTeam(teamname)
    if data[1]==0:
        minPrice=2000000
    else:
        minPrice=data[1]
    return jsonify({"Max Price":data[0],"Min Price":minPrice,"Total Price":data[2],"Average Price":data[3]})


if __name__ == "__main__":
    app.run()