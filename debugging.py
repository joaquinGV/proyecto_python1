def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingrese un numero : "))
        if num < 1:
            raise ValueError("No se debe ingresar numeros menores a 1")
        print(divisors(num))
        print("Programa finalizado")
    except ValueError as ve:
        if ve != '':
            print("Debes ingresar números positivos")
        print(ve)


if __name__ == '__main__':
    run()
