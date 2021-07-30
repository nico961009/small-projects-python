#Programa de curso de algoritmos que utiliza un contador que disminuye y un número que sumenta en numeros pares.
def run ():
    num = 0
    count = 50

    while count != 0:
        print (num, count)
        num += 2
        count -= 1

if __name__ == '__main__':
    run()