print("Loading...")

from googletrans import Translator
import random
import pandas as pd
from fuzzywuzzy import fuzz

# Create a translator object
translator = Translator()

# List of phrases we will translate they should be on the longer side
phrases = [
    "No parking",
    "No smoking",
    "Beware of the dog",
    "Police station",
    "Fire station",
    "Do not enter",
    "No trespassing",
    "No skateboarding",
    "Authorized personnel only",
    "Free wifi",
    "Free parking",
    "Quiet please",
    "Welcome to the library",
    "Thank you for your cooperation",
    "Please do not touch",
    "Please do not feed the animals",
    "Please do not litter",
    "Traffic doesn't stop",
    "Yield ahead",
    "No left turn",
    "Road work ahead",
    "Pedestrian crossing",
    "Buy one get one free",
    "Buy mobile sim cards here",
    "Phones and accessories",
    "Number one in service",
    "We accept credit cards",
    "Horses for sale",
    "We sell fruits and vegetables",
    "We sell fresh fish",
]

language_to_country = {
    "ko": "South Korea",
    "es": "Spain",
    "no": "Norway",
    "hi": "India",
    "uk": "Ukraine",
    "nl": "Netherlands",
    "it": "Italy",
    "de": "Germany",
    "ur": "Pakistan",
    "pl": "Poland",
    "ar": "Saudi Arabia",
    "gd": "Scotland",
    "fr": "France",
    "sr": "Serbia",
    "cs": "Czech Republic",
    "ru": "Russia",
    "ga": "Ireland",
    "pt": "Portugal",
    "kk": "Kazakhstan",
    "az": "Azerbaijan",
    "ja": "Japan",
    "tl": "Philippines",
    "vi": "Vietnam",
    "zh-cn": "China",
    "sq": "Albania",
    "hu": "Hungary",
    "en": "United States",
    "fa": "Iran",
    "sv": "Sweden",
    "iw": "Israel",
    "ta": "Sri Lanka",
    "th": "Thailand",
    "ro": "Romania",
    "el": "Greece",
    "tr": "Turkey",
    "id": "Indonesia",
    "ms": "Malaysia",
}

# Dictionary mapping language codes to full names
code_to_language = {
    "ko": "Korean",
    "es": "Spanish",
    "no": "Norwegian",
    "hi": "Hindi",
    "uk": "Ukrainian",
    "nl": "Dutch",
    "it": "Italian",
    "de": "German",
    "ur": "Urdu",
    "pl": "Polish",
    "ar": "Arabic",
    "gd": "Scottish",
    "fr": "French",
    "sr": "Serbian",
    "cs": "Czech",
    "ru": "Russian",
    "ga": "Irish",
    "pt": "Portuguese",
    "kk": "Kazakh",
    "az": "Azerbaijani",
    "ja": "Japanese",
    "tl": "Filipino",
    "vi": "Vietnamese",
    "zh-cn": "Chinese",
    "sq": "Albanian",
    "hu": "Hungarian",
    "en": "English",
    "fa": "Persian",
    "sv": "Swedish",
    "iw": "Hebrew",
    "ta": "Tamil",
    "th": "Thai",
    "ro": "Romanian",
    "el": "Greek",
    "tr": "Turkish",
    "id": "Indonesian",
    "ms": "Malay",
}

languages = list(code_to_language.keys())

# Dictionary mapping language full names to their codes
language_to_code = {v.lower: k for k, v in code_to_language.items()}

# Attempt to load data.csv as pd
try:
    data = pd.read_csv("data.csv")
    # print("Loaded data.csv")

    # # Ask user if the username is correct if so then set the username else ask for new username
    # usernameQ = input(f"Is {data['username'][0]} your username? (y/n) ").lower()
    # if usernameQ == "n":
    #     username = input("Enter your username: ")
    # else:
    #     username = data["username"][0]
    username = data["username"][0]


except FileNotFoundError:
    print("Could not find data.csv")
    data = pd.DataFrame()
    # If new create initial columns, langauge, guessed, correct
    username = input("Enter your username: ")
    data["username"] = ""
    data["language"] = ""
    data["guessed"] = ""
    data["correct"] = False

