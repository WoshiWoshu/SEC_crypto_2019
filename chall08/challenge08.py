#!/bin/python3

import sys
import base64

def count_repetition(ciphertext, num_line):
    partition = []
    cipher_length = len(ciphertext)
    for idx in range(0, cipher_length, 16):
        partition.append(ciphertext[idx:idx+16])
    rep = len(partition) - len(set(partition))
    result = {"num":num_line, "rep":rep}
    return (result)

ciphertext = []
try:
    with open(sys.argv[1]) as f:
        content = f.read()
        if (content == ""):
            raise NotImplementedError
        for line in content.splitlines():
            curr = base64.b64decode(line.strip())
            ciphertext.append(curr)
    repetition = [count_repetition(cipher, idx + 1) for idx, cipher in enumerate(ciphertext)]
    most_repetition = sorted(repetition, key=lambda x:x["rep"], reverse=True)
    print(most_repetition[0]["num"])
except:
    exit(84)