tip_Request = input("Would you like to leave a tip? (yes/no) :")
if tip_Request == "yes":
    #continue Code
    total_bill = input("Okay how much was your bill? $")
    total_bill =float(total_bill)
    tip_Percent = input("how much would you like to tip? (10%, 12%, 15%)")
    tip_Percent = int(tip_Percent)
    tip_Percent = (tip_Percent / 100)
    people_Total = input("How many people are splitting the bill? :")
    people_Total = int(people_Total)
    final_total = (((total_bill * tip_Percent) + total_bill) / people_Total)
    final_total = round(final_total, 2)
    final_total = str(final_total)
    print("Each person needs to pay " + final_total)

else:
    pass