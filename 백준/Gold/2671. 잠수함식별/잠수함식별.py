# 잠수함식별
import re
import sys
input = sys.stdin.readline

string = input().rstrip()

regex = re.compile('(100+1+|01)+')

if regex.fullmatch(string):
    print("SUBMARINE")
else:
    print("NOISE")
