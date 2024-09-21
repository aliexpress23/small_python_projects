def calculate_gdp_expenditures():
    print("\nCalculating GDP using the Expenditures Approach")
    consumption = float(input("Enter Consumption (C): "))
    investment = float(input("Enter Investment (I): "))
    government_spending = float(input("Enter Government Spending (G): "))
    exports = float(input("Enter Exports (X): "))
    imports = float(input("Enter Imports (M): "))
    
    net_exports = exports - imports
    gdp_expenditures = consumption + investment + government_spending + net_exports
    print(f"\nGDP calculated using the Expenditures Approach is: {gdp_expenditures}")

def calculate_gdp_income():
    print("\nCalculating GDP using the Income Approach")
    wages = float(input("Enter Total Wages (W): "))
    rents = float(input("Enter Total Rents (R): "))
    interest = float(input("Enter Total Interest (I): "))
    profits = float(input("Enter Total Profits (P): "))
    
    gdp_income = wages + rents + interest + profits
    print(f"\nGDP calculated using the Income Approach is: {gdp_income}")

if __name__ == "__main__":
    print("Welcome to the GDP Calculator!")
    while True:
        print("\nChoose an option:")
        print("1. Calculate GDP using the Expenditures Approach")
        print("2. Calculate GDP using the Income Approach")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            calculate_gdp_expenditures()
        elif choice == '2':
            calculate_gdp_income()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
