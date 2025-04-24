import sys, os

num = int(sys.argv[1]) % 26
if os.isatty(sys.stdin.fileno()):
    msg = input()
else:
    msg = sys.stdin.read()

msg = msg.upper()
final = ""
count = 0

for char in msg:

    if not char.isalpha():
        continue
    count+=1
    if (ord(char) + num) > 90:
        final+=chr(ord(char)+num-26)
    else:
        final+=chr(ord(char)+num)
        
    if count%5 == 0:
        final+=" "
        
    if count%50 == 0:
        final+="\n"

print (final)