import time
x = 0
for x in range (0,5):  
    b = "Loading" + "." * x
    print (b, end="\r")
    x = x+1
    time.sleep(1)