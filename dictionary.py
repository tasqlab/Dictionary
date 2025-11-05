import requests

base = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get(word):
    final = base + word
    response = requests.get(final)

    if response.status_code == 200:
        data = response.json()
        try:
            meanings = data[0]['meanings']
            print(f"\nWord: {word}\n")
            for meaning in meanings:
                part_of_speech = meaning.get('partOfSpeech', 'N/A')
                print(f"Part of Speech: {part_of_speech}")
                for definition in meaning['definitions']:
                    def_text = definition.get('definition', 'No definition found.')
                    synonyms = definition.get('synonyms', [])
                    print(f" - Definition: {def_text}")
                    if synonyms:
                        print(f"   Synonyms: {', '.join(synonyms)}")
                print()
        except (IndexError, KeyError):
            print("Definition not found in the expected format.")
    else:
        print("Word not found or an error occurred.")

word = input("Enter a word: ")
get(word)
input("Press enter to continue...")