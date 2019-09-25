#######################
# Flask Application
#######################

#Dependencies
from flask import Flask, render_template
import os

# Flask Setup
app = Flask(__name__)

#Flask routes
@app.route('/')
def index():
   return render_template('index.html')

@app.route("/data.html")
def raw_data():
    return render_template('data.html')

if __name__ == '__main__':
   app.run(debug=True)
