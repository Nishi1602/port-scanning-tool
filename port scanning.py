from socket import * 
ip = input ("ENTER THE IP ADDRESS : ")
port_start = int (input("enter the port to start the scan from :"))
port_stop = int (input("enter the port to stop the scan on :"))
main_array=[]
for port in range (port_start,port_stop+1):
    addr =(ip,port)
    s = socket(AF_INET,SOCK_STREAM)
    result = s.connect_ex(addr)
    setdefaulttimeout(0.01)
    s.close()
    if (result == 0 ):
        print("the port number {} is open ".format(port))
        main_array.append(port)
    else:
        print("the port number  {}is not open").format(port)
        print("-"*40)
        print ("the scanning is done...")
        print ("the port which ae open are :")
        print (main_array)