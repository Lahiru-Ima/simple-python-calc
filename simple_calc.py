import arithmetic as ari

print(">>>Calculater<<<")


def getNo():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    return no1, no2


while True:
    print("1).Add\n2).Sub\n3).Mul\n4).Div\n5).Exit")
    choice = int(input("Enter choice(1,2,3,4,5): "))

    if choice == 1:
        x, y = getNo()
        print(f'{x} + {y} = {ari.add(x, y)}')

    elif choice == 2:
        x, y = getNo()
        print(f'{x} - {y} = {ari.sub(x, y)}')

    elif choice == 3:
        x, y = getNo()
        print(f'{x} * {y} = {ari.mul(x, y)}')

    elif choice == 4:
        x, y = getNo()
        print(f'{x} / {y} = {ari.div(x, y)}')

    elif choice == 5:
        print('Bye!!!')
        break
    else:
        print("Invalid Choice")
