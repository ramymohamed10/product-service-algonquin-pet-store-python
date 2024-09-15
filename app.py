from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

if __name__ == '__main__':
    # Get the port from the environment variable or default to 8000
    port = int(os.getenv('PORT', 3030))
    # Run the Flask application on the specified port
    app.run(host='0.0.0.0', port=port)
