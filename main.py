import VersionQueue

verQ2 = VersionQueue.VersionQueueV2()
option = ''
while option != 'q':
    print('choose mode:-\te : Enqueue\td : Dequeue\tp : print \tq : Quit')
    option = input('Please enter your choice : ')
    if option == 'e':
        value = int(input('Please enter the number to insert : '))
        verQ2.enqueue(value)
    elif option == 'd':
        print('removed the value : ',verQ2.dequeue())
    elif option == 'p':
        value = int(input('Please enter the version of the queue, leave empty for latest version : '))
        print(verQ2.printQueue(value))
    elif option == 'q':
        break
    else:
        print('invalid option')