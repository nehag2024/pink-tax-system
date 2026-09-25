from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        product1 = request.form["product1"]
        price1 = float(request.form["price1"])

        product2 = request.form["product2"]
        price2 = float(request.form["price2"])

        difference = price2 - price1
        percentage = (difference / price1) * 100

        if percentage > 10:
            message = "⚠️ Potential Unfair Pricing Detected!"
        else:
            message = "✅ No Significant Unfair Pricing Detected."

        result = {
            "product1": product1,
            "price1": price1,
            "product2": product2,
            "price2": price2,
            "difference": difference,
            "percentage": percentage,
            "message": message
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
