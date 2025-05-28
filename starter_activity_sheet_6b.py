def logging_in ( ):
    print ("Enter your password on the next line ") 
    password = input() 
    while password != "secret" :
        print ("That password is not the one stored") 
        print ("Try again! ") 
        password = input()
        
    print ("Yes that's the correct password! ") 
