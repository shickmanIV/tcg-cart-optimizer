from flask import Flask, request, jsonify, Blueprint #pip install flask
from flask_cors import CORS #pip install flask_cors
from mtgsdk import Card #pip install mtgsdk

bp = Blueprint('search_page_bp', __name__)
CORS(bp)

@bp.route("/search")
def search():
    query = request.args.get("query", "").lower()
    print("Received query:", query)  
    if query.isdigit():
        print("Query is a 6-digit number:", query)
        card = Card.find(query)
        retCard = []
        retCard.append(card.name)
        retCard.append(card.image_url)
        retCard.append(card.multiverse_id)
        retCard.append(card.set_name)
        retCard.append(card.cmc)
        retCard.append(card.artist)
        retCard.append(card.type)
        
        return jsonify(retCard)
    else:
        if query:
            print("Query found in data:", query)
            cards = Card.where(name=query).all()
            retCards = []
            nameCheck = []
            for element in cards:
                if element.name and element.multiverse_id and element.image_url and element.set_name and element.cmc and element.artist and element.type and element.name not in nameCheck:
                    #element.power and element.toughness and element.loyalty and element.artist and
                    retCards.append(element.name)
                    retCards.append(element.multiverse_id)
                    nameCheck.append(element.name)
            return jsonify(retCards) # List to Set to List to avoid duplicates
        else:
            print("Query not found") 
            return jsonify([])