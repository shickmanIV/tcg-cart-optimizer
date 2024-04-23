# from flask import Flask, request, jsonify #pip install flask
# from flask_cors import CORS #pip install flask_cors
# from mtgsdk import Card #pip install mtgsdk

# app = Flask(__name__)
# CORS(app)


# @app.route("/card")
# def search():
#     query = request.args.get("query", "").lower()
#     print("Received query CardAPI:", query)  
    
#     if query:
#         print("Query found in data CardAPI:", query)
#         cards = Card.find(query)
#         retCards = []
#         retCards.append([cards.name, cards.image_url, cards.id])
#         return jsonify(retCards)
#     else:
#         print("Query not found CardAPI") 
#         return jsonify([]) 

# if __name__ == "__main__":
#     app.run(debug=True)