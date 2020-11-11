from flask import Flask, render_template #Importing flask page for the web interface
from dependencies import openDependencies #Loading openDependencies function out of dependencies modul, which is acutally dependencies.py. 

dependencies = openDependencies() #Loading dependencies
header  = dependencies[0]   #Defining header out of dependencies array
icon = dependencies[1]  #Defining icon out of dependencies array

app = Flask(__name__) #Setting up flask

PORT = 1234  #Defining the port the server will be listing to

@app.route('/') #Creating index and rendering specified template
def index():
    return render_template('index.html', icon=icon, header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>Kernfusionsreaktoren</h2>"))

@app.route('/iter') #Creating iter sub page and rendering specified template
def iter():
    title = "ITER - Ein Forschungsprojekt in Europa"
    return render_template('Iter/iter_index.html', header=header.replace('--name--', f"<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>{title}</h2>"))

@app.route('/iter/science')
def science():
    return render_template('Iter/iter_subpage1.html', header=header)


@app.route('/basics') #Creating basics sub page and rendering specified template
def basics():
    return render_template('Basics/basics_index.html', header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>Kerfusion</h2>"))

@app.route('/reactors') #Creating reactors sub page and rendering specified template
def reactors():
    return render_template('Reactors/reactor_index.html', header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>Reaktor Arten</h2>"))

@app.route('/reactors/stellarator') #Creating stellerator sub page of reactors and rendering specified template
def stellarator():
    return render_template('Reactors/Stellarator.html', header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>ITER - Forschung in Europa</h2>"))

@app.route('/reactors/tokamak') #Creating tokamak sub page of reactors and rendering specified template
def tokamak():
    return render_template('Reactors/tokamak.html', header=header)

@app.route('/reactors/vergleich') #Creating vergleich sub page of reactors and rendering specified template
def vergleich():
    return render_template('Reactors/vergleich.html', header=header)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, threaded=True) #Starting the server