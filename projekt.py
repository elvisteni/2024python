import random

def choose_word():
    """Zgjedh një fjalë të rastësishme nga një listë fjalësh."""
    words = ["blerton", "albin", "elesan", "elvs", "diart"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Kthen fjalën me shkronjat e zbuluara dhe vizat e tjera."""
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    return displayed

def hangman():
    """Funksioni kryesor i lojës Hangman."""
    word = choose_word()
    guessed_letters = set()  # Set për shkronjat e zbuluara
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Maksimumi i gabimeve të lejuara
    print("Loja Hangman! Gjej fjalën e fshehur.")
    print("_ " * len(word))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Zgjidhni një shkronjë: ").lower()

        # Kontrollon nëse zgjedhja është e vlefshme
        if len(guess) != 1 or not guess.isalpha():
            print("Zgjedhje jo e vlefshme. Ju lutemi zgjidhni një shkronjë.")
            continue

        if guess in guessed_letters:
            print("Keni zgjedhur tashmë këtë shkronjë. Provoni përsëri.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Shkronja '{guess}' është në fjalë!")
        else:
            incorrect_guesses += 1
            print(f"Shkronja '{guess}' nuk është në fjalë. Ju keni bërë {incorrect_guesses} gabime.")

        # Shfaq fjalën aktuale me shkronjat e zbuluara
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        # Kontrollon nëse lojtari ka fituar
        if "_" not in displayed_word:
            print("Urime! Ju keni fituar.")
            return

    print(f"Fatkeqësisht, ju keni humbur. Fjalë ishte: {word}")

# Filloni lojën
hangman()s
