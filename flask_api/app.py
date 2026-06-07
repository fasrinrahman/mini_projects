from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 250000
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 5000
    }
]


# ------------------
# GET ALL PRODUCTS
# ------------------

@app.route("/products", methods=["GET"])
def get_products():

    return jsonify(products)


# ------------------
# GET PRODUCT BY ID
# ------------------

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):

    for product in products:

        if product["id"] == id:

            return jsonify(product)

    return jsonify(
        {"message": "Product not found"}
    ), 404


# ------------------
# ADD PRODUCT
# ------------------

@app.route("/products", methods=["POST"])
def add_product():

    data = request.json

    products.append(data)

    return jsonify(
        {
            "message": "Product added",
            "product": data
        }
    )


# ------------------
# DELETE PRODUCT
# ------------------

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):

    for product in products:

        if product["id"] == id:

            products.remove(product)

            return jsonify(
                {
                    "message": "Deleted successfully"
                }
            )

    return jsonify(
        {"message": "Product not found"}
    ), 404


if __name__ == "__main__":

    app.run(debug=True)
    
    