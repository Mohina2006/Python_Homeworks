def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.2f}")


principal = float(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual rate of return: "))
num_years = int(input("Enter the number of years: "))



invest(principal, annual_rate, num_years)