# Translate hello username into a random language
translated = translator.translate(
    "Hello " + username + "!", dest=random.choice(languages)
)
print(translated.text)

# # Go through data and convert the guess to the language code
# for index, row in data.iterrows():
#     guess = row["guessed"]
#     row["guessed"] = language_to_code.get(guess, guess)


def play_game():
    # Pick a random language
    language = random.choice(languages)

    # Pick a random phrase
    phrase = random.choice(phrases)

    # Translate the phrase into the selected language
    translated = translator.translate(phrase, dest=language)

    print(f"Guess the language of this phrase: '{translated.text}'")

    guess = input("Your guess: ").lower()

    if guess == "quit":
        return False

    # Get the country and full name of the language
    country = language_to_country.get(language, "Unknown")
    full_name = code_to_language.get(language, "Unknown")

    if guess == "skip" or guess == "":
        print(
            f"The language is {full_name} ({language}), which is primarily spoken in {country}."
        )
        return True

    correct = False

    # Convert the guess to the language code by finding the closest match
    highest = 85
    guessed = guess
    for lang in languages:
        ratio = fuzz.ratio(guess, lang)
        if ratio > highest:
            highest = ratio
            guessed = lang
        ratio = fuzz.ratio(guess, language_to_country.get(lang, lang).lower())
        if ratio > highest:
            highest = ratio
            guessed = lang
        ratio = fuzz.ratio(guess, code_to_language.get(lang, lang).lower())
        if ratio > highest:
            highest = ratio
            guessed = lang

    # Check if the guess is correct
    if (guessed == language) or (guessed == country) or (guessed == full_name):
        print(
            f"Correct! This is {full_name} ({language}), which is primarily spoken in {country}."
        )
        correct = True
    else:
        print(
            f"Wrong. The correct answer is {full_name} ({language}), which is primarily spoken in {country}. While you guessed {code_to_language.get(guessed,guessed)}."
        )

    # Add the data to the dataframe as a new row
    data.loc[len(data)] = [username, language, guessed, correct]

    data.to_csv("data.csv")

    return True


while True:
    # Ask if they would like to look at their data or play
    play = input(
        "Would you like to play or look at your data? (play/data/quit) "
    ).lower()

    if play == "data":
        # Print statistics about the data
        print(f"Total guesses: {len(data)}")
        # Print ratio of correct guesses
        print(
            f"Correct guesses: {len(data[data['correct'] == True])} ({len(data[data['correct'] == True])/len(data)*100:.2f}%)"
        )

        # Print the most common correct guesses langague
        print(
            f"Most common correct guess: {code_to_language.get(data[data['correct'] == True]['language'].value_counts().index[0], 'Unknown')} ({data[data['correct'] == True]['language'].value_counts()[0]})"
        )

        # Print the most common incorrect langague
        print(
            f"Most common incorrect guess: {code_to_language.get(data[data['correct'] == False]['language'].value_counts().index[0], 'Unknown')} ({data[data['correct'] == False]['language'].value_counts()[0]})"
        )

        # Print most common mistakes (example: it is polish but you guess russian often) up languages

        # Create a new dataframe containing only incorrect guesses
        incorrect = data[data["correct"] == False]

        # Group the incorrect guesses by the actual language and the guessed language, and count the size of each group
        mixups = (
            incorrect.groupby(["language", "guessed"]).size().reset_index(name="counts")
        )

        # Sort the groups by size in descending order
        mixups = mixups.sort_values("counts", ascending=False)

        print("Most common mix-ups:")

        # Print the top 5 mix-ups
        for i in range(min(5, len(mixups))):
            row = mixups.iloc[i]
            actual = code_to_language.get(row["language"], "Unknown")
            guessed = code_to_language.get(row["guessed"], row["guessed"])
            count = row["counts"]
            print(
                f"\tActual language was {actual}, but guessed {guessed} {count} times."
            )

    if play == "play":
        while play_game():
            pass

    if play == "quit":
        data.to_csv("data.csv")
        break
