from pymongo import MongoClient
url="mongodb+srv://Prashil:prashil123@cluster0-uvyy0.mongodb.net/ipl2020?retryWrites=true&w=majority"

client=MongoClient(url)

def get_team_names():
    db=client.ipl2020
    collection=db.ipl
    teamNames=[]

    for ele in collection.find({},{"_id":0,"team":1}):
        teamNames.append(ele["team"])

    return teamNames


def get_team_labels():
    db=client.ipl2020
    collection=db.ipl
    teamNames=[]

    for ele in collection.find({},{"_id":0,"label":1}):
        teamNames.append(ele["label"])

    return teamNames

def get_team_details():
    db=client.ipl2020
    collection=db.ipl
    teamDetails=[]

    for ele in collection.find({}):
        teamDetails.append(ele)

    return teamDetails

def get_players():
    db=client.ipl2020
    collections=db.players
    players=[]
    for ele in collections.find({}):
        players.append(ele)

    return players

def get_team_players(teamName):
    db=client.ipl2020
    collections=db.players
    players=[]
    for ele in collections.find({"label":teamName}):
        players.append(ele)
    return players

def get_count(teamname):
    db=client.ipl2020
    collections=db.players
    arr=list()
    arr.append(collections.find({"label":teamname,"role":"Bowler"}).count())
    arr.append(collections.find({"label":teamname,"role":"Wicket Keeper"}).count())
    arr.append(collections.find({"label":teamname,"role":"All-Rounder"}).count())
    arr.append(collections.find({"label":teamname,"role":"Batsman"}).count())

    return arr

def get_statIPL():
    db=client.ipl2020
    collections=db.players
    max=-999999
    min=9999999999
    total=0
    arr=list()
    for ele in collections.find({}):
        if ele["price"]>max:
            max=ele["price"]
        elif ele["price"]<min:
            min=ele["price"]

        total=total+ele["price"]

    avg=total/(collections.find({}).count())

    arr.append(max)
    arr.append(min)
    arr.append(total)
    arr.append(avg)

    return arr

def get_statIPLTeam(teamname):
    db=client.ipl2020
    collections=db.players
    max=-999999
    min=9999999999
    total=0
    arr=list()
    for ele in collections.find({"label":teamname}):
        if ele["price"]>max:
            max=ele["price"]
        elif ele["price"]<min:
            min=ele["price"]

        total=total+ele["price"]

    avg=total/(collections.find({}).count())

    arr.append(max)
    arr.append(min)
    arr.append(total)
    arr.append(avg)

    return arr



        
