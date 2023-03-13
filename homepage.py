from flask import Flask,render_template
app = Flask(__name__)

import datetime
adesso = datetime.datetime.now()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', ora = adesso)


@app.route('/mappa', methods=['GET'])
def mappa():
    return render_template('mappa.html')

@app.route('/mappa600', methods=['GET'])
def mappa600():
    return render_template('mappa.html',larghezza = 600)

@app.route('/mappa800', methods=['GET'])
def mappa800():
    return render_template('mappa.html', larghezza =  800)

@app.route('/mappa1000', methods=['GET'])
def mappa1000():
    return render_template('mappa.html',larghezza =  1000)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)