try:
    mob_no = input("Enter your 10-digit mobile number:")
    if not mob_no.isdigit():
        raise ValueError("Mobile number should contain digits only.")
    elif len(mob_no)!=10:
        raise ValueError("Mobile number must be exactly 10 digits.")
    else:
        print("Mobile number accepted:", mob_no)
        
except ValueError as e:
    print("Invalid input:", e)
