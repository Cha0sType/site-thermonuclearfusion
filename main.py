from flask import Flask, render_template #Importing flask page for the web interface
from dependencies import openDependencies #Loading openDependencies function out of dependencies modul, which is acutally dependencies.py. 

dependencies = openDependencies() #Loading dependencies
header  = dependencies[0]   #Defining header out of dependencies array
icon = dependencies[1]  #Defining icon out of dependencies array

app = Flask(__name__) #Setting up flask

PORT = 1234  #Defining the port the server will be listing to

headername = "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>---</h2>"

@app.route('/') #Creating index and rendering specified template
def index():
    return render_template('index.html', icon=icon, header=header.replace('--name--', headername.replace('---', "Kernfusionsreaktoren")))

@app.route('/iter') #Creating iter sub page and rendering specified template
def iter():
    return render_template('Iter/iter_index.html', header=header.replace('--name--', headername.replace('---', "ITER - Ein europäisches Forschungsprojekt")))

@app.route('/basics') #Creating basics sub page and rendering specified template
def basics():
    return render_template('Basics/basics_index.html', header=header.replace('--name--', headername.replace('---', "Physik der Kernfusion")))

@app.route('/reactors') #Creating reactors sub page and rendering specified template
def reactors():
    return render_template('Reactors/reactor_index.html', header=header.replace('--name--', headername.replace('---', "Reaktoren")))

@app.route('/reactors/stellarator') #Creating stellerator sub page of reactors and rendering specified template
def stellarator():
    return render_template('Reactors/Stellarator.html', header=header.replace('--name--', headername.replace('---', "Stellarator")))

@app.route('/reactors/tokamak') #Creating tokamak sub page of reactors and rendering specified template
def tokamak():
    return render_template('Reactors/tokamak.html', header=header.replace('--name--', headername.replace('---', "Tokamak")))

@app.route('/reactors/vergleich') #Creating vergleich sub page of reactors and rendering specified template
def vergleich():
    return render_template('Reactors/vergleich.html', header=header.replace('--name--', headername.replace('---', "Vergleich")))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, threaded=True) #Starting the server, the 