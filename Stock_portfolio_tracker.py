import yfinance as yf

# Dictionary to store user's stock holdings
portfolio = {}

def add_stock(symbol, shares):
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol}.")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"{symbol} not found.")

def show_portfolio():
    total_value = 0
    print("\nYour Portfolio:")
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1]
        value = shares * price
        print(f"{symbol}: {shares} shares @ ${price:.2f} = ${value:.2f}")
        total_value += value
    print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")

def main():
    while True:
        print("1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)

        elif choice == "3":
            show_portfolio()

        elif choice == "4":
            print("Exiting Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Try again.")

main()
