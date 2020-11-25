line = input()
key = sum((int(input())).to_bytes(2, byteorder="little"))
byte_message = bytearray(line, encoding="utf-8")
for i in range(len(byte_message)):
    byte_message[i] += key
print(byte_message.decode())
