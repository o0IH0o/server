from flask import Flask
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS hello('
               'id INTEGER PRIMARY KEY, '
               'context TEXT)')

result = cursor.execute('SELECT * FROM hello').fetchall()
if result is None:
    insert_query = 'INSERT INTO hello VALUES(?, ?)'

    users = [number, string]

    users.append((1, 'penguin'))
    users.append((2, 'giraffe'))
    users.append((3, 'shark'))

    cursor.executemany(insert_query, users)
    conn.commit()
conn.close()

@app.route("/")
def hello():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    result = cursor.execute('SELECT context FROM hello').fetchall()
    conn.close()
    if result is None:
        return "Hello Word"
    else:
        python2json = {}
        data = []
        for i in result:
            data.append(i[0])
        python2json["listData"] = data
        json_str = json.dumps(python2json)
        print ("test")
        print (json_str)
        return json_str

@app.route("/goodbye")
def goodbye():
    return "GoodBye World"

if __name__ == "__main__":
    app.run()