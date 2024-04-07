from googletrans import Translator

def translate_text():
    try:
        translator = Translator()
        input_text = input("Введіть текст на англійській: ")
        translated_text = translator.translate(input_text, src='en', dest='uk').text
        print("Переклад українською: ", translated_text)
    except Exception as e:
        print("Виникла помилка: ", e)

if __name__ == "__main__":
    translate_text()