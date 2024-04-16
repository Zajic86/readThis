import pyttsx3

# init and setting of eSpeak voice
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('pause', 0.5)  # Přidání pauzy 0.5 sekundy mezi slovy
engine.setProperty('volume', 1)
engine.setProperty('pitch', 0.9)
engine.setProperty('modulation', 0.5)  # Nastavení modulace na 0.5
engine.setProperty('emphasis', 'strong')  # Zvýraznění důležitých slov


def speak(text):
    engine.say(text)
    engine.runAndWait()
    inputText()


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
    print("")
    print("____________________________")
    print("  ReadThis - Text to voice  ")
    print("")

    print("Choose language for reading:")
    print("1. Čeština")
    print("2. Slovenčina")
    print("3. English")
    print("4. Deutsch")
    print("5. Polski")
    print("6. Español")
    print("7. Français")
    print("8. Magyar")
    print("9. Italiano")

    choice = input("Choose number of your language: ")
    if choice == "1":
        engine.setProperty('voice', 'cs')
    elif choice == "2":
        engine.setProperty('voice', 'sk')
    elif choice == "3":
        engine.setProperty('voice', 'en')
    elif choice == "4":
        engine.setProperty('voice', 'de')
    elif choice == "5":
        engine.setProperty('voice', 'pl')
    elif choice == "6":
        engine.setProperty('voice', 'es')
    elif choice == "7":
        engine.setProperty('voice', 'fr')
    elif choice == "8":
        engine.setProperty('voice', 'hu')
    elif choice == "9":
        engine.setProperty('voice', 'it')
    else:
        print("Bad choice, default language: English")
        engine.setProperty('voice', 'en')
    inputText()


def inputText():
    print("Text INPUT (or lang: change language, or exit to close program):")
    while True:
        text = input()
        if text.lower() == 'exit':
            break
        if text.lower() == 'lang':
            select_language()
        speak(text)


# MAIN
def main():
    select_language()


if __name__ == "__main__":
    main()