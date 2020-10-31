from flask import Flask, render_template
import datetime

time = datetime.datetime.now()

app = Flask(__name__)

PORT = 1234

@app.route('/')
def index():
    return render_template('index.html')
1
@app.route('/iter')
def iter():
    return render_template('./Iter/iter_index.html', var=time)

@app.route('/basics')
def basics():
    return render_template('./Basics/basics_index.html')

@app.route('/reactors')
def reactors():
    return render_template('./Reactors/reactor_index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, threaded=True)