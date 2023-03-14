from flask import Flask,render_template
app = Flask(__name__)

import datetime

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', ora = datetime.datetime.now())


@app.route('/mappa', methods=['GET'])
def mappa():
    return render_template('mappa.html')

@app.route('/mappa/<width>', methods=['GET'])
def mappaWidth(width):
    return render_template('mappa.html',larghezza = width)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)