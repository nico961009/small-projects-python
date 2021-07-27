def collatz(number):
        if number % 2 == 0: #even number
            return number // 2
        elif number % 2 == 1: #odd number
            return 3 * number + 1
        else:
            print('something went wrong')
            return None

number= collatz(int(input('Give me a number=')))

while (number != 1):
    number= collatz(number)
    print(number)
print(number)
