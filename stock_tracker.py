# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 135,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

# User input
n = int(input("Enter number of stocks you want to add: "))

for i in range(n):
    stock_name = input("Enter stock symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        portfolio[stock_name] = quantity

        investment = stock_prices[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not available in price list.")

# Display Portfolio
print("\n--- Portfolio Summary ---")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    print(f"{stock} -> Quantity: {quantity}, Price: ${price}, Total: ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Save to text file
with open("portfolio_summary.txt", "w") as file:
    file.write("--- Portfolio Summary ---\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"{stock} -> Quantity: {quantity}, Price: ${price}, Total: ${investment}\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")