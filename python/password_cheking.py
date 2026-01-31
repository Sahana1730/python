def check_password(password):
    has_upper = has_lower = has_digit = has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    if len(password) < 8:
        return "Weak"

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif has_upper and has_lower and has_digit:
        return "Medium"
    else:
        return "Weak"

print(check_password("@Sahana.178"))
