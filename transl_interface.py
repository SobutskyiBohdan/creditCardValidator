import tkinter as tk
from deep_translator import GoogleTranslator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Англійсько-український перекладач")

        self.input_label = tk.Label(self.master, text="Введіть текст на англійській:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.master, width=50)
        self.input_entry.pack()

        self.translate_button = tk.Button(self.master, text="Перекласти", command=self.translate_text)
        self.translate_button.pack()

        self.output_text = tk.StringVar()
        self.output_label = tk.Label(self.master, textvariable=self.output_text)
        self.output_label.pack()

    def translate_text(self):
        input_text = self.input_entry.get()
        translated_text = GoogleTranslator(source='en', target='uk').translate(input_text)
        self.output_text.set(translated_text)

def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
