from flask import Flask, render_template # Importing flask page for the web interface
from dependencies import openDependencies # Loading openDependencies function out of dependencies modul, which is acutally dependencies.py. 
import json #Importing JSON to use it for our config file

with open('server_config.json', 'r') as server:
    config = json.load(server)


port = config["port"]
if config["debug"] == "true": #Testing for false because when it's an invalid input in the config, it is usually the best to go with debug off
    debug = True
else:
    debug = False
if config["threaded"] == "false": #Testing for false because when it's an invalid input in the config, it is usually the best to go with threaded
    threaded = False
else:
    threaded = True


dependencies = openDependencies()

header = dependencies[0]   # Defining header out of dependencies array
footer = dependencies[1]
icon = dependencies[2]  # Defining icon out of dependencies array

app = Flask(__name__) # Setting up flask

 # Defining the port the server will be listing to

headername = "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: 50%; transform: translateX(-60%); position: absolute;'>---</h2>"

@app.route('/') # Creating index and rendering specified template
def index():
    return render_template('index.html', icon=icon, footer=footer, header=header.replace('--name--', headername.replace('---', "Kernfusionsreaktoren")))

@app.route('/iter') # Creating iter sub page and rendering specified template
def iter():
    return render_template('Iter/iter_index.html', footer=footer, header=header.replace('--name--', headername.replace('---', "ITER - Ein internationales Forschungsprojekt")))

@app.route('/iter/sience') # Creating iter sub page and rendering specified template
def science():
    return render_template('Iter/iter_subpage1.html', footer=footer, header=header.replace('--name--', headername.replace('---', "ITER - Forschung in Europa")))

@app.route('/basics') #Creating basics sub page and rendering specified template
def basics():
    return render_template('Basics/basics_index.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Physik der Kernfusion")))

@app.route('/basics/fusionsablauf')
def fusionsablauf():
    return render_template('Basics/fusionsablauf.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Wie läuft eine Fusion ab?")))

@app.route('/basics/bedingungen')
def bedingungen():
    return render_template('Basics/bedingungen.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Helium Snake")))

@app.route('/reactors') # Creating reactors sub page and rendering specified template
def reactors():
    return render_template('Reactors/reactor_index.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Reaktoren")))

@app.route('/reactors/stellarator') # Creating stellerator sub page of reactors and rendering specified template
def stellarator():
    return render_template('Reactors/Stellarator.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Stellarator")))

@app.route('/reactors/tokamak') # Creating tokamak sub page of reactors and rendering specified template
def tokamak():
    return render_template('Reactors/tokamak.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Tokamak")))

@app.route('/reactors/vergleich') # Creating vergleich sub page of reactors and rendering specified template
def vergleich():
    return render_template('Reactors/vergleich.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Vergleich")))

@app.route('/extras/snake')
def snake():
    return render_template('extras/helium_snake.html', footer=footer, header=header.replace('--name--', headername.replace('---', "Helium Snake")))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=debug, threaded=threaded)
    # Starting the server, the threaded=True makes it possible to handle more connections
    # at the same time, which makes it more performant