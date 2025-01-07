# app.py
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS  # Import CORS
from game import run_game  # Import your quantum game logic

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_quantum', methods=['POST'])
def run_quantum():
    result = run_game()  # Call the function from game.py
    return jsonify({'quantum_result': result})

if __name__ == '__main__':
    app.run(debug=True)
