from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
1
@app.route('/iter')
def iter():
    return "Iter side in progress"

@app.route('/basics')
def basics():
    return "Basics of nuclear fusion reactor side in progress"

@app.route('/reactors')
def reactors():
    return "Reactors side in progress"

if __name__ == '__main__':
    app.run(port=1234, debug=True, threaded=True)