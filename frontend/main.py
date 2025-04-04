from flask import Flask, render_template
from flask import request, jsonify
from chatbot_pipeline import find_best_match

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    
    #  API endpoint for chatbot interaction.

    user_input = request.json.get("message", "")
    response = find_best_match(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
