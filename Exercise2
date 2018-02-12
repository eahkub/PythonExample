IPAddr = []

while True:
    menu = raw_input('1:Add IP\n2:Delete IP\n3:List IP\n'
                     '4:Ping\n5:Exit\nEnter menu: ')
    if menu == '5':
        break
    
    elif menu == '1':
        x = raw_input('New IP Address: ')
        IPAddr.append(x)
        
    elif menu =='2':
        del IPAddr[len(IPAddr)-1]
        
    elif menu =='3':
        print IPAddr
        
    elif menu =='4':
        for count in range (len(IPAddr)):
            print 'ping ' + IPAddr[count]
    
    else:
        print '\nInvalid menu\n'
