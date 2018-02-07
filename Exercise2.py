def AppendIP(x, IPAddr):
    return x.append(IPAddr)

def RmIP(x):
    return x.remove(x[len(x)-1])

ListIP = []
menu = '1'

while True:
    menu = raw_input('\n\nPlease input menu.\n1.Insert IP\n2.Delete IP\n'
                     '3.View IP\n4.Ping IP\n5.Exit\nYour choice:')
    if menu == '1':
        IPAppend = raw_input('Input added IP address: ')
        AppendIP(ListIP, IPAppend)
        
    elif menu == '2':
        RmIP(ListIP)
        
    elif menu == '3':
        print 'IP list: ', ListIP

    elif menu == '4':
        for count in range (0, len(ListIP)):
            print 'ping ', ListIP[count]
    elif menu == '5':
        break
    else:
        print 'Invalid menu'
