import tkinter as tk

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

def check_card():
    card_number = entry.get()
    if validator.validate_credit_card(card_number):
        result_label.config(text="Номер картки є дійсним.")
    else:
        result_label.config(text="Номер картки не є дійсним.")

validator = CardNumberValidator()

window = tk.Tk()
window.title("Валідатор кредитних карт")

label = tk.Label(window, text="Введіть номер кредитної картки:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Перевірити", command=check_card)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()