
from random import choice
import re


def restore_abc():
    abc = []
    with open("./archivos/abecedario.txt", "r", encoding="utf-8") as f:
        for line in f:
            abc.append(line.strip())
    with open("./archivos/abc.txt", "w", encoding="utf-8") as f:
        for i in abc:
            f.write(i)
            if i != abc[len(abc) - 1]:
                f.write('\n')


def read_data():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf=8") as f:
        for line in f:
            words.append(line.strip())
        cword = choice(words)
    return(cword)


def hide(text, dic):
    for i in dic:
        text = text.replace(i, "_")
    return text


def normalize(s):  # It removes the accents of a string
    replacements = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def compare():
    letters = []
    with open("./archivos/abc.txt", "r", encoding="utf=8") as f:
        for line in f:
            letters.append(line.strip())
    return letters


def ask(letter):
    abc = []
    abc2 = []
    with open("./archivos/abc.txt", "r", encoding="utf-8") as f:
        for line in f:
            abc2.append(line.strip())
            if len(line.strip()) > 0 and line.strip() != letter:
                abc.append(line.strip())
    if abc == abc2:
        print("\n -- Esta letra ya fue seleccionada --")
        return
    with open("./archivos/abc.txt", "w", encoding="utf-8") as f:
        for i in abc:
            f.write(i)
            f.write('\n')


def revision(hidden_word, word):
    state = False
    if hidden_word == word:
        state = True
    return state


def run():
    rev = False
    restore_abc()
    word = read_data().upper()
    cword = normalize(word)
    letters = compare()
    hidden_word = hide(cword, letters)
    while rev == False:
        try:
            print("Adivina la palabra\n" + cword + "\n\n" + hidden_word)
            char = input("\n Ingresa una letra : ").upper()
            if len(char) == 1:
                ask(char)
            else:
                raise ValueError("\nSolo una letra por favor\n")
            letters = compare()
            hidden_word = hide(cword, letters)
            rev = revision(hidden_word, cword)
        except ValueError as ve:
            print(ve)
    print("\n\n -- Felicidades Ganaste -- \n  La palabra era : " + word)


if __name__ == '__main__':
    run()
