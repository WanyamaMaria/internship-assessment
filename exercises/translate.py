# Simple translator for English and 5 Ugandan languages

languages = ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"]

# Example dictionary for demonstration purposes
translations = {
    "How are you?": {
        "Luganda": "Oli otya?",
        "Runyankole": "Oli otya?",
        "Ateso": "Ibon aosi?",
        "Lugbara": "Mi ngoni?",
        "Acholi": "Itye nining?"
    },
    "Oli otya?": {
        "English": "How are you?"
    },
    "Ibon aosi?": {
        "English": "How are you?"
    },
    "Mi ngoni?": {
        "English": "How are you?"
    },
    "Itye nining?": {
        "English": "How are you?"
    }
}

def get_language_input(prompt):
    while True:
        print(f"{prompt} (Choose from: {', '.join(languages)}):")
        choice = input().strip()
        if choice in languages:
            return choice
        else:
            print("Invalid choice. Please try again.")

def main():
    source_lang = get_language_input("Please choose the source language")
    while True:
        target_lang = get_language_input("Please choose the target language")
        if target_lang != source_lang:
            break
        else:
            print("Source and target languages must be different.")

    text = input("Enter the text to translate:\n").strip()

    if text in translations and target_lang in translations[text]:
        print("Translation:", translations[text][target_lang])
    else:
        print("Sorry, translation not available for that input.")

if __name__ == "__main__":
    main()
