import os

from flask import Flask, render_template, request, flash, redirect, session, abort
from random import randint

app = Flask("story_time")

@app.route("/")
def storytime():
    #fill in the blanks
    character = ["human", "dwarf", "ogre", "elf", "gnome", "centaur"]
    randomCharacter = randint(0,len(character)-1)
    character = character[randomCharacter]

    name = ["Olga", "Arabella", "Morgana", "Beatriz", "Luna", "Hazel"]
    randomName = randint(0,len(name)-1)
    name = name[randomName]

    location = ["cabin in the woods", "luxury mansion", "run-down castle",
    "spooky cave", "jungle treehouse", "thatched cottage"]
    randomLocation = randint(0,len(location)-1)
    location = location[randomLocation]

    dream = ["owning a fishing business",
    "becoming the greatest chef in the land",
    "sleeping for sixteen hours a day and not much else",
    "creating powerful spells and potions",
    "opening a rescue centre for abandoned magical creatures",
    "destroying everyone and everything in their path"]
    randomDream = randint(0,len(dream)-1)
    dream = dream[randomDream]

    destiny = ["avenge their parents",
    "become a grandmaster chess player",
    "achieve nothing spectacular",
    "open an enormous dairy farm",
    "become the palace cake decorator",
    "destroy the world"]
    randomDestiny = randint(0,len(destiny)-1)
    destiny = destiny[randomDestiny]

    activity = ["chopping wood",
    "weaving a blanket",
    "chatting to the local frogs",
    "cooking a chicken",
    "trying to turn water into wine",
    "getting really drunk"]
    randomActivity = randint(0,len(activity)-1)
    activity = activity[randomActivity]

    artifact = ["an ancient tome",
    "a jewelled sceptre",
    "a novelty colour-change mug",
    "a toy snake",
    "a magical sword",
    "a rusted mace"]
    randomArtifact = randint(0,len(artifact)-1)
    artifact = artifact[randomArtifact]

    nemesis = ["Randolph the wizard",
    "Chef Thompson: the second best chef in the land",
    "Elpheba, her secret twin sister",
    "Darius, the man who could turn into a raven",
    "Boris the dragon",
    "Sissy, seemingly a normal teenage girl"]
    randomNemesis = randint(0,len(nemesis)-1)
    nemesis = nemesis[randomNemesis]

    landscape = ["scorching deserts",
    "an enchanted forest",
    "a fairly small town",
    "misty mountains",
    "an intricate forgotten mine",
    "landscapes you could only dream of"]
    randomLandscape = randint(0,len(landscape)-1)
    landscape = landscape[randomLandscape]

    companion = ["Pepe the frog",
    "Reginald the bee",
    "Aberforth the chameleon",
    "Fifi the miniature horse",
    "Alfonso the siberian tiger",
    "Flappy the enormous butterfly"]
    randomCompanion = randint(0,len(companion)-1)
    companion = companion[randomCompanion]

    task = ["return",
    "destroy",
    "paint a portrait of",
    "create a display cabinet for",
    "stare at",
    "work out the secrets of"]
    randomTask = randint(0,len(task)-1)
    task = task[randomTask]

    return render_template("index.html", **locals())

"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at https://www.heroku.com/ before the deployment session!). When
running the app on Heroku, the PORT environment/config variable is pre-populated by
Heroku to tell our app the correct port to run on.
"""
if "PORT" in os.environ:
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
    app.run(debug=True)
