from flask import Flask, render_template, render_template_string, request
from flask import jsonify
from flask_cors import CORS, cross_origin
import sqlite3 as sql

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
   conn = sql.connect('database.db')
   print("Opened database successfully")

   conn.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
   print("Table created successfully")
   conn.close()
   return render_template('home.html')

@app.route("/track/<id>")
def get_parcel(id):
   #take the id parameter and query the db with it
   return jsonify(
        idn = id,
        nameOfDriver = "John",
        status = "In transit",
        eta = "23 minutes",
        dispatchTime = "2pm",
        address = "33 Pain Street, london S4 7GP"
    )

@app.get("/directions/<id>")
def get_directions(id):
    
    #GET THE DIRECTION DATA FROM DATABASE
    #FOR THE EXAMPLE I WILL JUST USE DUMMY DATA
    directions = [{"field1": "field1 data"},
                  {"field1": "field2 data"}]
    
    """
        Any data you want to pass to the template you just
        list it as a keyword argument 
        e.g if you wanted to add a variable for user
        you would just add user=user_object 
    """
    return  render_template("directions.html", 
                            directions=directions)

@app.route('/enternew')
def new_student():
   return render_template('student.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug=True)
