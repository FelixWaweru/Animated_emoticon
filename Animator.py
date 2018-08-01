import time

charachters = ["( 0|0)", "( o|o)", "( -|-)", "( o|o)", "( 0|0)"]
eyes = ["0", "o", "-"]
x = 0
for x in range(0, 3):
    if x > 3:
        print("( " + eyes[x] + " ͜ʖ " + eyes[x] + ")", end="\r")
        x = x + 1
        time.sleep(0.08)
    else:
        print("( " + eyes[x] + " ͜ʖ " + eyes[x] + ")", end="\r")
        x = x - 1
        time.sleep(0.08)
