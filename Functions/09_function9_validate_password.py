def validate_password(password):
    if len(password) < 8 :
        return("Weak password")

    has_upper = False
    has_lower = False
    has_num   = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_num = True

    if has_upper and has_lower and has_num:
        return("Strong password")
    else:
        return("Weak password")

password = input("Please enter your password: ")
    
print(validate_password(password))
 
