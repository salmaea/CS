import sys

#Character encoding: Unicode UTF-8
UTF8 = 'UTF-8'

def encrypt(plaintext):
    '''Encrypt a message.'''
    #Generate a one-time pad using binary data from /dev/randomself.
    with open('/dev/random', 'rb') as r:
        pad = r.read(len(plaintext))

    #Take the XOR of the plaintext and the one-time pad.
    ciphertext = bytes(x ^ y for x,y in zip(plaintext,pad))
    return ciphertext, pad

def decrypt(ciphertext, pad):
    '''Decrypt a message.'''
    #Take the XOR of the ciphertext and the one-time padself.
    decoded_msg = bytes(x ^ y for x,y in zip(ciphertext,pad))
    return decoded_msg.decode(UTF8)
