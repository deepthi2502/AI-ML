from flask import Flask, render_template, request

# Use __name__ instead of _name_
app = Flask(__name__)

# Dictionary of food prices
prices = {"Biryani": 220, "Rice": 50, "Chicken": 180, "Soup": 100}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order():
    name = request.form["name"]
    foods = request.form.getlist("food")

    # Validate quantity input
    try:
        quantity = int(request.form["quantity"])
    except ValueError:
        message = "⚠ Quantity must be a number!"
        return render_template("index.html", message=message)

    # Validate food selection
    if not foods:
        message = "⚠ Please select at least one food item!"
        return render_template("index.html", message=message)

    # Calculate total bill
    total = sum(prices[item] * quantity for item in foods)

    return render_template(
        "bill.html",
        name=name,
        foods=foods,
        quantity=quantity,
        prices=prices,
        total=total
    )

# Use __name__ == "__main__" instead of _name_ == "_main_"
if __name__ == "__main__":
    app.run(debug=True)
