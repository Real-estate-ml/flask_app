from flask import Flask, render_template, request
from connect_gcs import get_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/resultat', methods = ['POST'])
def resultat():
    result = request.form
    surface = result['surface']
    localisation = result['localisation']
    pieces = result['pieces']
    return render_template("resultat.html", surface=surface, localisation=localisation, pieces=pieces, price=get_prediction(int(pieces), int(surface), int(localisation)))

@app.route('/ourservice')
def ourservice():
    return render_template('ourservice.html')

if __name__ == '__main__':
    app.run(debug=True)