# Tip Calculator: https://replit.com/@appbrewery/tip-calculator-end

def main():
    total = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
    tip = 1.0 + (float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100)
    split = int(input("How many people to split the bill? "))
    print(f"Each person should play: ${round((total * tip / split), 2)}")

if __name__ == "__main__":
    main()