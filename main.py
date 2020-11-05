from flask import Flask, render_template
import datetime

time = datetime.datetime.now()

header_html = open('templates/header.html')
header = header_html.read()
header_html.close()

app = Flask(__name__)

PORT = 1234

@app.route('/')
def index():
    return render_template('index.html', header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 160%; margin-bottom: 0.89%; margin-left: auto; left: 50%; margin-right: 50%; transform: translate(-50%, 0); position: absolute;'>Kernfusionsreaktoren</h2>"))

@app.route('/iter')
def iter():
    return render_template('Iter/iter_index.html', time=time)

@app.route('/basics')
def basics():
    return render_template('Basics/basics_index.html', header=header)

@app.route('/reactors')
def reactors():
    return render_template('Reactors/reactor_index.html', header=header)

@app.route('/Stellarator')
def stellarator():
    return render_template('Reactors/Stellarator.html', header=header)

@app.route('/Tokamak')
def tokamak():
    return render_template('Reactors/Tokamak.html', header=header)

@app.route('/Vergleich')
def vergleich():
    return render_template('Reactors/Vergleich.html', header=header)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, threaded=True)