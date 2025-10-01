while True:

    Age=int(input('Enter your age: '))
    if Age<=12:
        print('The ticket price for your child is 5')
    elif Age>=13 and Age<=17:
        print('The ticket price for your teen is 7')
    elif Age>=18 and Age<=64:
        print('The price is 10')
    else:
        print('the price is 6')