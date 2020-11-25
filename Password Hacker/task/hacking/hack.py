import socket
from sys import argv
from string import digits, ascii_lowercase


def all_casings(input_string):
    if not input_string:
        yield ""
    else:
        first = input_string[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(input_string[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(input_string[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing


if len(argv) < 3:
    print("Incorrect arguments")
else:
    comb = ascii_lowercase + digits
    ip = argv[1]
    port = int(argv[2])
    with socket.socket() as s, open("passwords.txt", "r") as f:
        s.connect((ip, port))
        for elem in f:
            found = False
            for case in all_casings(elem[len(elem) - 1]):
                s.send(case.encode())
                msg = s.recv(1024).decode()
                if msg == "Connection success!":
                    print(case)
                    found = True
                    break
                else:
                    continue
                break
