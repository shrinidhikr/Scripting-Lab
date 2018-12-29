from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "secret"

@app.route("/", methods=["GET", "POST"])
def store():
    if request.method == "GET":
        return render_template("store.html")

    # For each item in store, checks if item is in session
    # If item is in session, increments the count by value entered in the form
    # If item is not in session, initialises the count by value entered in the form
    # Redirects to the HTML page to view Shopping Cart
    if request.method == "POST":
        for item in ["eggs", "milk", "bread"]:
            if item not in session :
                session[item] = int(request.form[item])
            else:
                session[item] += int(request.form[item])
        return redirect(url_for("cart"))
    

@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Creates a list of dictionaries containing each item in cart and its quantity
    # Displays this list in a HTML page
    cart = []
    for item in ["eggs", "milk", "bread"]:
        cart.append({"name":item.capitalize(), "quantity":session[item]})
    return render_template("cart.html", cart=cart)


@app.route("/buy", methods=["GET", "POST"])
def buy():

    # Total amount initialised to 0
    amount = 0

    # Index for list containing prices of items
    index = 0

    # Prices of every item
    prices = [5, 12, 22]

    # Creates a list of dictionaries containing each item in cart, its quantity, and cost(price*qty)
    # Calculates total bill amount
    # Displays the bill in a HTML page
    cart = []
    for item in ["eggs", "milk", "bread"]:
        row = {}
        row["name"] = item.capitalize()
        row["quantity"] = session[item]
        row["price"] = prices[index] * session[item]
        amount = amount + row["price"]
        cart.append(row)
        index = index + 1
    return render_template("bill.html", cart=cart, amount=amount)

if __name__ == '__main__':
	app.run(port=8000)