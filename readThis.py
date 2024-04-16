import pyttsx3
import os
from gtts import gTTS


# init and setting of eSpeak voice
engine = pyttsx3.init()


def speak_with_pyttsx3(text, lang):
    engine.setProperty('voice', lang)
    engine.setProperty('rate', 170)
    engine.setProperty('pause', 0.5)
    engine.setProperty('volume', 1)
    engine.setProperty('pitch', 0.9)
    engine.setProperty('modulation', 0.5)
    engine.setProperty('emphasis', 'strong')
    engine.say(text)
    engine.runAndWait()


def speak_with_gtts(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system('mpg321 output.mp3')


def select_engine():
    print("")
    print("1. pyttsx3")
    print("2. gTTS")
    choice = input("Choose TTS engine:")
    return choice


# Select language
def select_language():
    # List of voices variants
    # voices = engine.getProperty('voices')
    # for voice in voices:
    # print("Language:", voice.languages[0])
    # print("Voice:", voice.name)
    # print("ID:", voice.id)
    # print("Gender:", "Male" if "male" in voice.id else "Female")
    # print()
    print("1. Čeština")
    print("2. Slovenčina")
    print("3. English")
    print("4. Deutsch")
    print("5. Polski")
    print("6. Español")
    print("7. Français")
    print("8. Magyar")
    print("9. Italiano")
    choice = input("Choose language for reading: ")
    if choice == "1":
        return "cs"
    elif choice == "2":
        return "sk"
    elif choice == "3":
        return "en"
    elif choice == "4":
        return "de"
    elif choice == "5":
        return "pl"
    elif choice == "6":
        return "es"
    elif choice == "7":
        return "fr"
    elif choice == "8":
        return "hu"
    elif choice == "9":
        return "it"
    else:
        print("Bad choice, default language: English")
        return "en"


def input_text():
    while True:
        print("Text INPUT (or lang: change language,    or exit to close program):")
        text = input()

        if text == "lang":
            lang = select_language()
            return text, lang
        if text == "exit":
            break
        return text, None


# MAIN
def main():
    engine_choice = select_engine()
    lang = select_language()

    while True:
        text, new_lang = input_text()
        if text is None:
            break
        if new_lang:
            lang = new_lang
        if engine_choice == "1":
            speak_with_pyttsx3(text, lang)
        elif engine_choice == "2":
            speak_with_gtts(text, lang)


if __name__ == "__main__":
    main()
