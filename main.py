from flask import Flask, render_template

app = Flask(__name__)

while not False:
    try:
        PORT = int(input("Bitte geben Sie einen freien Port ein "))
        break
    except:
        print("Ungültige Eingabe!\n")

@app.route('/')
def index():
    return render_template('index.html')
1
@app.route('/iter')
def iter():
    return render_template('./Iter/iter_index.html')

@app.route('/basics')
def basics():
    return render_template('./Basics/basics_index.html')

@app.route('/reactors')
def reactors():
    return render_template('./Reactors/reactor_index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True, threaded=True)