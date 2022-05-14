
from random import choice

def replace(text, dic):
    for i in dic:
        print(dic[i])
        text = text.replace(dic[i], "a").strip()
    return text


def read_data():
    words = []
    letters = []
    with open("./archivos/data.txt", "r", encoding="utf=8") as f:
        for line in f:
            words.append(line)
        cword = choice(words)
    with open("./archivos/abc.txt", "r", encoding="utf=8") as f:
        for line in f:
            letters.append(line.strip())

    print(len(letters))
    print(cword)
    cword = hide_word
    print(hide_word)
    for i in letters:
        hide_word = hide_word.replace(letters[i], "-")
    print(cword)
    print(hide_word)


def del_abc(word):
    abc = []
    with open("./archivos/abc.txt", "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0 and line.strip() != word:
                abc.append(line.strip())
    with open("./archivos/abd.txt", "w", encoding="uft-8") as f:
        for x in abc:
            f.write(x)
            f.write("\n")


def ask():
    pass


def run():
    read_data()


if __name__ == '__main__':
    run()
