y = int(input('Enter year:'))

if y % 4 == 0:

    if y % 100 == 0:

        if y % 400 == 0:
            print('Leap Year')
            
        else:
            print('Not Leap Year')

    else:
        print('Leap Year')

else:
    print('Not Leap Year')

