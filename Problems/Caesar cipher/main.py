n = input()
res = ""
for elem in n:
    res += chr(ord(elem) + 1)
print(res)
