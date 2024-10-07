starting_balance = float(input("What is the principle amount?: $"))
interest = float(input("What is the interest?: "))

total_interest = 0

print("Year","  Beginning Balance"," Ending Balance")
for x in range (1, 6, 1):
    annual_interest = starting_balance * interest
    end_balance = starting_balance + annual_interest

    print(x,"     $",starting_balance,"         $",end_balance)

    starting_balance = starting_balance + annual_interest
    total_interest = total_interest + annual_interest
    



print("Total interest earned: $",total_interest)

    
