print(type(ord('a')))
while True:
    val = input('type yo shit here:  ')
    numval = int(ord(val))
    if numval >= int(ord('0')) and numval <= int(ord ('9')):
        print('this is number')
    elif numval == int(ord('.')):
        break
    elif numval >= int(ord('A')) and numval <= int(ord ('Z')):
        print('this is a capital letter')
    elif numval >= int(ord('a')) and numval <= int(ord ('z')):
        print('this is a lowercase letter')
    else:
        print('this is a special')