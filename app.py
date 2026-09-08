def detect_unfair_price(product1, product2, price1, price2):
    if price1 <= 0 or price2 <= 0:
        print("Invalid price entered.")
        return

    difference = price2 - price1
    percentage = (difference / price1) * 100

    print("\n===== PINK TAG SYSTEM =====")
    print(f"Product 1: {product1}")
    print(f"Price: ₹{price1:.2f}")

    print(f"\nProduct 2: {product2}")
    print(f"Price: ₹{price2:.2f}")

    print(f"\nPrice Difference: ₹{difference:.2f}")
    print(f"Percentage Difference: {percentage:.2f}%")

    if percentage > 10:
        print("\n⚠️ Potential Unfair Pricing Detected!")
    else:
        print("\n✅ No Significant Unfair Pricing Detected.")


if __name__ == "__main__":
    product1 = input("Enter Product 1 name: ")
    price1 = float(input("Enter Product 1 price: ₹"))

    product2 = input("Enter Product 2 name: ")
    price2 = float(input("Enter Product 2 price: ₹"))

    detect_unfair_price(product1, product2, price1, price2)
