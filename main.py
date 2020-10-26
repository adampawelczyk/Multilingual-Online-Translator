import requests
from bs4 import BeautifulSoup


class Translator:

    def __init__(self):
        self.languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese", "Dutch", "Polish",
                          "Portuguese", "Romanian", "Russian", "Turkish", "Chinese"]
        self.translate_to = None
        self.translate_from = None
        self.translate_word = None
        self.headers = \
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                           ' Safari/537.36'}
        self.translations = None
        self.examples = None

    def menu(self):
        print("Hello, you're welcome to the translator.\n")
        while True:
            for (i, language) in enumerate(self.languages, start=1):
                print(f"{i}. {language}")
            print("\n0. Exit\n")
            try:
                self.translate_from = int(input("Type the number of your language: "))
                if self.translate_from == 0:
                    print("\nBye!")
                    exit()
                self.translate_to = int(input("Type the number of language you want to translate: "))
                if self.translate_to == 0:
                    print("\nBye!")
                    exit()
                self.translate_word = input("Type the word you want to translate: ")
            except ValueError:
                print("\nIncorrect data!\n")
            else:
                self.translate()

    def translate(self):
        url = f"https://context.reverso.net/translation/{(self.languages[self.translate_from - 1]).lower()}-" \
              f"{(self.languages[self.translate_to - 1]).lower()}/{self.translate_word.lower()}"
        try:
            response = requests.get(url, headers=self.headers)
            if response:
                soup = BeautifulSoup(response.content, "html.parser")
                self.translations = [i.text.strip() for i in soup.select("#translations-content > .translation")]
                self.examples = [i.text.strip() for i in soup.select("#examples-content .text")]
                self.print_translation()
            else:
                print(f"\nSorry, unable to find {self.translate_word}\n")
        except requests.exceptions.ConnectionError:
            print("\nSomething wrong with your internet connection\n")

    def print_translation(self):
        if not self.translations:
            print(f"\nTranslator doesn't support translation from {self.languages[self.translate_from - 1]} to "
                  f"{self.languages[self.translate_to - 1]}\n")
        else:
            print(f"\n{self.languages[self.translate_to - 1]} Translations:")
            for i in self.translations[:6]:
                print(i)
            print(f"\n{self.languages[self.translate_to - 1]} Examples:")
            for i in range(0, 10, 2):
                print(self.examples[i])
                print(self.examples[i + 1] + '\n')


Translator().menu()
