from flask import Flask, render_template # Importing flask page for the web interface
from dependencies import openDependencies # Loading openDependencies function out of dependencies modul, which is acutally dependencies.py. 
import json #Importing JSON to use it for our config file

with open('server_config.json', 'r') as server: #Opening and loading JSON config file
    config = json.load(server)


PORT = config["port"]
if config["debug"] == "true": #Testing for false because if it's an invalid input in the config, it is usually the best to go with debug turned off
    debug = True
else:
    debug = False
if config["threaded"] == "false": #Testing for false because if it's an invalid input in the config, it is usually the best to go with threaded turned on
    threaded = False
else:
    threaded = True


dependencies = openDependencies()

header = dependencies[0]   # Defining header out of dependencies array
footer = dependencies[1]
icon = dependencies[2]  # Defining icon out of dependencies array

app = Flask(__name__) # Setting up flask

 # Defining the port the server will be listing to

headername = ""

@app.route('/') # Creating index and rendering specified template
def index():
    return render_template('index.html', icon=icon, footer=footer.replace('--sources--', 'Für diese Seite<br>gibt es keine<br>Quellen'), header=header.replace('--name--', "Kernfusionsreaktoren"))

@app.route('/iter') # Creating iter sub page and rendering specified template
def iter():
    return render_template('Iter/iter_index.html', footer=footer.replace('--sources--', '<a href="https://de.wikipedia.org/wiki/ITER" target="_blank">ITER Wiki</a><br><a href="https://iter.org" target="_blank">Iter (Offizelle Website)</a>'), header=header.replace('--name--', "ITER - Ein internationales Forschungsprojekt"))

@app.route('/iter/science') # Creating iter sub page and rendering specified template
def science():
    return render_template('Iter/iter_science.html', footer=footer.replace('--sources--', '<a href="https://de.wikipedia.org/wiki/ITER" target="_blank">ITER Wiki</a><br><a href="https://iter.org" target="_blank">Iter (Offizelle Website)</a>'), header=header.replace('--name--', "ITER - Forschung in Europa"))

@app.route('/iter/status')
def status():
    return render_template('Iter/iter_status.html', footer=footer.replace('--sources--', '<a href="https://de.wikipedia.org/wiki/ITER" target="_blank">ITER Wiki</a><br><a href="https://iter.org" target="_blank">Iter (Offizelle Website)</a>'), header=header.replace('--name--', "ITER - Status"))

@app.route('/basics') #Creating basics sub page and rendering specified template
def basics():
    return render_template('Basics/basics_index.html', footer=footer.replace('--sources--', '<a href="https://physikunterricht-online.de/jahrgang-12/kernfusion/" target="_blank">Kernfusion</a><br><a href="https://physikunterricht-online.de/jahrgang-12/kernfusion/" target="_blank">Kernfusion (Allgemein)</a><br><a href="https://www.lernhelfer.de/schuelerlexikon/physik/artikel/kernfusion#" target="_blank">Kernfusion (Sonne)</a>'), header=header.replace('--name--', "Physik der Kernfusion"))

@app.route('/basics/fusionsablauf')
def fusionsablauf():
    return render_template('Basics/fusionsablauf.html', footer=footer.replace('--sources--', '<a href="https://physikunterricht-online.de/jahrgang-12/kernspaltung/" target="_blank">Allgemein</a><br><a href="https://www.youtube.com/watch?v=fBJ7MW2daPU" target="_blank">Deuterium und Tritium</a><br><a href="https://www.youtube.com/watch?v=_g54PJhXYxU">Masseäquivalenzformel <br>und Hitze</a>'), header=header.replace('--name--', "Wie läuft eine Fusion ab?"))

@app.route('/basics/bedingungen')
def bedingungen():
    return render_template('Basics/bedingungen.html', footer=footer.replace('--sources--', '<a href="https://physikunterricht-online.de/jahrgang-12/kernspaltung/" target="_blank">Allgemein</a><br><a href="https://www.youtube.com/watch?v=fBJ7MW2daPU" target="_blank">Deuterium und Tritium</a><br><a href="https://www.youtube.com/watch?v=_g54PJhXYxU">Masseäquivalenzformel <br>und Hitze</a>'), header=header.replace('--name--', "Wann kommt es zur Fusion?"))

@app.route('/reactors') # Creating reactors sub page and rendering specified template
def reactors():
    return render_template('Reactors/reactor_index.html', footer=footer.replace('--sources--', 'Für diese Seite<br>gibt es keine<br>Quellen'), header=header.replace('--name--', "Reaktoren"))

@app.route('/reactors/stellarator') # Creating stellerator sub page of reactors and rendering specified template
def stellarator():
    return render_template('Reactors/Stellarator.html', footer=footer.replace('--sources--', '<a href="https://de.wikipedia.org/wiki/Stellarator" target="_blank">Stellarator Wiki</a>'), header=header.replace('--name--', "Stellarator"))

@app.route('/reactors/tokamak') # Creating tokamak sub page of reactors and rendering specified template
def tokamak():
    return render_template('Reactors/tokamak.html', footer=footer.replace('--sources--', '<a href="https://de.wikipedia.org/wiki/Tokamak" target="_blank">Tokamak Wiki</a>'), header=header.replace('--name--', "Tokamak"))

@app.route('/reactors/vergleich') # Creating vergleich sub page of reactors and rendering specified template
def vergleich():
    return render_template('Reactors/vergleich.html', footer=footer.replace('--sources--', '<a href="https://de.wikipedia.org/wiki/Stellarator" target="_blank">Stellarator Wiki</a><br><a href="https://de.wikipedia.org/wiki/Tokamak" target="_blank">Tokamak Wiki</a>'), header=header.replace('--name--', "Vergleich"))

@app.route('/quiz')
def quiz():
    return render_template('extras/Quiz/quiz.html', footer=footer.replace('--sources--', 'Für diese Seite<br>gibt es keine<br>Quellen'), header=header.replace('--name--', "Quiz"))

@app.route('/extras/snake')
def snake():
    return render_template('extras/HeliumSnake/helium_snake.html', footer=footer.replace('--sources--', 'Für diese Seite<br>gibt es keine<br>Quellen'), header=header.replace('--name--', "Helium Snake"))

@app.route('/secret')
def secret():
    return '<meta http-equiv="refresh" content="3; URL=/extras/snake"><body style="display: flex; justify-content: center; align-items: center;"><h1 id="text" style="font-family: Arial; font-size: 3vw;">Du alter Secrethunter</h></body><script>setTimeout(() => {document.getElementById("text").innerHTML = "Du hast das geheime Snake Game gefunden =)!";}, 1500);</script>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=debug, threaded=threaded)
    # Starting the server, the threaded=True makes it possible to handle more connections
    # at the same time, which makes it more performant