#Input
StockSymbol = input("Enter Stock Symbol: ")
ShareAmount = float(input("Enter Amount of Shares Owned: "))
CostPerShare = float(input("Enter Cost per Share: "))

#Process
AmountInvested = ShareAmount * CostPerShare

#Output
print("Amount Invested: $", AmountInvested)