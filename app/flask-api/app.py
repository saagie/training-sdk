
from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Flask API for Saagie'

@app.route('/sdk')
def sdk():
    return 'Saagie Training on SDK'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
