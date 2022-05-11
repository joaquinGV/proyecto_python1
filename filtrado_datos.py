from cProfile import label
from concurrent.futures.thread import _worker
from pprint import pprint


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    platzy_worker = list(
        filter(lambda worker: worker["language"] == "python", DATA))
    platzy_worker = list(map(lambda worker: worker["name"], platzy_worker))

    platzy = list(
        filter(lambda worker: worker["organization"] == "Platzi", DATA))
    platzy = list(map(lambda worker: worker["name"], platzy))

    adults = [worker["name"] for worker in DATA if worker["age"] > 18]

    # old_people = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA]

    def MapFunc(worker): return {**worker, **{"old": worker["age"] > 70}}
    old_people = list(map(MapFunc, DATA))

    for i in platzy_worker:
        print(i)

    print("--------------------------------")

    for i in platzy:
        print(i)

    print("--------------------------------")

    for i in adults:
        print(i)

    print("--------------------------------")

    for i in old_people:
        pprint(i)


if __name__ == '__main__':
    run()
