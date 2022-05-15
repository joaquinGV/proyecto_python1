
from random import choice
import re
import os


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


def clean_window(): return os.system("cls")


def impresion(spaced_word):
    x = True
    ve = ""
    while x:
        try:
            # Imprime letras descubiertas
            print("Adivina la palabra\n" + "\n\n" + spaced_word)
            # Pregunta letra de entrada
            char = input("\n Ingresa una letra : ").upper()
            # if len(char) == 1 and (ord(char) in range(65, 90) or ord(char) in range(97, 122)):
            if len(char) == 1 and char.isalpha():  # Maneja si la letra no es una sola letra
                ask(char)
                x = False
            else:
                # Mensaje de error
                raise ValueError("\nIngrese una unica letra por favor\n")
        except ValueError as ve:
            print(ve)


def hide(text, dic):
    for i in dic:
        text = text.replace(i, "_")
    return text


def spaced(text):
    text2 = ""
    for i in range(len(text)):
        text2 = text2 + (text[i] + " ")
    return text2


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
    spaced_word = spaced(hidden_word)
    while rev == False:
        try:
            clean_window()
            impresion(spaced_word)
            letters = compare()
            hidden_word = hide(cword, letters)
            spaced_word = spaced(hidden_word)
            rev = revision(hidden_word, cword)
        except ValueError as ve:
            print(ve)

        # clean_window()  # Limpia la pantalla
    print("\n\n -- Felicidades Ganaste -- \n  La palabra era : " + word)


if __name__ == '__main__':
    run()
