from flask import Flask, jsonify
from random import randint
import sqlite3

app = Flask(__name__)

@app.route('/phrase')
def random_phrase():

    try:
        # connect at the DB and get phrase
        conn = sqlite3.connect('DB/phrases.db')
        cursor = conn.cursor()
        cursor.execute("SELECT ID, AUTOR, PHRASE FROM ALL_PHRASES WHERE ID = {0}".format(randint(1,35)))
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
