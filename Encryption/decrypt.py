import one_time

#Decrypt a file using a one-time pad.

LINE = 80*'_'
ciphertext_file = 'message.dat'
#Open the ciphertext file in binary mode.
#This means we read the file as bytes objects.
with open(ciphertext_file, 'rb') as f:
    ciphertext = f.read()

pad_file = 'pad.dat'
#Read the one-time pad.
with open(pad_file, 'rb') as f:
    pad = f.read()

print('Ciphertext as bytestring:')
print(ciphertext)
print(LINE)

print('One-time pad as bytestring:')
print(pad)
print(LINE)

print('Decrypted message:\n')
print(one_time.decrypt(ciphertext, pad))
