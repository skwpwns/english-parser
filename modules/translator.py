from googletrans import Translator

def translate_to_korean(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='ko')
    return translation.text