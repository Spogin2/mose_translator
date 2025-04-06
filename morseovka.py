# Slovník: písmena -> Morseova abeceda
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

# Slovník: Morseova abeceda -> písmena
reverse_morse_code = {v: k for k, v in morse_code.items()}

# Funkce: Překlad textu do Morseovy abecedy
def text_to_morse(text):
    words = text.upper().split()
    morse_words = []
    for word in words:
        morse_letters = []
        for char in word:
            if char in morse_code:
                morse_letters.append(morse_code[char])
        morse_words.append('|'.join(morse_letters))
    return '||'.join(morse_words)

# Funkce: Překlad Morseovy abecedy zpět do textu
def morse_to_text(morse):
    morse_words = morse.strip().split('||')
    decoded_words = []
    for word in morse_words:
        letters = word.split('|')
        decoded_letters = []
        for symbol in letters:
            decoded_letters.append(reverse_morse_code.get(symbol, '?'))
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)

# Hlavní program
print("MORSEOVKA ↔ TEXT PŘEKLADAČ")
print("--------------------------")

while True:
    volba = input("\nZadej 1 pro překlad do Morseovy abecedy,\n2 pro překlad z Morseovky zpět,\nQ pro konec: ").strip()

    if volba == '1':
        text = input("Zadej text: ")
        print("→ Morseova abeceda:")
        print(text_to_morse(text))

    elif volba == '2':
        morse = input("Zadej Morseovku (| mezi písmeny, || mezi slovy): ")
        print("→ Překlad do textu:")
        print(morse_to_text(morse))

    elif volba.upper() == 'Q':
        print("Na shledanou! 👋")
        break

    else:
        print("Neplatná volba, zkus to znovu.")
