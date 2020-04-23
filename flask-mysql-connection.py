from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
import json
app = Flask(__name__)

# Database connection info. Note that this is not a secure connection.
app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'Identity_Details'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

#api building
@app.route('/')
def search():
    cursor.execute("SELECT * from Identity")
    conn.commit()
    data = cursor.fetchall()
    return json.dumps({'Data':str(data)})
       

if __name__ == '__main__':
    app.debug = True
    app.run()