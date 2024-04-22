from flask import Flask, request, jsonify #pip install flask
from flask_cors import CORS #pip install flask_cors
from mtgsdk import Card #pip install mtgsdk

app = Flask(__name__)
CORS(app)

@app.route("/search")
def search():
    query = request.args.get("query", "").lower()
    print("Received query:", query)  
    
    if query:
        print("Query found in data:", query)
        cards = Card.where(name=query).all()
        retCards = []
        for element in cards:
            print(element.name)
            retCards.append(element.name)
        return jsonify(list(set(retCards)))
    else:
        print("Query not found") 
        return jsonify([]) 

if __name__ == "__main__":
    app.run(debug=True)
