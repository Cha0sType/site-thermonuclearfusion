from flask import Flask, render_template
import datetime

time = datetime.datetime.now()

header_html = open('templates/header.html')
header = header_html.read()
header_html.close()

icon_svg = open('static/Icon.svg')
icon = icon_svg.read()
icon_svg.close()

app = Flask(__name__)

PORT = 1234

@app.route('/')
def index():
    return render_template('index.html', icon=icon, header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>Kernfusionsreaktoren</h2>"))

@app.route('/iter')
def iter():
    title = "ITER - Ein Forschungsprojekt in Europa"
    return render_template('Iter/iter_index.html', header=header.replace('--name--', f"<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>{title}</h2>"))

@app.route('/basics')
def basics():
    return render_template('Basics/basics_index.html', header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>Kerfusion</h2>"))

@app.route('/reactors')
def reactors():
    return render_template('Reactors/reactor_index.html', header=header.replace('--name--', "<h2 style='color: rgba(255, 255, 255, 0.8); font-weight: normal; font-size: 1.61vw; margin-bottom: 0.9vw; margin-left: auto; margin-left: 50%; transform: translateX(-50%); position: absolute;'>Reaktor Arten</h2>"))

@app.route('/reactors/stellarator')
def stellarator():
    return render_template('Reactors/Stellarator.html', header=header)

@app.route('/reactors/tokamak')
def tokamak():
    return render_template('Reactors/tokamak.html', header=header)

@app.route('/reactors/vergleich')
def vergleich():
    return render_template('Reactors/vergleich.html', header=header)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, threaded=True)