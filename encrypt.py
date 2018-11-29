import one_time

#Encrypt a file using a one-time padself.

LINE = 80*'-'

plaintext_file = 'alice.txt'
#Open the plaintext file in binary so we
#don't have to convert the text to bytes later.
with open(plaintext_file, 'rb') as f:
    plaintext = f.read()

print('Plaintext as bytestring:')
print(plaintext)
print(LINE)

ciphertext, pad = one_time.encrypt(plaintext)
print('Ciphertext as bytestring:')
print(ciphertext)
print(LINE)

print('One-time pad as bytestring:')
print(pad)
print(LINE)

print('Decrypted message:')
print(one_time.decrypt(ciphertext, pad))
