# BUILD A TRAIN SEAT INFORMATION SYSTEM.

seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

if seat_type == "sleeper":
    print("Sleeper - No AC, beds available")
elif seat_type == "ac":
    print("AC - Air conditioned, comfy ride")
elif seat_type == "general":
    print("General - Cheapest option, no reservation")
elif seat_type == "luxury":
    print("Luxury - Premium seats with meals")
else:
    print("Invalid seat type")
