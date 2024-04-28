# Import the translator module I will be using.
from googletrans import Translator

# Initialize the translator variable to be used later
translator = Translator()
# Send a welcome message
print("Welcome to the Translator!")
"""
Add a list that provides all availibe languages so we can transfer
the language the user inputs into a country code
"""
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}
# Ask the user what sentence they would like to translate

# Initialize a variable for the users inputted text
untranslated_text = input("What would you like to translate? >> ")
# Create a function that will translate the user's text


def translate_text(text):
  # Detect which language the user's input is written in and store it
  detectedLang = translator.detect(text)
  """"
  Since the detect function stores the language and confidence level,
  we want to only store the language that was detected
  """
  originalLang = (detectedLang.lang)
  # Ask the user which languages they want their sentence translated into
  desiredLangs = []
  # Create a loop so the user can add as many languages as they want
  while True:
    # Ask the user which language(s) they want their sentence translated into
    anotherLang = input(
        "What language do you want your sentence to be translated to? (type q to quit) >> "
    ).lower()
    # If the user does not want to select any more languages, break the loop
    if anotherLang.lower() == "q":
      break
    # If the user does not input q, keep adding the languages into the list
    else:
      desiredLangs.append(anotherLang)
  # When user inputs all the languages, translate the sentence to each language
  # I did this by iterating through each item inside of the desiredLangs list
  for desiredLang in desiredLangs:
    # Create a key set to false to check each language in the list to find a match
    language_key = None
    # Iterate through the languages dictionary to find a match
    for key, value in LANGUAGES.items():
      # If the language is found, set the language key to the key
      if value == desiredLang:
        language_key = key
        break
    # If a valid language is found, let the user know and translate the statement
    if language_key:
      # Change the desired language to the matched language found in the list
      desiredLang = language_key
      print("Translating statement to " + str(language_key) + "!\n")
      # Translate the statement, and store it in a variable
      # Let the program know what language the statement is coming from
      # Do this by assigning the source parameter to the detected language
      translatedStatement = translator.translate(text,
                                                 dest=desiredLang,
                                                 src=originalLang)
      # Output the translated statement
      print(translatedStatement.text + "\n")
    # If a language was not found, let the user know that language didn't get a match
    else:
      print("No matching language found for " + str(desiredLang) + "!")


translate_text(untranslated_text)
