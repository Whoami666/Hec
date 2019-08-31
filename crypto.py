header = "What do you think about this: "

message = open('cipher.txt', 'r').read()
#message = header + content
msg_len = len(message)
crypto = ""

for i in range(len(header)):
    print(chr( int(ord(header[i])) ^ int(message[i]) ), end = '')
   

open('cipher.enc', 'w').write(crypto)