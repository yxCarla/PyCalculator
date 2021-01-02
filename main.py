print('Welcome to the Calculator! Calculates only basic expressions.')

h = 1


def restart():
    global h

    cont = input('Would you like to continue? Please enter either yes or no.\n')

    if cont.lower() == 'yes':
        print('Alright!')
        h = 1
    if cont.lower() == 'no':
        h = 2
        print('Thank you for using the calculator!')
    if cont.lower() not in ('yes', 'no'):
        h = 2
        print('Invalid response received, exited.')


def calc_num():
    while h == 1:
        try:
            x = int(input('Enter the first number of your equation:\n'))
            y = int(input('Enter the second number of your equation:\n'))

            op = input('Which operation would you like to perform? Please enter either +, -, *, or /\n')

            if op == '+':
                print(f'{x} + {y} = ')
                print(x + y)
                restart()
            elif op == '-':
                print(f'{x} - {y} = ')
                print(x - y)
                restart()
            elif op == '*':
                print(f'{x} * {y} = ')
                print(x * y)
                restart()
            elif op == '/':
                print(f'{x} / {y} = ')
                print(x / y)
                restart()
            else:
                print('Bruh! Did you forget an operator? Try again.')
                calc_num()

        except ValueError:
            print('Invalid number! Try again.')
            calc_num()


calc_num()
