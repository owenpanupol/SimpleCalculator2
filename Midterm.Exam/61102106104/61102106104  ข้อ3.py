def menu():
    print('1.menu1')
    print('2.menu2')
    print('3.menu3')
    print('4.menu4')
    print('5.Exit')
    c = input('select your choice[1-5]')
    if c == '1':
        print('select.1.\n.........................................................................')
        menu()
    if c == '2':
        print('select.2.\n.........................................................................')
        menu()
    if c == '3':
        print('select.3.\n.........................................................................')
        menu()
    if c == '4': 
        print('select.4.\n..........................................................................')
        menu()
        
    if c == '5':
        print('Exit.\n.............................................................................')
        menu()
        print('....................................................................................')

menu()
 
            
            
    
