#/usr/local/bin/python

import base64

conv = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
cipher = 'rKrUl+/clKHb4u/sm6sgnaPfnO/XkO=ewqPU45bRjp4gwa7NntoM467Onu/enqPRlakgj6Egjp0e1gAA'
code = ''

for i in cipher:
    for n, j in enumerate(conv):
        if i == j:
            code += conv[len(conv) - 1 - n]
            break

print(code)
dec = base64.b64decode(code)
print(dec)
