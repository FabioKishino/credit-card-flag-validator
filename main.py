import re

def get_credit_card_brand(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    
    patterns = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Maestro": r"^(?:5[06789]\d{0,2}|6\d{0,2})\d{12,15}$"
    }
    
    for brand, pattern in patterns.items():
        if re.match(pattern, card_number):
            return brand
    
    return "Unknown"

# Example usage
card_number = "3400 680394 14376"
brand = get_credit_card_brand(card_number)
print(f"The credit card brand is: {brand}")