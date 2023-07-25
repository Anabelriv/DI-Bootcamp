from googletrans import Translator

def translate_french_to_english(words):
    translator = Translator()
    translations = {}

    for word in words:
        translation = translator.translate(word, src='fr', dest='en')
        translations[word] = translation.text

    return translations

if __name__ == "__main__":
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    translations = translate_french_to_english(french_words)
    print(translations)
