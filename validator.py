class CardNumberValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate_credit_card(card_number):
        card_number = card_number.replace(" ", "")

        if not card_number.isdigit():
            return False

        if len(card_number) != 16:
            return False

        total = 0
        for digitNumber in range(0, 16, 2):
            digit = int(card_number[digitNumber]) * 2
            if digit > 9:
                digit -= 9
            total += digit

        for digitNumber in range(1, 16, 2):
            total += int(card_number[digitNumber])

        if total % 10 == 0:
            return True
        else:
            return False

def check_multiple_cards():
    validator = CardNumberValidator()
    while True:
        card_number = input("Введіть номер кредитної картки або натисніть 'q' для виходу: ")
        if card_number.lower() == 'q':
            break
        if validator.validate_credit_card(card_number):
            print("Номер картки є дійсним.")
        else:
            print("Номер картки не є дійсним.")


check_multiple_cards()