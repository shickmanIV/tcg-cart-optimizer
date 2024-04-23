from flask import Flask, request, jsonify #pip install flask
from flask_cors import CORS #pip install flask_cors
from mtgsdk import Card #pip install mtgsdk

app = Flask(__name__)
CORS(app)
#CORS(app, origins="http://localhost:5500")

@app.route("/search")
def search():
    query = request.args.get("query", "").lower()
    print("Received query:", query)  
    if query.isnumeric():
        print("YESSSS")
    else:
        if query:
            print("Query found in data:", query)
            cards = Card.where(name=query).all()
            retCards = []
            for element in cards:
                if element.name and element.multiverse_id:
                    retCards.append(element.name)
                    retCards.append(element.multiverse_id)
            return jsonify(retCards) # List to Set to List to avoid duplicates
        else:
            print("Query not found") 
            return jsonify([]) 
    

if __name__ == "__main__":
    app.run(debug=True)
