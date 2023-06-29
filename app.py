from flask import Flask, render_template
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/user')
def get_user():
    return jsonify(
        username = "Ahmed",
        email = "ahmed@test.com",
        id = "00982"
    )

@app.route('/car')
def get_car():
    return jsonify(
        make = "Audi",
        model = "A7",
        style = "Black Edition"
    )

@app.route('/class')
def get_class():
    return jsonify(
        name = "Y12 CS",
        quality = "Kinda Poor now",
        potential = "High"
    )


if __name__ == '__main__':
   app.run(debug=True)