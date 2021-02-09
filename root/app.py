from flask import Flask, jsonify
from random import randint

app = Flask(__name__)

@app.route('/phrase')
def random_phrase():
    
    algo = randint(1,35)

    prueba = {"mensaje":algo}
    return jsonify(prueba)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
