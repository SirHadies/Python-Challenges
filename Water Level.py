#simple water level if else task
water_level = input("What is the water level :")
water_level = int(water_level)
if water_level > 80:
    print("Drain the water now!")
elif water_level < 20:
    print("The water level is low!")
else:
    print("The water level is within normal paramiters")

