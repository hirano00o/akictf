#!/usr/local/bin/python

import base64

str = '==AVoVGImxWYnBSazByUzMkUzQ1XLNTW'
code = ''

for i in range(len(str) -1, -1, -1):
    code += str[i]

print(code)
decode = base64.b64decode(code).decode('utf-8')
print(decode)

flag = ''
for i in range(len(decode) -1, -1, -1):
    flag += decode[i]

print(flag)
