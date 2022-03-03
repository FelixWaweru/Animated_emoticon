import time
#
# charachters = ["( 0|0)", "( o|o)", "( -|-)", "( o|o)", "( 0|0)"]
# eyes = ["0", "o", "-"]
# x = 0
# for x in range(0, 3):
#     if x > 3:
#         print("( " + eyes[x] + " ͜ʖ " + eyes[x] + ")", end="\r")
#         x = x + 1
#         time.sleep(0.08)
#     else:
#         print("( " + eyes[x] + " ͜ʖ " + eyes[x] + ")", end="\r")
#         x = x - 1
#         time.sleep(0.08)


one = """
 (    )
\/\   \ 7 
   |_)_)
  /   /
  \   \ 
"""

two = """
 (    )
_/\   \ 7
   |_)_)
  /   /
  \   \ 
"""
three = """
 (    )
 /\   \ 7
 \ |_)_)
  /   /
  \   \ 
"""
four = """
 (    )
 /\   \ 7
 \  |_)_)
  /   /
  \   \ 
"""
five = """
 ('   )
\/\   \ 7  
   |_)_)
  /   /
  \   \ 
"""
six = """
 (-'  )
\/\   \ 7  
   |_)_)
  /   /
  \   \ 
"""
seven = """
 ('-' )
\/\   \ 7  
   |_)_)
  /   /
  \   \ 
"""
eight = """
 ('-^ )
\/\   \ 7  
   |_)_)
  /   /
  \   \ 
"""



def frame1():
    print(one, end="\b")
    time.sleep(0.15)


def frame2():
    print(two, end="\b")
    time.sleep(0.15)


def frame3():
    print(three, end="\r")
    time.sleep(0.15)


def frame4():
    print(four, end="\r")
    time.sleep(0.15)


def frame5():
    print(five, end="\r")
    time.sleep(0.15)


def frame6():
    print(six, end="\r")
    time.sleep(0.15)


def frame7():
    print(seven, end="\r")
    time.sleep(0.15)


def frame8():
    print(eight, end="\r")
    time.sleep(0.15)


def playBack():
    a = 1
    while a is 1:
        frame1()
        frame2()
        frame3()
        frame4()
        frame3()
        frame4()
        frame3()
        frame4()
        frame3()
        frame2()
        frame1()
        frame5()
        frame6()
        frame7()
        frame8()
        frame7()
        frame6()
        frame5() 

playBack()

