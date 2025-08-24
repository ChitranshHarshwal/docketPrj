## flask app for G'day Mate

from flask import Flask
import os
app=Flask(__name__)

@app.route('/', methods=['GET'])
def home(): 
    return "G'day mate!!"

if __name__== "__main__": 
    app.run(debug=True, host="0.0.0.0", port=5000)