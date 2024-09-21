
def gotoxy(x,y): 
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def printRed(s):
    print(f"\033[31m{s}\033[m")

def printGreen(s):
    print(f"\033[32m{s}\033[m")

def printBlue(s):
    print(f"\033[34m{s}\033[m")

def printLI(s):
    print(f"\033[1;34m{s}\033[m")

def printCyt(s):
    print(f"\033[0;36m{s}\033[m")

def printYELLOW(s):
    print(f"\033[1;33m{s}\033[m")