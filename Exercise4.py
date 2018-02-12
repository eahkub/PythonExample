import telnetlib
import time
import sys

host = '10.0.60.126'
port = '5022'
un = 'admin'
pw = 'nttcadmin'
buffer = ''

try:
    tn = telnetlib.Telnet(host, port)
except:
    print 'Error in telnet.'
    sys.exit()

tn.write('\r\n')
time.sleep(3)
tn.write(un + '\r\n')
time.sleep(1)
tn.write(pw + '\r\n')
time.sleep(1)

tn.write('conf t' + '\r\n')
time.sleep(1)
tn.write('int g 1/0' + '\r\n')
time.sleep(1)
tn.write('ip add 192.168.1.22 255.255.255.0' + '\r\n')
time.sleep(1)
tn.write('no shut' + '\r\n')
time.sleep(1)
tn.write('end' + '\r\n')
time.sleep(1)
for x in range (10, 24):
    buffer = ''
    tn.write('ping 192.168.1.'+str(x)+' repeat 2\r\n')
    buffer = tn.read_eager
    print buffer
    time.sleep(3)
    #time.sleep(1)
    #tn.expect(['#'],10)

tn.write ('XX123\r\n')

txtout = tn.read_until('#XX123')

tn.write('exit\r\n')
print txtout
