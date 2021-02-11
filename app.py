from flask import Flask, jsonify
from random import randint
import sqlite3
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
    r"/*" :{
        "origin": "*"
    }
})

@app.route('/phrase')
def random_phrase():

    try:
        # connect at the DB
        conn = sqlite3.connect('DB/phrases.db')
        cursor = conn.cursor()

        # Get len of array
        cursor.execute("SELECT * FROM ALL_PHRASES")
        all = len(cursor.fetchall())

        if all == 35:
            all -= 1
        
        elif all == 4:
            all += 1

        #Get phrase by random id
        cursor.execute("SELECT * FROM ALL_PHRASES WHERE ID = {0}".format(randint(0,all)))
        req = cursor.fetchone()

        # convert phrase in object
        res = {
            "ID":req[0],
            "Author":req[1],
            "Phrase":req[2]
        }

        conn.commit()
        conn.close()
        
        # Return response
        return jsonify(res)
    
    except:
        return jsonify("PHRASE NOT FOUND")
    


if __name__ == '__main__':
    app.run(debug=True,port=5000)
