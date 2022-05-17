
from email.mime import image
from random import choice
import os

imagen = [
    '''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''', '''
 
   +---+
   |   |
       |
   O   |
  /|\  |
  / \  |
 =========''', '''

   +---+
   |   |
       |
 O     |
/|\    |
/ \    |
 =========''']


def restore_abc():
    abc = []
    with open("./archivos/abecedario.txt", "r", encoding="utf-8") as f:
        abc = [line.strip() for line in f]
    with open("./archivos/abc.txt", "w", encoding="utf-8") as f:
        for i in abc:
            f.write(i)
            if i != abc[len(abc) - 1]:
                f.write('\n')


def diff():
    valid = False
    while not valid:
        try:
            decision = int(input('''
        
    Seleccione la difultad: \n
    Palabras cortas: Seleccione " 1 " 
    Palabras largas: Seleccione " 2 "
    Salir : " 3 "

    '''))
            if not decision in range(1, 4):
                clean_window()
                print("\t-- Seleccion no valida -- \n")
                diff()

            return decision
        except ValueError:
            clean_window()
            print("Error: La seleccion no es un numero decimal")


def read_data(lives):
    cword = []
    with open("./archivos/data.txt", "r", encoding="utf=8") as f:
        if lives == 6:
            cword = choice([line.strip() for line in f if len(line) <= 7])
        if lives == 8:
            cword = choice([line.strip() for line in f if len(line) > 7])
    return(cword)


def clean_window(): return os.system("cls")


def impresion(spaced_word, lives):
    x = True
    ve = ""
    while x:
        try:
            # Imprime letras descubiertas

            print('''
============================
    Adivina la palabra 
============================ ''' + imagen[lives] + "\nTienes " + str(lives) + " vidas\n\n" + spaced_word)
            # Pregunta letra de entrada
            char = input("\n Ingresa una letra : ").upper()
            # if len(char) == 1 and (ord(char) in range(65, 90) or ord(char) in range(97, 122)):
            clean_window()
            if len(char) == 1 and char.isalpha():  # Maneja si la letra no es una sola letra
                ask(char)
                return char
            else:
                # Mensaje de error
                raise ValueError("\nIngrese una unica letra por favor\n")
        except ValueError as ve:
            print(ve)


def live(lives, cword, char):
    x = True
    for i in range(len(cword)):
        if char == cword[i]:
            x = False
    if x:
        lives = lives - 1
    return lives


def hide(text, dic):
    text2 = ""
    for i in dic:
        text = text.replace(i, "_")
    for i in range(len(text)):
        text2 = text2 + (text[i]) + " "
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
        s = s.replace(a, b)
    return s


def compare():
    letters = []
    with open("./archivos/abc.txt", "r", encoding="utf=8") as f:
        letters = [line.strip() for line in f]
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
        print("\n -- La letra *" + letter.upper() + "* ya fue seleccionada --")
        return
    with open("./archivos/abc.txt", "w", encoding="utf-8") as f:
        for i in abc:
            f.write(i)
            f.write('\n')


def run():
    y = 0
    clean_window()
    while y != 3:
        dif = diff()
        if dif == 1:
            lives = 6
        elif dif == 2:
            lives = 8
        else:
            print(" -- Juego terminado -- ")
            break
        clean_window()
        rev = False
        restore_abc()
        word = read_data(lives).upper()
        cword = normalize(word)
        letters = compare()
        hidden_word = hide(cword, letters)
        while rev == False and lives > 0:
            char = impresion(hidden_word, lives)
            lives = live(lives, cword, char)
            letters = compare()
            hidden_word = hide(cword, letters)
            if hidden_word.replace(" ", "") == cword:
                rev = True
        if rev == True:
            print("\n\n -- Felicidades Ganaste -- ")
        if lives == 0:
            print(image[0] + "\n\n -- Game Over --")
        print("La palabra era : " + word)


if __name__ == '__main__':
    run()
