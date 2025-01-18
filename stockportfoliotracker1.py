import yfinance as yf

class StockPortfolio:
    def __init__(self):
        # Initialize the portfolio as an empty dictionary
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker]["shares"] += shares
        else:
            self.portfolio[ticker] = {"shares": shares}
        print(f"Added {shares} shares of {ticker} to your portfolio.")

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if self.portfolio[ticker]["shares"] >= shares:
                self.portfolio[ticker]["shares"] -= shares
                if self.portfolio[ticker]["shares"] == 0:
                    del self.portfolio[ticker]
                print(f"Removed {shares} shares of {ticker} from your portfolio.")
            else:
                print(f"You don't own enough shares of {ticker} to remove.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nYour Portfolio:")
        for ticker, data in self.portfolio.items():
            shares = data["shares"]
            try:
                stock = yf.Ticker(ticker)
                price = stock.history(period="1d")["Close"][-1]
                total_value = shares * price
                print(f"{ticker}: {shares} shares @ ${price:.2f} = ${total_value:.2f}")
            except Exception as e:
                print(f"Could not retrieve data for {ticker}. Error: {e}")
        print()

    def track_performance(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nPortfolio Performance:")
        total_value = 0
        for ticker, data in self.portfolio.items():
            shares = data["shares"]
            try:
                stock = yf.Ticker(ticker)
                price = stock.history(period="1d")["Close"][-1]
                total_value += shares * price
                print(f"{ticker}: {shares} shares @ ${price:.2f}")
            except Exception as e:
                print(f"Could not retrieve data for {ticker}. Error: {e}")
        print(f"Total Portfolio Value: ${total_value:.2f}\n")


def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter stock ticker symbol (e.g., AAPL, MSFT): ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == "2":
            ticker = input("Enter stock ticker symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            portfolio.track_performance()
        elif choice == "5":
            print("Exiting Stock Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
