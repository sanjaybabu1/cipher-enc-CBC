import os
import time
start = time.time()
from Crypto.Cipher import DES3
key = 'Sixteen byte key'
def encrypt_file(in_filename, out_filename, chunk_size, key, iv):
    des = DES3.new(key, DES3.MODE_CBC, iv)

    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                out_file.write(des.encrypt(chunk))

from Crypto import Random
iv = Random.get_random_bytes(8)
with open('to_enc.txt', 'r') as f:
    print 'to_enc.txt: %s' % f.read()
encrypt_file('to_enc.txt', 'to_enc.enc', 8192, key, iv)
with open('to_enc.enc', 'r') as f:
    print 'to_enc.enc: %s' % f.read()
end = time.time()
print(end - start)
